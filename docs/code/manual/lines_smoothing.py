from matplotlib import pyplot as plt
from matplotlib.path import Path
from matplotlib.patches import PathPatch

import numpy
import geopandas as gpd
from shapely.wkt import loads
import cartagen as c4

line = loads('LineString (-176283.00173896295018494 5373523.20335822738707066, -176284.12561622171779163 5373530.73189105931669474, -176283.79858441557735205 5373542.38433008268475533, -176283.49681569819222204 5373553.13660864252597094, -176280.51933755574282259 5373577.74947946425527334, -176276.23351891804486513 5373590.44030951056629419, -176271.00609994871774688 5373605.91930489707738161, -176260.12988276744727045 5373622.43225789815187454, -176241.18261740999878384 5373634.99746511317789555, -176220.59483572118915617 5373640.61643818207085133, -176199.08239050811971538 5373642.14700586069375277, -176193.33157180700800382 5373641.34373851586133242, -176173.97623034240677953 5373638.64017973560839891, -176162.70156723572290502 5373634.01987256668508053, -176148.60888729523867369 5373628.24473069980740547, -176147.94445495080435649 5373627.87718675378710032, -176118.40851719881175086 5373611.53872985951602459, -176116.77005434015882201 5373610.63237410224974155, -176097.47451161858043633 5373601.75439327582716942, -176084.54216705964063294 5373595.80412461515516043, -176075.80798485179548152 5373594.26099958084523678, -176071.61450497503392398 5373593.52010690420866013, -176061.18692039689631201 5373591.64263125229626894, -176052.06513008938054554 5373590.93169923219829798, -176034.6363259383069817 5373589.32423806749284267, -176009.53038148829364218 5373585.81696144863963127, -175991.87063821422634646 5373580.21871133055537939, -175971.49583528959192336 5373570.49836398009210825, -175962.85201082288403995 5373563.25366575829684734, -175957.32518327035359107 5373558.62142644450068474, -175953.92211818875512108 5373554.46091531403362751, -175945.03621062668389641 5373543.5971882427111268, -175935.48018434963887557 5373525.58516346476972103, -175933.45406480284873396 5373521.76615201774984598, -175928.41186328750336543 5373500.3786083310842514, -175928.34853853366803378 5373500.1100028995424509, -175927.76874646675423719 5373486.07514364365488291, -175927.31860892896656878 5373475.17877863254398108, -175928.02892485680058599 5373458.7873552106320858, -175928.96818767991499044 5373437.11265027895569801, -175928.59376375653664581 5373409.24388919863849878, -175924.39241319749271497 5373386.56882080715149641, -175918.26169635044061579 5373366.21538938581943512, -175908.05724673558142968 5373346.78976117912679911, -175893.47124094472383149 5373330.10477467533200979, -175891.68085428982158192 5373328.73503715265542269, -175877.20448933073203079 5373317.65985492616891861, -175864.84248095549992286 5373311.7392307547852397, -175852.01711695158155635 5373305.59666572231799364, -175829.71370610687881708 5373298.19783743284642696, -175806.93968476584996097 5373294.55427216459065676)')

plt.rcParams.update({
    'font.size': 12,
    'axes.labelpad': 10
})

fig = plt.figure(1, (12, 12))

sub1 = fig.add_subplot(331)
sub1.set_aspect('equal')
sub1.set_xticks([])
sub1.set_yticks([])
sub1.set_ylabel('sample=5')
sub1.set_xlabel('sigma=10')
sub1.xaxis.set_label_position('top') 
path1 = Path(numpy.asarray(line.coords)[:, :2])
path2 = Path(numpy.asarray(c4.gaussian_smoothing(line, 10, 5).coords)[:, :2])
sub1.add_patch(PathPatch(path1, facecolor="none", edgecolor='gray', linewidth=1))
sub1.add_patch(PathPatch(path2, facecolor="none", edgecolor='red', linewidth=1))
sub1.autoscale_view()

sub2 = fig.add_subplot(332)
sub2.set_aspect('equal')
sub2.axes.get_yaxis().set_visible(False)
sub2.set_xticks([])
sub2.set_xlabel('sigma=20')
sub2.xaxis.set_label_position('top') 
path1 = Path(numpy.asarray(line.coords)[:, :2])
path2 = Path(numpy.asarray(c4.gaussian_smoothing(line, 20, 5).coords)[:, :2])
sub2.add_patch(PathPatch(path1, facecolor="none", edgecolor='gray', linewidth=1))
sub2.add_patch(PathPatch(path2, facecolor="none", edgecolor='red', linewidth=1))
sub2.autoscale_view()

