from matplotlib import pyplot as plt
from matplotlib.path import Path
from matplotlib.patches import PathPatch

import numpy
import geopandas as gpd
from shapely.wkt import loads
import cartagen4py as c4

network = [
    loads('LINESTRING (-186131.08878997288 5375717.304421046, -186139.69426741 5375718.737198636, -186147.9412263793 5375716.327910789)'), 
    loads('LINESTRING (-186076.24506305897 5375597.570451453, -186101.85450734163 5375639.258803574, -186107.61209670882 5375650.927472962, -186123.688558325 5375681.864141386)'), 
    loads('LINESTRING (-186145.5574866182 5375677.285979828, -186148.9338298137 5375675.348704298, -186152.7430838316 5375672.689413757, -186157.27106502268 5375669.311396043, -186162.74393370075 5375665.391439133)'), 
    loads('LINESTRING (-186199.4603500886 5375619.072366634, -186216.70980224523 5375611.885094902)'), 
    loads('LINESTRING (-186199.4603500886 5375619.072366634, -186203.62896769322 5375601.535423608)'), 
    loads('LINESTRING (-186157.44110805442 5375687.909904248, -186152.4029940673 5375681.579872394, -186145.5574866182 5375677.285979828)'), 
    loads('LINESTRING (-186145.5574866182 5375677.285979828, -186137.7820257827 5375675.943079686, -186130.17269279592 5375677.487656809, -186123.688558325 5375681.864141386, -186119.2649649174 5375688.604470463, -186117.6606976433 5375696.561023481, -186119.10232296094 5375704.892929517)'), 
    loads('LINESTRING (-186172.90647355863 5375717.778369768, -186168.69882707632 5375712.722517302, -186165.5364275143 5375708.266408829, -186162.73339153887 5375702.3009732915, -186160.505337302 5375696.4792831885, -186157.44110805442 5375687.909904248)'), 
    loads('LINESTRING (-186119.10232296094 5375704.892929517, -186119.48398389228 5375714.249812542, -186118.8910339744 5375723.359679461, -186117.60689883507 5375731.467563318)'), 
    loads('LINESTRING (-186147.9412263793 5375716.327910789, -186154.35417382178 5375710.713893424, -186158.02940461325 5375702.913229728, -186158.4742564866 5375693.920182807, -186157.44110805442 5375687.909904248)'), 
    loads('LINESTRING (-186119.10232296094 5375704.892929517, -186123.800587587 5375712.484311891, -186131.08878997288 5375717.304421046)'), 
    loads('LINESTRING (-186147.9412263793 5375716.327910789, -186154.68364719918 5375714.878698822, -186160.64908273664 5375714.66308067, -186166.03953653554 5375715.525553278, -186172.90647355863 5375717.778369768)'), 
    loads('LINESTRING (-186117.60689883507 5375731.467563318, -186122.5026380197 5375724.779165634, -186127.2821737214 5375720.251184442, -186131.08878997288 5375717.304421046)'), 
    loads('LINESTRING (-186076.24506305897 5375597.570451453, -186081.18797129163 5375592.739586186, -186083.30755179765 5375586.554745696, -186082.52949055893 5375580.122617605, -186078.77165627622 5375574.412529207, -186073.2384345493 5375571.284668306, -186066.895700798 5375570.821461122, -186060.58028020186 5375573.250538903)'), 
    loads('LINESTRING (-186060.58028020186 5375573.250538903, -186056.06360513385 5375578.332553483, -186054.1199630994 5375585.196309146, -186055.78174424637 5375592.680206469, -186059.60607542796 5375597.146276799)'), 
    loads('LINESTRING (-186059.60607542796 5375597.146276799, -186065.80800337132 5375599.960215491, -186070.31676993455 5375599.563940341, -186076.24506305897 5375597.570451453)'), 
    loads('LINESTRING (-186049.6377624998 5375622.2466825, -186051.16299889752 5375615.269081527, -186054.05689636574 5375608.213027304, -186059.60607542796 5375597.146276799)'), 
    loads('LINESTRING (-186162.74393370075 5375665.391439133, -186175.59860793877 5375648.3964353, -186187.6732244483 5375634.309382706, -186199.4603500886 5375619.072366634)'), 
    loads('LINESTRING (-186117.60689883507 5375731.467563318, -186112.20687126362 5375740.968495208, -186107.6070173552 5375747.293294332, -186101.56970910044 5375751.893148241, -186094.23869193395 5375755.199293237, -186085.47022042103 5375757.930456495, -186075.98302173498 5375758.649183668)'), 
    loads('LINESTRING (-186060.58028020186 5375573.250538903, -186053.9899702355 5375564.305356039, -186045.33829188807 5375550.568682942)'), 
    loads('LINESTRING (-186216.70980224523 5375611.885094902, -186203.62896769322 5375601.535423608)'), 
    loads('LINESTRING (-186203.62896769322 5375601.535423608, -186186.52326097136 5375588.742079927, -186170.9987540305 5375577.242445155, -186156.0492288282 5375565.167828646, -186141.67468536444 5375550.218303444, -186131.8999958091 5375533.543833026, -186122.7002879923 5375515.719399131, -186108.9007262671 5375499.044928713, -186088.2013836793 5375489.270239158, -186067.5020410915 5375487.545293941, -186049.67760719644 5375489.8452208955)'), 
    loads('LINESTRING (-186216.70980224523 5375611.885094902, -186233.67176353245 5375625.253420324, -186250.92121568896 5375640.490436396, -186264.43328654487 5375655.727452467, -186273.6329943617 5375675.564322447, -186277.9453574008 5375696.551155904, -186277.37037566226 5375718.400461969, -186273.05801262314 5375732.775005433, -186270.22802437894 5375739.881420356)'), 
    loads('LINESTRING (-186157.44110805442 5375687.909904248, -186157.7741740439 5375683.685939507, -186158.20541034781 5375680.37979451, -186158.924137521 5375676.35492234, -186159.93035556347 5375672.258177454, -186161.36780990983 5375667.730196262, -186162.74393370075 5375665.391439133)'), 
    loads('LINESTRING (-186172.90647355863 5375717.778369768, -186182.47143653256 5375724.572531567, -186190.88054445887 5375729.962985367, -186201.44583390476 5375735.569057317, -186213.08921411043 5375740.959511116, -186227.32001213956 5375745.918728611, -186240.90395571283 5375750.23109165, -186255.5659900459 5375755.1903091455)'), 
    loads('LINESTRING (-186255.5659900459 5375755.1903091455, -186270.22802437894 5375739.881420356)'), 
    loads('LINESTRING (-186270.22802437894 5375739.881420356, -186271.5217332907 5375760.365144792)'), 
    loads('LINESTRING (-186255.5659900459 5375755.1903091455, -186271.5217332907 5375760.365144792)'), 
    loads('LINESTRING (-186271.5217332907 5375760.365144792, -186280.57769567287 5375764.246271527, -186291.3586032707 5375771.14605239, -186298.47400228528 5375780.202014772)'), 
    loads('LINESTRING (-186045.33829188807 5375550.568682942, -186041.02592884892 5375527.281922529, -186041.02592884892 5375511.757415589, -186049.67760719644 5375489.8452208955)'), 
    loads('LINESTRING (-186045.33829188807 5375550.568682942, -186029.81378494718 5375538.062830128, -186015.58298691802 5375531.594285569, -185994.45240802626 5375527.281922529, -185974.61553804626 5375526.419449922)'), 
    loads('LINESTRING (-186049.67760719644 5375489.8452208955, -186030.676257555 5375494.939199736, -186015.58298691802 5375500.545271687, -185996.60858954585 5375508.738761461, -185983.6984526974 5375516.743585353, -185974.61553804626 5375526.419449922)'), 
    loads('LINESTRING (-185974.61553804626 5375526.419449922, -185959.09103110537 5375544.100138382, -185947.8788872036 5375554.018573373, -185925.45459940014 5375566.093189882, -185903.89278420445 5375573.4242070485)'), 
]

