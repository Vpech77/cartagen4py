from matplotlib import pyplot as plt
import cartagen4py as c4
import geopandas as gp
from shapely.wkt import loads

buildings = [loads('Polygon ((893851.09999999997671694 2017260.89999999990686774, 893840.5 2017264.60000000009313226, 893844.30000000004656613 2017276.60000000009313226, 893841.90000000002328306 2017277.30000000004656613, 893845.40000000002328306 2017286.80000000004656613, 893858.59999999997671694 2017282, 893851.09999999997671694 2017260.89999999990686774))'),
    loads('Polygon ((893877.5 2017265.39999999990686774, 893863.5 2017270.10000000009313226, 893866.69999999995343387 2017278.80000000004656613, 893881.09999999997671694 2017273.30000000004656613, 893877.5 2017265.39999999990686774))'),
    loads('Polygon ((893863.30000000004656613 2017256.69999999995343387, 893873 2017256.60000000009313226, 893873.40000000002328306 2017245.69999999995343387, 893862.30000000004656613 2017246.30000000004656613, 893863.30000000004656613 2017256.69999999995343387))'),
    loads('Polygon ((893841.5 2017211.69999999995343387, 893846 2017223.10000000009313226, 893854.69999999995343387 2017219.80000000004656613, 893854.09999999997671694 2017218.39999999990686774, 893859.80000000004656613 2017216.10000000009313226, 893855.40000000002328306 2017205.60000000009313226, 893841.5 2017211.69999999995343387))'),
    loads('Polygon ((893865.30000000004656613 2017237.19999999995343387, 893865.30000000004656613 2017228.60000000009313226, 893855.09999999997671694 2017228.5, 893855 2017236.80000000004656613, 893865.30000000004656613 2017237.19999999995343387))')]
roads = [loads('LineString (893764.80000000004656613 2017240.19999999995343387, 893786.80000000004656613 2017227.60000000009313226, 893815 2017212.5, 893835 2017199.89999999990686774, 893846.30000000004656613 2017193.5, 893855.59999999997671694 2017189.89999999990686774)'),
    loads('LineString (893891.80000000004656613 2017277, 893884.40000000002328306 2017258.60000000009313226, 893866.80000000004656613 2017213.89999999990686774, 893860.90000000002328306 2017199.10000000009313226, 893855.59999999997671694 2017189.89999999990686774)'),
    loads('LineString (893759 2017255.39999999990686774, 893763.30000000004656613 2017265.69999999995343387, 893768 2017275.39999999990686774, 893770.80000000004656613 2017279.5, 893781.30000000004656613 2017287.19999999995343387, 893795.69999999995343387 2017292.80000000004656613, 893814.59999999997671694 2017296.89999999990686774, 893824.30000000004656613 2017297.10000000009313226, 893837.19999999995343387 2017295.5, 893852.09999999997671694 2017292.39999999990686774, 893863.90000000002328306 2017288.89999999990686774, 893891.80000000004656613 2017277)'),
    loads('LineString (893759 2017255.39999999990686774, 893761.5 2017253.80000000004656613, 893764.90000000002328306 2017251.30000000004656613, 893766 2017249.19999999995343387, 893766.80000000004656613 2017247, 893766.59999999997671694 2017244.30000000004656613, 893764.80000000004656613 2017240.19999999995343387)')]
    
# buffer the roads to simulate the cartographic symbols
symbolized_roads = []
for road in roads:
    symbolized_roads.append(road.buffer(10.0))
p1 = gp.GeoSeries(buildings)
p3 = gp.GeoSeries(symbolized_roads)
envgdf = gp.GeoDataFrame(geometry=p1)
roadgdf = gp.GeoDataFrame(geometry=p3)
riversgdf = gp.GeoDataFrame(geometry=gp.GeoSeries([]))
displacement = c4.RandomDisplacement(3.5, network_partitioning=False)
displaced = displacement.displace(envgdf,roadgdf,riversgdf)

p2 = displaced.geometry
base = p1.plot()
p2.plot(ax=base, facecolor='none', edgecolor='red')
p3.plot(ax=base, facecolor='none', edgecolor='black', linewidth=4)
plt.show()