from matplotlib import pyplot as plt
from matplotlib.path import Path
from matplotlib.patches import PathPatch

import numpy
import geopandas as gpd
from shapely.wkt import loads
import cartagen as c4

network = [
    loads('LINESTRING (-186277.18038877263 5374855.945724207, -186247.52070756117 5374854.018672603)'), 
    loads('LINESTRING (-186369.42960214068 5374552.002297648, -186357.7845827461 5374488.374544599, -186346.20467074815 5374418.626703974, -186342.01327958424 5374393.381079372, -186340.01812332866 5374381.36381018, -186338.13600882003 5374372.227390038, -186331.0904399329 5374351.793284621, -186328.4913839808 5374344.688609773, -186325.18079649034 5374338.067434792, -186320.76667983638 5374333.1015535565)'), 
    loads('LINESTRING (-186375.26059161263 5374587.678180919, -186390.34278058523 5374668.632768409, -186396.5690025884 5374704.240913349, -186402.34244216792 5374737.259434619, -186404.139508701 5374747.536900533, -186407.46904152888 5374766.578544514, -186415.56806579875 5374827.056471489, -186417.57191755032 5374842.01978865)'), 
    loads('LINESTRING (-186417.57191755032 5374842.01978865, -186421.33704555765 5374862.776533827, -186424.70692134585 5374886.314337533, -186425.18126901117 5374897.323351258, -186424.6292291146 5374914.597342971, -186420.08858565142 5374934.301730055, -186407.96727597105 5374998.159261297)'), 
    loads('LINESTRING (-186369.42960214068 5374552.002297648, -186372.57711212398 5374569.068569971, -186375.19946230014 5374586.578083885, -186375.26059161263 5374587.678180919)'), 
    loads('LINESTRING (-186247.52070756117 5374854.018672603, -186238.7079231619 5374828.992172079, -186233.5424082976 5374807.762028433, -186224.933588626 5374774.033854198, -186219.93808807925 5374765.760901696, -186213.03233371623 5374760.215727953, -186205.67778415943 5374756.488909287)'), 
    loads('LINESTRING (-186143.22641123782 5374772.949075376, -186169.08585506197 5374768.329853409, -186196.87845694253 5374761.395331409, -186205.67778415943 5374756.488909287)'), 
    loads('LINESTRING (-186152.02589610076 5374602.23750931, -186141.75938214382 5374575.7756357575)'), 
    loads('LINESTRING (-186162.4074970587 5374633.245043574, -186154.27265895667 5374608.04324214, -186152.02589610076 5374602.23750931)'), 
    loads('LINESTRING (-186320.76667983638 5374333.1015535565, -186327.6177567264 5374326.2964570485, -186332.21579490765 5374320.778811229, -186339.57265599762 5374313.789793193, -186344.35461570608 5374310.479205703, -186349.13657541457 5374307.904304322, -186355.389907341 5374306.432932104, -186362.011082322 5374306.432932104, -186366.79304203045 5374306.432932104, -186373.78206006592 5374307.536461268, -186378.19617671988 5374309.0078334855)'), 
    loads('LINESTRING (-185682.62778529 5374592.204150558, -185675.61594262903 5374596.661102103, -185666.4198662666 5374601.810904866, -185652.4418301957 5374610.639138173, -185640.30300939726 5374617.628156209)'), 
    loads('LINESTRING (-185640.30300939726 5374617.628156209, -185629.63556081682 5374623.513645081, -185623.01438583585 5374627.927761735, -185614.5539955824 5374634.181093661, -185566.36655544318 5374664.712067185)'), 
    loads('LINESTRING (-185738.57655801164 5374847.44123737, -185729.8783258728 5374840.986615003, -185720.94367166312 5374834.356538995, -185712.04785987994 5374826.311425938, -185701.40705101765 5374816.6881667795, -185689.24013365206 5374803.022094607, -185683.01122521065 5374789.851841104, -185681.0979032945 5374780.7664177, -185680.39846207245 5374777.445113379, -185681.1277737768 5374765.817226832, -185684.03393322966 5374751.3088685395, -185690.22775359693 5374729.167963803, -185691.52896438545 5374723.3632433275, -185695.06498696192 5374707.588974191, -185696.1773610378 5374702.626644487, -185697.61401556057 5374686.407277805, -185697.11585263797 5374684.12734522, -185694.66616583252 5374672.915902105, -185689.116719348 5374665.44377645, -185687.38724278123 5374663.115097821, -185673.94186776874 5374651.175981949)'), 
    loads('LINESTRING (-185673.94186776874 5374651.175981949, -185666.99839546083 5374644.942881052, -185655.23552830357 5374633.599439825, -185640.30300939726 5374617.628156209)'), 
    loads('LINESTRING (-186014.8697042496 5375050.637309037, -186009.2305795743 5375062.954027809, -186005.11364753652 5375072.978484027, -186001.87358404012 5375091.368692781, -185997.92543817963 5375109.3846915, -185990.42288152035 5375132.70355746, -185988.34496749844 5375141.9147727685, -185986.6724037775 5375149.329097434, -185980.31828074995 5375166.100258851)'), 
    loads('LINESTRING (-186088.7095101916 5374585.777845035, -186092.22217906683 5374604.479106767, -186107.34320497065 5374661.430308324, -186121.18269349806 5374702.728216784, -186122.16523259855 5374705.570027038)'), 
    loads('LINESTRING (-186086.36121124064 5375085.54006311, -186085.55047909054 5375083.635128107, -186075.78386875836 5375060.686995295, -186068.86130111726 5375044.42132931, -186067.57108088772 5375041.389749167, -186064.02877597706 5375033.066527128, -186062.96470550375 5375030.566318508, -186053.2630616578 5375014.279466282, -186046.93546134955 5375006.770422883)'), 
    loads('LINESTRING (-185773.36893719682 5374808.114047185, -185829.09289008973 5374850.0136904195, -185845.08872402742 5374862.0410859855, -185880.12851610171 5374893.2606910365, -185903.7988443052 5374914.350237201, -185945.4994574604 5374951.3350203745, -185951.53369541414 5374956.68683035, -185952.52013753413 5374957.5617124075, -185964.14678880238 5374968.912830442)'), 
    loads('LINESTRING (-186099.77736530837 5374495.498586818, -186095.83951495055 5374526.065271831, -186092.73686492187 5374544.446717763)'), 
    loads('LINESTRING (-186141.75938214382 5374575.7756357575, -186108.50882887281 5374580.946059781, -186088.7095101916 5374585.777845035)'), 
    loads('LINESTRING (-186141.75938214382 5374575.7756357575, -186133.03343116847 5374564.676836152, -186117.65355422942 5374550.087937209, -186107.81708173794 5374543.741183676, -186101.93990708631 5374541.862890002, -186092.73686492187 5374544.446717763)'), 
    loads('LINESTRING (-186122.16523259855 5374705.570027038, -186134.22935486317 5374737.173553913, -186141.27522674965 5374760.091639135, -186143.22641123782 5374772.949075376)'), 
    loads('LINESTRING (-186118.09225373776 5374916.850662042, -186098.8361808333 5374941.378340713, -186061.17601408064 5374988.454866678, -186050.9237725159 5375001.857208145)'), 
    loads('LINESTRING (-186046.93546134955 5375006.770422883, -186040.38216551841 5375014.99984679, -186025.2276366261 5375036.31748856, -186019.85503536265 5375043.87502504)'), 
    loads('LINESTRING (-185997.4143288596 5375011.057221473, -185986.84806166898 5374996.022257992, -185984.72828981996 5374993.005985467, -185969.5452173044 5374974.542617017, -185964.14678880238 5374968.912830442)'), 
    loads('LINESTRING (-186082.15681480517 5374551.935415071, -186088.7095101916 5374585.777845035)'), 
    loads('LINESTRING (-186092.73686492187 5374544.446717763, -186090.57503618937 5374545.119387341, -186082.15681480517 5374551.935415071)'), 
    loads('LINESTRING (-186050.9237725159 5375001.857208145, -186046.93546134955 5375006.770422883)'), 
    loads('LINESTRING (-185997.4143288596 5375011.057221473, -186001.96655811465 5375007.497449043, -186035.2225483172 5374981.491666639)'), 
    loads('LINESTRING (-186050.9237725159 5375001.857208145, -186035.2225483172 5374981.491666639)'), 
    loads('LINESTRING (-186019.85503536265 5375043.87502504, -186010.9356129802 5375030.741715671, -186007.57999626047 5375025.800765793, -186000.09877327894 5375014.950547891, -185997.4143288596 5375011.057221473)'), 
    loads('LINESTRING (-186019.85503536265 5375043.87502504, -186016.30915738954 5375048.6847834, -186014.8697042496 5375050.637309037)'), 
    loads('LINESTRING (-186320.76667983638 5374333.1015535565, -186315.80079860066 5374331.998024393, -186307.7471671895 5374332.409130646, -186301.4366077902 5374332.624307446, -186290.73376821887 5374332.947311736, -186278.62253042602 5374332.6594282845, -186265.6968125282 5374332.555035161, -186252.01772593136 5374333.734195192, -186249.2209428326 5374334.230806492, -186238.40738499287 5374336.1509091975, -186224.88869985958 5374340.217703809, -186211.33228119276 5374346.079755874, -186198.15682007937 5374353.851581198, -186184.77603665626 5374362.876303264, -186171.25820513658 5374371.908679073, -186157.61096265758 5374381.086217141, -186143.43088243308 5374390.569420399, -186128.8320709831 5374399.938094515, -186113.12178387944 5374409.093048142, -186096.83283144468 5374417.728599593, -186080.5209378259 5374425.951599468, -186063.62274581037 5374433.517679995, -186046.43520918116 5374440.824040307, -186044.88021007722 5374441.476842949, -186029.37703045373 5374447.985199762, -186011.57263023444 5374454.084561586, -185993.09072927112 5374460.359713453, -185991.7793803207 5374460.795838434, -185975.14162180695 5374466.329161433, -185967.78334571025 5374468.005261662, -185956.68217363695 5374470.533922759, -185938.5043871634 5374474.860835018, -185920.3418508167 5374479.462733376, -185907.82839725792 5374482.901178788, -185902.06517392295 5374484.484790205, -185889.53711524213 5374488.431092385, -185883.96366612086 5374490.186706373, -185865.59572223996 5374496.041420638, -185846.85484918943 5374502.606636789, -185828.8143291394 5374509.408541642, -185811.23827726135 5374517.150016749, -185794.33967958842 5374524.71565544, -185777.60860368275 5374532.8236562, -185761.76069170434 5374541.98577558, -185745.91274680564 5374551.147875733, -185731.15333010067 5374560.111178121, -185717.87825661688 5374568.577688545, -185706.4833443122 5374576.249413488, -185696.67929118357 5374582.866648467, -185689.13596588757 5374588.116082705, -185682.62778529 5374592.204150558)'), 
    loads('LINESTRING (-186014.8697042496 5375050.637309037, -185997.90465394346 5375029.790479706, -185980.19354598408 5375010.662619738, -185976.40962784505 5375006.576007283, -185949.6842574243 5374980.757150186, -185917.4770671571 5374950.278772295, -185892.93000725942 5374929.028248856, -185877.0632208949 5374918.052093352, -185864.45501656004 5374908.824973288, -185848.38331140505 5374901.584743004, -185828.35269048333 5374892.358695259, -185799.2931085451 5374881.430217046, -185776.1563655511 5374870.722377694, -185755.86675362178 5374859.303585372, -185744.31716987558 5374851.810458642, -185738.57655801164 5374847.44123737)'), 
    loads('LINESTRING (-186053.72275466597 5375096.02346157, -186048.51028323392 5375089.588275334, -186041.63422215686 5375081.423510891, -186035.2896775485 5375073.889867578, -186027.31916696602 5375064.425502985, -186021.1479005874 5375057.590625179, -186014.8697042496 5375050.637309037)'), 
    loads('LINESTRING (-186082.15681480517 5374551.935415071, -186069.22400344643 5374556.65897263, -186042.69443394564 5374556.625371778, -186007.33426275762 5374555.982006231, -185982.70012284326 5374555.428411049, -185982.45488208148 5374555.450959331, -185975.04206324634 5374556.132516184, -185968.6782947284 5374557.867752905, -185963.7080672611 5374562.421781838, -185960.40582649948 5374572.262168154, -185961.70713048778 5374583.6262675375, -185962.0067109558 5374586.242458288, -185969.51733836034 5374615.065683924, -185984.47684505652 5374666.646466879, -186000.0529390673 5374716.951580415, -186008.9412903512 5374743.35315391, -186014.1113700315 5374749.823185402, -186025.7369893366 5374756.208086776, -186072.01644633597 5374767.827883381, -186119.35361023564 5374776.2156177275, -186133.5662336583 5374774.730916575, -186143.22641123782 5374772.949075376)'), 
    loads('LINESTRING (-186035.2225483172 5374981.491666639, -186030.64787228082 5374975.602902654, -186024.16023499332 5374967.251663285, -186018.79043101205 5374960.339350057, -185999.79300669464 5374940.020236587, -185951.97694042482 5374893.309881791, -185923.04395535254 5374866.255822094, -185910.07765911715 5374854.131506785, -185907.55146408622 5374852.100790936, -185883.60485707913 5374832.850929283, -185836.29376065158 5374795.216543429, -185816.65085867298 5374780.5891689425, -185815.41155061836 5374779.856503855, -185808.976609947 5374776.052234973, -185800.86874567912 5374773.608667386, -185791.05585382108 5374772.639820483, -185782.14908057547 5374773.137677766, -185778.05387484145 5374776.125425314, -185774.14183337538 5374782.413547593, -185771.95043614254 5374789.984921076, -185772.14164340036 5374798.186595321, -185772.14956120713 5374798.526222806, -185773.36893719682 5374808.114047185)'), 
    loads('LINESTRING (-186417.57191755032 5374842.01978865, -186479.7443020202 5374837.850138534, -186538.30096639012 5374835.3998450115)'), 
    loads('LINESTRING (-186417.57191755032 5374842.01978865, -186404.72187008188 5374843.290755196, -186395.87779619536 5374844.773436254, -186351.60955930533 5374852.194728389, -186301.6707179939 5374856.368660983, -186277.18038877263 5374855.945724207)'), 
    loads('LINESTRING (-186320.76667983638 5374333.1015535565, -186318.00785692764 5374336.22821952, -186315.6168770734 5374343.033316028, -186313.93184490307 5374349.71885021, -186312.4032003245 5374356.839127968, -186308.58340485767 5374364.777296811, -186304.04793996498 5374372.203771105, -186299.2155065839 5374379.233056371, -186295.7710193141 5374383.0077317115, -186293.64448329975 5374385.338115689, -186287.48717048825 5374390.7862972235, -186280.85003132155 5374395.01989481, -186274.03002818787 5374398.436100221, -186268.13861012817 5374401.248598397, -186262.37657020398 5374403.9159176415, -186256.20346324646 5374406.60623303, -186249.48990665015 5374409.464719465, -186242.38819867658 5374412.758728797, -186235.4235067471 5374416.045067538, -186228.99925650732 5374419.16322848, -186222.9631501497 5374421.845859093, -186217.88619058527 5374424.474825888, -186213.3420371463 5374426.798108071, -186209.15453573936 5374428.59699826, -186208.91198758406 5374428.701193375, -186204.77125605455 5374430.863965389)'), 
    loads('LINESTRING (-186369.42960214068 5374552.002297648, -186356.79391392195 5374557.123478294, -186356.29122059012 5374557.361646873, -186342.59797569597 5374563.849287759, -186318.96416644522 5374578.827815624, -186294.97892367892 5374591.678286321, -186289.06536919516 5374594.846553067, -186279.79624294277 5374598.886182495, -186276.71890056884 5374600.2273336, -186266.6636319512 5374604.790203722, -186257.0265814669 5374606.984684933, -186246.2470156785 5374605.932519494, -186237.9639672053 5374602.809507255, -186229.73344470866 5374595.683295862, -186223.7766545263 5374586.122558136, -186217.35929622204 5374575.822585449, -186217.0765065549 5374575.312320732, -186204.68013338037 5374552.944308685, -186204.63336442792 5374547.153485736, -186208.95606463082 5374540.842340525, -186223.34972660447 5374532.726318846, -186245.9041115151 5374525.533084996, -186269.09822467348 5374519.95926626, -186280.9346924061 5374515.296768003)'), 
    loads('LINESTRING (-186205.67778415943 5374756.488909287, -186194.58923840598 5374732.555560231, -186181.17571289456 5374691.509660566)'), 
    loads('LINESTRING (-186247.52070756117 5374854.018672603, -186238.54512453827 5374853.279351216, -186201.07438871614 5374849.306168479, -186190.31744900843 5374848.66645448, -186181.66940103992 5374848.874358151, -186169.24658862263 5374855.36293823, -186157.49453521508 5374866.504074484, -186123.73966314102 5374909.637545475, -186118.09225373776 5374916.850662042)'), 
    loads('LINESTRING (-186222.37848502042 5374987.852352914, -186239.6977456193 5374948.258632081, -186270.85043642542 5374875.612059314, -186277.18038877263 5374855.945724207)'), 
    loads('LINESTRING (-186118.09225373776 5374916.850662042, -186147.32128710393 5374935.769480929, -186186.64667265947 5374963.227836433, -186192.79269266804 5374967.991818423, -186209.05458384939 5374980.59691115, -186214.28116861905 5374983.443016257, -186222.37848502042 5374987.852352914)'), 
    loads('LINESTRING (-186375.26059161263 5374587.678180919, -186420.63682299067 5374578.103706547, -186449.47185818187 5374572.627478305)'), 
    loads('LINESTRING (-186204.77125605455 5374430.863965389, -186199.3907598029 5374433.129274623, -186170.3887606348 5374445.339697768, -186164.7560464975 5374447.861790815, -186136.90465844076 5374461.144435263, -186123.9185495128 5374464.905452128)'), 
    loads('LINESTRING (-186152.02589610076 5374602.23750931, -186158.86137965045 5374599.0963455085, -186164.66940570483 5374597.254110526, -186170.75147771396 5374595.396541678, -186176.4224746929 5374593.56196486, -186181.56064911681 5374592.033070978, -186186.02897769128 5374590.817526234, -186190.10150934552 5374589.900000544, -186194.04465442372 5374589.127650929, -186198.39887098124 5374588.332302743, -186201.2532660037 5374587.560492676, -186203.5446770375 5374586.94090914)'), 
    loads('LINESTRING (-186181.17571289456 5374691.509660566, -186194.99192306414 5374687.839982782, -186206.51688068567 5374684.988173156, -186217.63839315556 5374682.296861053, -186229.03394973403 5374679.590203282, -186233.86755815314 5374677.5265416205, -186237.11749429896 5374674.172071204, -186238.2509356203 5374669.832487609, -186235.4779626373 5374659.504126063, -186233.3757972813 5374653.828227483, -186229.34669424454 5374643.156339129, -186227.14570643066 5374638.17568086, -186225.21113169665 5374633.042179699, -186221.63131572632 5374623.034878592, -186216.17994278783 5374618.925776361, -186211.94745997075 5374619.438444716, -186205.92601907774 5374619.913253477, -186192.79504288765 5374623.5445926245, -186179.80108056258 5374627.168248207, -186167.3781204185 5374631.173764269, -186162.4074970587 5374633.245043574)'), 
    loads('LINESTRING (-186181.17571289456 5374691.509660566, -186169.23231586732 5374654.657856142, -186162.4074970587 5374633.245043574)'), 
    loads('LINESTRING (-186122.16523259855 5374705.570027038, -186146.35726663974 5374700.630339095, -186174.9641892394 5374693.512436058, -186181.17571289456 5374691.509660566)'), 
]

fig = plt.figure(1, (8, 8))

sub1 = fig.add_subplot(111)
sub1.set_aspect('equal')
sub1.axes.get_xaxis().set_visible(False)
sub1.axes.get_yaxis().set_visible(False)

original = []
for n in network:
    original.append({"geometry": n})
original = gpd.GeoDataFrame(original)
selection = c4.detect_dead_ends(original)

sdict = selection.to_dict('records')

for s in sdict:
    geom = s['geometry']
    path1 = Path(numpy.asarray(geom.coords)[:, :2])

    if s['deadend']:
        sub1.add_patch(PathPatch(path1, facecolor="none", edgecolor='red', linewidth=1))
    else:
        sub1.add_patch(PathPatch(path1, facecolor="none", edgecolor='gray', linewidth=1))

sub1.autoscale_view()
plt.show()