fig = plt.figure(1, (8, 12))

sub1 = fig.add_subplot(211)
sub1.set_title('a) Providing branching crossroads', pad=10, family='sans-serif')
sub1.axes.get_xaxis().set_visible(False)
sub1.axes.get_yaxis().set_visible(False)

sub2 = fig.add_subplot(212)
sub2.set_title('b) Without providing branching crossroads', pad=10, family='sans-serif')
sub2.axes.get_xaxis().set_visible(False)
sub2.axes.get_yaxis().set_visible(False)

original = []
for n in network:
    original.append({"geometry": n})
original = gpd.GeoDataFrame(original)
selection = c4.detect_roundabouts(original)
selection2 = c4.detect_branching_crossroads(original, selection)
generalized1 = c4.collapse_roundabouts(original, selection)
generalized2 = c4.collapse_roundabouts(original, selection, selection2)

for o in original.geometry:
    path1 = Path(numpy.asarray(o.coords)[:, :2])
    sub1.add_patch(PathPatch(path1, facecolor="none", edgecolor='gray', linewidth=0.5))
    sub2.add_patch(PathPatch(path1, facecolor="none", edgecolor='gray', linewidth=0.5))

for g in generalized1.geometry:
    path1 = Path(numpy.asarray(g.coords)[:, :2])
    sub2.add_patch(PathPatch(path1, facecolor="none", edgecolor='red', linewidth=1.5))

for g in generalized2.geometry:
    path1 = Path(numpy.asarray(g.coords)[:, :2])
    sub1.add_patch(PathPatch(path1, facecolor="none", edgecolor='red', linewidth=1.5))

sub1.autoscale_view()
sub2.autoscale_view()

plt.show()