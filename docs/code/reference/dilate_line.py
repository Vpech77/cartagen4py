from matplotlib import pyplot as plt
from matplotlib.path import Path
from matplotlib.patches import PathPatch

import numpy
import geopandas as gpd
import shapely
from shapely.wkt import loads
import cartagen as c4

line = loads('LineString (-187494.54617879918077961 5374508.44924286287277937, -187484.88630315277259797 5374514.6591629208996892, -187475.45642454555490986 5374520.40908890124410391, -187465.10655778154614381 5374524.54903560690581799, -187454.06669989993679337 5374526.84900599904358387, -187441.18686570471618325 5374527.99899119511246681, -187426.92704927429440431 5374528.22898823395371437, -187415.65719435349456035 5374527.07900303788483143, -187401.39737792307278141 5374526.61900895927101374, -187388.28754668863257393 5374526.15901488158851862, -187376.09770361101254821 5374523.16905337199568748, -187365.51783980781328864 5374517.18913035281002522, -187356.08796120059560053 5374507.98924878425896168, -187351.71801745580160059 5374497.63938202057033777, -187351.02802633820101619 5374487.51951229572296143, -187354.01798784779384732 5374478.54962776694446802, -187357.69794047498726286 5374469.11974915955215693, -187361.37789310220978223 5374456.46991200372576714, -187359.76791382778901607 5374443.1300837304443121, -187354.24798488698434085 5374433.47020808327943087, -187345.50809739739634097 5374427.03029098641127348, -187328.94831057495321147 5374424.04032947681844234, -187311.6985326349386014 5374423.12034131959080696, -187297.43871620451682247 5374426.57029690779745579, -187283.40889681328553706 5374433.47020808327943087, -187278.34896195089095272 5374445.66005116142332554, -187279.498947146901628 5374459.45987351331859827, -187283.63889385250513442 5374468.42975804209709167, -187292.83877542050322518 5374481.07959519792348146, -187305.25861553731374443 5374492.80944419745355844, -187313.07851487013977021 5374502.69931688252836466, -187319.51843196773552336 5374513.04918364714831114, -187322.50839347735745832 5374528.4589852737262845, -187321.81840235975687392 5374541.33881946839392185, -187316.9884645365527831 5374554.21865366399288177, -187308.93856816453626379 5374563.87852931022644043, -187298.81869843971799128 5374575.37838126998394728, -187280.41893530369270593 5374585.72824803460389376, -187259.71920177567517385 5374590.55818585772067308)')
line = c4.gaussian_smoothing(line, sigma=10, sample=10)

fig = plt.figure(1, (12, 4))

#############################################################

sub1 = fig.add_subplot(121)
sub1.set_title("a) offset=28, cap_style='round'", pad=10, family='sans-serif')
sub1.axes.get_xaxis().set_visible(False)
sub1.axes.get_yaxis().set_visible(False)

left, right = c4.dilate_line(line, 28, cap_style='round')

path1 = Path(numpy.asarray(line.coords)[:, :2])
sub1.add_patch(PathPatch(path1, facecolor="none", edgecolor='gray', linewidth=1))

for l in left:
    path2 = Path(numpy.asarray(l.coords)[:, :2])
    sub1.add_patch(PathPatch(path2, facecolor="none", edgecolor='blue', linewidth=1))

for r in right:
    path2 = Path(numpy.asarray(r.coords)[:, :2])
    sub1.add_patch(PathPatch(path2, facecolor="none", edgecolor='red', linewidth=1))

sub1.autoscale_view()

#############################################################

sub2 = fig.add_subplot(122)
sub2.set_title("a) offset=50, cap_style='flat'", pad=10, family='sans-serif')
sub2.axes.get_xaxis().set_visible(False)
sub2.axes.get_yaxis().set_visible(False)

left, right = c4.dilate_line(line, 50, cap_style='flat')

path1 = Path(numpy.asarray(line.coords)[:, :2])
sub2.add_patch(PathPatch(path1, facecolor="none", edgecolor='gray', linewidth=1))

for l in left:
    path2 = Path(numpy.asarray(l.coords)[:, :2])
    sub2.add_patch(PathPatch(path2, facecolor="none", edgecolor='blue', linewidth=1))

for r in right:
    path2 = Path(numpy.asarray(r.coords)[:, :2])
    sub2.add_patch(PathPatch(path2, facecolor="none", edgecolor='red', linewidth=1))

sub2.autoscale_view()

plt.show()