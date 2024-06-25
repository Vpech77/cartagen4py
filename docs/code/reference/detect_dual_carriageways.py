from matplotlib import pyplot as plt
from matplotlib.path import Path
from matplotlib.patches import PathPatch

import numpy
import geopandas as gpd
from shapely.wkt import loads
import cartagen4py as c4

network = [
    loads('LINESTRING (-187379.7052932845 5374428.746871513, -187384.08119944856 5374428.580059872, -187395.58884462202 5374426.687937666, -187407.30763075722 5374423.649171588, -187419.42846878245 5374419.49961636, -187431.6122163518 5374414.472159996, -187443.89406885882 5374408.3756938195, -187456.19617396838 5374401.0967372805, -187469.0912565376 5374392.742851763, -187481.97888259694 5374383.893287892, -187484.1119585546 5374382.3726302525, -187494.7108123178 5374374.816782305, -187496.1157653071 5374373.833736992, -187507.52061638376 5374365.853780239, -187520.67705672968 5374357.153619456, -187529.20526917523 5374351.297625966, -187533.45170136436 5374348.38177081, -187543.00560431276 5374341.948961359, -187545.96506818582 5374339.956306423, -187558.8730574851 5374329.924363229)'), 
    loads('LINESTRING (-187123.61336767394 5374315.133543446, -187143.92113725655 5374335.255468211, -187154.07958107255 5374344.569805615, -187159.2353732912 5374349.297173025, -187173.21854875702 5374359.854974939, -187187.4592860192 5374369.211592066, -187206.99723209813 5374380.882718746, -187223.79701002594 5374388.583672038, -187239.0471916236 5374394.700805844, -187263.46179689188 5374402.130534774, -187304.81182638556 5374413.397191998)'), 
    loads('LINESTRING (-187191.95147573296 5374433.135476228, -187195.94997817744 5374427.7036706805, -187199.9231502181 5374423.271055238, -187207.4968835907 5374417.905641764, -187212.15512515884 5374415.56440161, -187218.2250194773 5374414.275473451, -187221.2277704347 5374413.781153249, -187240.4236812368 5374412.069507167, -187250.3192960117 5374412.909094423, -187273.2923432365 5374419.719614804, -187286.73321864102 5374421.058711495, -187291.50859190803 5374420.814151809, -187303.3470777264 5374418.172518691)'), 
    loads('LINESTRING (-187558.8730574851 5374329.924363229, -187547.1435564214 5374337.310718511, -187541.15111697314 5374341.084315008, -187535.41406736488 5374344.697092154, -187525.9782602212 5374350.502772987, -187523.71978400508 5374351.892374844, -187512.06070544908 5374358.896566426, -187500.17553826107 5374366.056030922, -187498.4641925845 5374367.065546462, -187488.09947596712 5374373.179659925, -187482.47679774405 5374376.579853691, -187475.87518289522 5374380.572045687, -187463.72875904053 5374388.077933052, -187451.39144102484 5374395.5479867, -187439.1671843964 5374402.940432355, -187426.77974911442 5374409.610234537, -187413.8750330208 5374414.798877987, -187400.75698456052 5374418.464587328, -187387.46826456767 5374420.911952872, -187380.05279665004 5374421.49653433, -187373.93100898678 5374422.027492316, -187360.18788059184 5374422.11579555, -187346.35192348668 5374421.099231198, -187332.27489488473 5374419.246537582, -187318.260747856 5374416.515933807, -187304.81182638556 5374413.397191998)'), 
    loads('LINESTRING (-187379.7052932845 5374428.746871513, -187379.58696691296 5374430.998415794, -187380.8071906909 5374436.170536188, -187383.21552402654 5374441.8623536555, -187386.0131479503 5374448.121570265, -187389.42615820095 5374454.792926513, -187393.08021899173 5374462.3004175965)'), 
    loads('LINESTRING (-187570.1002422336 5374322.048238735, -187558.8730574851 5374329.924363229)'), 
    loads('LINESTRING (-187303.3470777264 5374418.172518691, -187319.34306739277 5374422.650901604, -187332.42193155273 5374425.593646041, -187340.9231932567 5374426.901532457, -187352.04022779266 5374428.209418873, -187362.11632125126 5374428.804954919, -187373.0107885563 5374429.170277084, -187379.7052932845 5374428.746871513)'), 
    loads('LINESTRING (-186934.47978543397 5374523.476095251, -186923.1216044901 5374531.348648069, -186900.80885816086 5374547.5576335285)'), 
    loads('LINESTRING (-186934.47978543397 5374523.476095251, -187021.33066272922 5374491.444909563, -187037.60051937753 5374486.237895005, -187055.57055722736 5374480.121999631, -187070.54927200545 5374474.158214275, -187084.3230776023 5374467.935864848, -187098.06573858764 5374462.146907829, -187110.97601067275 5374456.99657633, -187123.32399246935 5374452.982886941, -187134.74923232477 5374451.474370285, -187145.1151796989 5374451.938792079)'), 
    loads('LINESTRING (-187124.63623897918 5374423.152178986, -187117.55659753364 5374437.160453627, -187108.30716385692 5374445.485285712, -187107.64672744926 5374445.912934637, -187096.7132245088 5374452.992653008, -187083.20953005366 5374459.712995313, -187076.6297167139 5374462.316373064, -187067.96375031304 5374465.745162627, -187051.41063890886 5374471.119592081, -187033.9988985087 5374476.607473985, -187017.40366791282 5374482.24099675, -187000.5894076079 5374488.816763296, -186984.1134957131 5374496.15669443, -186967.51004319917 5374504.663739039, -186951.21080430038 5374513.801899376, -186934.47978543397 5374523.476095251)'), 
    loads('LINESTRING (-187154.54935024306 5374453.20908079, -187162.4402659079 5374453.456658069, -187169.9897880219 5374452.373675642, -187177.3625807315 5374449.492558526, -187183.85680910293 5374444.85128398, -187189.10901157837 5374439.2519550305, -187191.95147573296 5374433.135476228)'), 
    loads('LINESTRING (-187145.1151796989 5374451.938792079, -187154.54935024306 5374453.20908079)'), 
    loads('LINESTRING (-187124.63623897918 5374423.152178986, -187125.77184080798 5374429.242338269, -187128.1062975917 5374434.458215655, -187130.80422641058 5374438.871986352, -187133.6326836003 5374442.685117897, -187137.8989605587 5374446.555359121, -187145.1151796989 5374451.938792079)'), 
    loads('LINESTRING (-187130.5431556655 5374402.354287305, -187127.20664430503 5374409.873529406, -187124.93544884678 5374416.552704696, -187124.63623897918 5374423.152178986)'), 
    loads('LINESTRING (-187130.5431556655 5374402.354287305, -187136.05692406558 5374391.980542923, -187138.88162738923 5374383.832764538, -187140.25808032043 5374371.541536214, -187138.45978948008 5374362.405816223, -187135.2036305312 5374352.291772345, -187129.52089730185 5374339.492146638, -187123.83816407155 5374326.692520931, -187122.9553930154 5374323.413091205, -187122.77657975443 5374320.495938424, -187123.61336767394 5374315.133543446)'), 
    loads('LINESTRING (-187123.61336767394 5374315.133543446, -187075.76552410703 5374265.536047943)'), 
    loads('LINESTRING (-187303.3470777264 5374418.172518691, -187304.81182638556 5374413.397191998)'), 
]

fig = plt.figure(1, (12, 6))

sub1 = fig.add_subplot(111)
sub1.axes.get_xaxis().set_visible(False)
sub1.axes.get_yaxis().set_visible(False)

original = []
for n in network:
    original.append({"geometry": n})
original = gpd.GeoDataFrame(original)
selection = c4.detect_dual_carriageways(original)

for d in selection.geometry:
    poly1 = Path.make_compound_path(Path(numpy.asarray(d.exterior.coords)[:, :2]),*[Path(numpy.asarray(ring.coords)[:, :2]) for ring in d.interiors])
    sub1.add_patch(PathPatch(poly1, facecolor="red", edgecolor='none'))

for o in original.geometry:
    path1 = Path(numpy.asarray(o.coords)[:, :2])
    sub1.add_patch(PathPatch(path1, facecolor="none", edgecolor='gray', linewidth=1))

sub1.autoscale_view()
plt.show()