sub3 = fig.add_subplot(333)
sub3.set_aspect('equal')
sub3.axes.get_yaxis().set_visible(False)
sub3.set_xticks([])
sub3.set_xlabel('sigma=30')
sub3.xaxis.set_label_position('top') 
path1 = Path(numpy.asarray(line.coords)[:, :2])
path2 = Path(numpy.asarray(c4.gaussian_smoothing(line, 30, 5).coords)[:, :2])
sub3.add_patch(PathPatch(path1, facecolor="none", edgecolor='gray', linewidth=1))
sub3.add_patch(PathPatch(path2, facecolor="none", edgecolor='red', linewidth=1))
sub3.autoscale_view()

#######################################################

sub4 = fig.add_subplot(334)
sub4.set_aspect('equal')
sub4.axes.get_xaxis().set_visible(False)
sub4.set_yticks([])
sub4.set_ylabel('sample=30')
path1 = Path(numpy.asarray(line.coords)[:, :2])
path2 = Path(numpy.asarray(c4.gaussian_smoothing(line, 10, 30).coords)[:, :2])
sub4.add_patch(PathPatch(path1, facecolor="none", edgecolor='gray', linewidth=1))
sub4.add_patch(PathPatch(path2, facecolor="none", edgecolor='red', linewidth=1))
sub4.autoscale_view()

sub5 = fig.add_subplot(335)
sub5.set_aspect('equal')
sub5.axes.get_xaxis().set_visible(False)
sub5.axes.get_yaxis().set_visible(False)
path1 = Path(numpy.asarray(line.coords)[:, :2])
path2 = Path(numpy.asarray(c4.gaussian_smoothing(line, 20, 30).coords)[:, :2])
sub5.add_patch(PathPatch(path1, facecolor="none", edgecolor='gray', linewidth=1))
sub5.add_patch(PathPatch(path2, facecolor="none", edgecolor='red', linewidth=1))
sub5.autoscale_view()

sub6 = fig.add_subplot(336)
sub6.set_aspect('equal')
sub6.axes.get_xaxis().set_visible(False)
sub6.axes.get_yaxis().set_visible(False)
path1 = Path(numpy.asarray(line.coords)[:, :2])
path2 = Path(numpy.asarray(c4.gaussian_smoothing(line, 30, 30).coords)[:, :2])
sub6.add_patch(PathPatch(path1, facecolor="none", edgecolor='gray', linewidth=1))
sub6.add_patch(PathPatch(path2, facecolor="none", edgecolor='red', linewidth=1))
sub6.autoscale_view()

#######################################################

sub7 = fig.add_subplot(337)
sub7.set_aspect('equal')
sub7.axes.get_xaxis().set_visible(False)
sub7.set_yticks([])
sub7.set_ylabel('sample=60')
path1 = Path(numpy.asarray(line.coords)[:, :2])
path2 = Path(numpy.asarray(c4.gaussian_smoothing(line, 10, 60).coords)[:, :2])
sub7.add_patch(PathPatch(path1, facecolor="none", edgecolor='gray', linewidth=1))
sub7.add_patch(PathPatch(path2, facecolor="none", edgecolor='red', linewidth=1))
sub7.autoscale_view()

sub8 = fig.add_subplot(338)
sub8.set_aspect('equal')
sub8.axes.get_xaxis().set_visible(False)
sub8.axes.get_yaxis().set_visible(False)
path1 = Path(numpy.asarray(line.coords)[:, :2])
path2 = Path(numpy.asarray(c4.gaussian_smoothing(line, 20, 60).coords)[:, :2])
sub8.add_patch(PathPatch(path1, facecolor="none", edgecolor='gray', linewidth=1))
sub8.add_patch(PathPatch(path2, facecolor="none", edgecolor='red', linewidth=1))
sub8.autoscale_view()

sub9 = fig.add_subplot(339)
sub9.set_aspect('equal')
sub9.axes.get_xaxis().set_visible(False)
sub9.axes.get_yaxis().set_visible(False)
path1 = Path(numpy.asarray(line.coords)[:, :2])
path2 = Path(numpy.asarray(c4.gaussian_smoothing(line, 30, 60).coords)[:, :2])
sub9.add_patch(PathPatch(path1, facecolor="none", edgecolor='gray', linewidth=1))
sub9.add_patch(PathPatch(path2, facecolor="none", edgecolor='red', linewidth=1))
sub9.autoscale_view()

plt.subplots_adjust(wspace=0, hspace=0)
plt.show()