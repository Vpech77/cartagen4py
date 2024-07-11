from functools import reduce
import operator
import math
import shapely
import numpy as np
from shapely import Point, LineString, Polygon

from cartagen4py.utils.geometry.angle import angle_2_pts, angle_3_pts
from cartagen4py.utils.math.vector import Vector2D

def polygon_compactness(polygon):
    """
    Calculate the compactness of a polygon.

    This function calculates the compactness of a polygon
    using the Miller index. This index gives a maximum
    value of 1 for circles.

    Parameters
    ----------
    polygon : Polygon
        The polygon to calculated the compactness from.

    Returns
    -------
    float

    Notes
    -----
    The Miller index is calculated using :math:`(4·pi·area)/(perimeter^2)`

    Examples
    --------
    >>> polygon = Polygon([(0, 0), (0, 1), (1, 1), (1, 0), (0, 0)])
    >>> polygon_compactness(polygon)
    0.7853981633974483
    """
    return 4 * np.pi * polygon.area / (polygon.exterior.length * polygon.exterior.length)

def polygon_elongation(polygon):
    """
    Calculate the elongation of a polygon.

    This function calculates the elongation of a polygon
    using the :func:`minimum_rotated_rectangle <shapely.minimum_rotated_rectangle>`.
    It is the ratio between the length and the width of this rectangle.

    Parameters
    ----------
    polygon : Polygon
        The polygon to calculated the elongation from.

    Returns
    -------
    float

    Examples
    --------
    >>> polygon = Polygon([(0, 0), (0, 1), (2, 1), (2, 0), (0, 0)])
    >>> polygon_elongation(polygon)
    2.0
    """
    points = polygon.exterior.coords
    ssr = shapely.MultiPoint(points).minimum_rotated_rectangle.exterior.coords

    x0, x1, x2 = ssr[0][0], ssr[1][0], ssr[2][0]
    y0, y1, y2 = ssr[0][1], ssr[1][1], ssr[2][1]

    length = np.sqrt((x1 - x0) * (x1 - x0) + (y1 - y0) * (y1 - y0))
    width = np.sqrt((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1))

    if length < width:
        length, width = width, length

    return length / width

def polygon_concavity(polygon):
    """
    Calculate the concavity of a polygon.

    This function calculates the concavity of a polygon as
    its area divided by the area of its convex hull.

    Parameters
    ----------
    polygon : Polygon
        The polygon to calculated the concavity from.

    Returns
    -------
    float

    Examples
    --------
    >>> polygon = Polygon([(0, 0), (0, 2), (1, 1), (2, 2), (2, 0), (0, 0)])
    >>> polygon_concavity(polygon)
    0.75
    """
    hull = shapely.convex_hull(polygon)
    return polygon.area / hull.area

from cartagen4py.utils.debug import plot_debug

def enclosing_rectangle(polygon, mode='hull', property='minimum area'):
    """
    Construct an enclosing rectangle from a polygon.

    This function relies on the rotating calipers algorithm
    proposed by Toussaint. :footcite:p:`toussaint:1983`
    The idea is to simulate the rotation of a spring-loaded
    vernier caliper around the outside of a convex polygon.
    Using this approach, an enclosing rectangle can be calculated
    for each side of the convex hull of the polygon as
    described by Bayer. :footcite:p:`bayer:2009`

    Parameters
    ----------
    polygon : Polygon
        The polygon to calculate its enclosing rectangle from.
    mode : str, optional
        The type of enclosing rectangle wanted.
        In 'hull' mode, a rectangle is calculated for every side of the convex
        hull to return the right one.
        In 'input' mode, a rectangle is calculated only if the side of the convex
        hull is also the side of the provided polygon
    property : str, optional
        Which geometric property to consider to return the rectangle.
        'minimum area', 'maximum area', 'minimum length', 'maximum length'
        Length represents the longest side of the rectangle.

    Returns
    -------
    Polygon :
        The enclosing rectangle. Its vertexes are ordered clockwise
        and it starts in its southwestern corner. 

    References
    ----------
    .. footbibliography::

    Examples
    --------
    >>> polygon = Polygon([ (0, 0), (0, 1), (1, 1), (1, 2), (2, 2), (2, 0), (0, 0) ])
    >>> enclosing_rectangle(polygon)
    <POLYGON ((0 0, 0 2, 2 2, 2 0, 0 0))>
    """
    # Storage for allowed modes and properties
    modes = ['hull', 'input']
    properties = ['minimum area', 'maximum area', 'minimum length', 'maximum length']

    # Raise exceptions in case of wrong input
    if mode not in modes:
        raise Exception('Chosen mode for bounding rectangle not handled: {0}.'.format(mode))
    if property not in properties:
        raise Exception('Chosen property for bounding rectangle not handled: {0}.'.format(property))

    # Retrieve the boundary list of coordinates
    boundary = polygon.boundary
    bcoords = list(boundary.coords)

    # Flag if the coords contains a value of 0
    zero = False
    for b in bcoords:
        if 0 in b:
            zero = True
    
    # If a 0 is present, translate the polygon by adding
    # 1 to x and y to avoid division by zero
    if zero:
        bcoords = [ (b[0] + 1, b[1] + 1) for b in bcoords ]
        polygon = Polygon(bcoords)

    # Retrieve the convex hull
    hull = polygon.convex_hull
    hcoords = list(hull.boundary.coords)

    # Compute the length of the polygon
    length = polygon.length

    # The value will be the area or the length depending on the user choice
    value = None
    # Storage for the resulting rectangle
    bounding_rectangle = None
    # Loop through the coordinates of the convex hull vertexes
    for i in range(0, len(hcoords) - 1):
        # Get the current and next vertex
        # Avoid the last as it's the same as the first
        vertex1 = hcoords[i]
        vertex2 = hcoords[i + 1]
        # Create the points
        point1, point2 = Point(vertex1), Point(vertex2)
        # Create the segment between both points
        segment = LineString([point1, point2])

        # If the mode is input, make sure the segment is contained
        # within the polygon boundary before continuing
        if mode == 'input':
            if not shapely.contains(boundary, segment):
                continue
        
        # Create the unit vector from the segment
        unit = Vector2D(point1, point2)
        # Create a vector by the length of the polygon
        vector = unit.change_norm(length)
        # Create its opposite vector
        opposite = vector.opposite()

        # Create the first two corner point by
        # translating the point by the vectors
        corner1 = opposite.translate(point1)
        corner2 = vector.translate(point1)

        # Storage for the distance
        d = 0
        # Storage for the two corners
        corner3, corner4 = None, None
        # Loop through all the polygon boundary coords
        for v in bcoords:
            point = Point(v)
            # Translate the point in both direction
            # parallel to the considered side
            p1 = vector.translate(point)
            p2 = opposite.translate(point)

            # Calculate the distance between both sides
            distance = shapely.distance(segment, LineString([p1, p2]))
            # If this distance is above the current one,
            # update it along with the corner points
            if distance > d:
                d = distance
                corner3, corner4 = p1, p2

        # Create lines for the two opposite sides
        side1 = LineString([corner1, corner2])
        side3 = LineString([corner3, corner4])
        
        # Create the orthogonal vector and its opposite
        orthogonal = vector.rotate(- np.pi / 2)
        orthogonal_opposite = orthogonal.opposite()

        # Storage for perpendiculars lines
        perpendiculars = []
        # Loop again through all polygon vertexes
        for v in bcoords:
            point = Point(v)
            # Translate the vertex along both orthogonal vectors
            p1 = orthogonal.translate(point)
            p2 = orthogonal_opposite.translate(point)
            # Create the line between those corners
            orthogonal_segment = LineString([p1, p2])
            # If the intersection is of type Point, it means
            # the line only intersects once the polygon
            if shapely.intersection(orthogonal_segment, hull.boundary).geom_type == 'Point':
                # Add the segment if not already present, which can happen
                # with orthogonal polygons.
                if orthogonal_segment not in perpendiculars:
                    perpendiculars.append(orthogonal_segment)

        # Final rectangle nodes
        nodes = []
        # Append the intersection between side 1 and 3 and both perpendiculars
        # which should only be 2
        nodes.append(shapely.intersection(side1, perpendiculars[0]).coords[0])
        nodes.append(shapely.intersection(side3, perpendiculars[0]).coords[0])
        nodes.append(shapely.intersection(side1, perpendiculars[-1]).coords[0])
        nodes.append(shapely.intersection(side3, perpendiculars[-1]).coords[0])

        # Reorder nodes for them to be clockwise
        # TODO: If issues arise, make a function 
        # to order points clockwise or counter clockwise
        nodes.append(nodes.pop(1))
        nodes.append(nodes[0])

        # If 0 were found in the first polygon
        # Translate the resulting rectangle back using dx = dy = -1
        if zero:
            nodes = [ (n[0] - 1, n[1] - 1) for n in nodes ]
                
        # Create the rectangle
        rectangle = Polygon(nodes)

        # Set the precision to avoid weird results
        rectangle = shapely.set_precision(rectangle, 0.0000001, mode='pointwise')

        # Reverse it if counter clockwise
        if shapely.is_ccw(rectangle.boundary):
            rectangle = rectangle.reverse()

        # Remove the last vertex as its the same as the first
        rcoords = list(rectangle.boundary.coords)[:-1]

        # Find the lower left corner index
        minimum, minindex = None, None
        for i, c in enumerate(rcoords):
            s = c[0] + c[1]
            if minimum is None:
                minimum, minindex = s, i
            else:
                if s < minimum:
                    minimum, minindex = s, i
        
        # Reconstruct the boundary by slicing the coordinates list
        start = rcoords[-(len(rcoords) - minindex):]
        end = rcoords[:minindex]
        ordered = start + end + [start[0]]

        # Replace the rectangle with the clockwise, lower left corner starting rectangle
        rectangle = Polygon(ordered)

        # Calculate the area
        rectangle_area = rectangle.area

        # Check the geometric properties wanted
        if property in ['minimum area', 'maximum area']:
            if value is None:
                value, bounding_rectangle = rectangle_area, rectangle
            else:
                if property == 'minimum area':
                    if rectangle_area < value:
                        value, bounding_rectangle = rectangle_area, rectangle
                elif property == 'maximum area':
                    if rectangle_area > value:
                        value, bounding_rectangle = rectangle_area, rectangle
        else:
            if property in ['minimum length', 'maximum length']:
                # Here, the length is wanted, i.e. the length
                # of the longest side of the rectangle.
                rcoords = list(rectangle.boundary.coords)
                rlength = None
                for vi in range(0, len(rcoords) - 1):
                    l = LineString([rcoords[vi], rcoords[vi + 1]]).length
                    if rlength is None:
                        rlength = l
                    else:
                        if l < rlength:
                            rlength = l

                if value is None:
                    value, bounding_rectangle = rlength, rectangle
                else:
                    if property == 'minimum length':
                        if rlength < value:
                            value, bounding_rectangle = rlength, rectangle
                    elif property == 'maximum length':
                        if rlength > value:
                            value, bounding_rectangle = rlength, rectangle
    
    return bounding_rectangle