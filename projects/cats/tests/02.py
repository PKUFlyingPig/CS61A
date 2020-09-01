test = {
  'name': 'Problem 2',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> dogs = about(['dogs', 'hounds'])
          >>> dogs('A paragraph about cats.')
          False
          >>> dogs('A paragraph about dogs.')
          True
          >>> dogs('Release the Hounds!')
          True
          >>> dogs('"DOGS" stands for Department Of Geophysical Science.')
          True
          >>> dogs('Do gs and ho unds don\'t count')
          False
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from cats import about
      """,
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> ab = about(['neurine', 'statutably', 'quantivalent', 'intrarachidian', 'itinerantly', 'cloaklet'])
          >>> ab('unhollow simsim dcloakletB itinerantly cloakLet dQUaNtivalentJ gnEurinE fissiparity Mneurinel')
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['unsimilar', 'conditioning', 'crystallogenical', 'mennom', 'foreannouncement', 'neomorph'])
          >>> ab('#crystallogenIcalW podded reorganizationist neomorPhf hneomorphj')
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['lactonic', 'ungroaning', 'intraepiphyseal', 'sporangiform', 'saccharate', 'hermeneutic', 'butanal', 'gregariously', 'splenopexy'])
          >>> ab('Hsp\\leno?pexy qsacchar<ate, dungroaninGy pennate Ybutanal zbutana|l proterogyny')
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['gendarme', 'tigerlike', 'countergabble', 'lollipop', 'regovern', 'acoelomate', 'walnut', 'combat', 'reattribution'])
          >>> ab('tig;eRlikE fiscal nwaLnut cou(ntergab!bleg unsuccessiveness reattr<ibuTion acoeloma$te!U EgEndarme scrappily')
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['multivoltine', 'nonpacifist', 'oviferous', 'postelection', 'multidigitate', 'reallege', 'intercavernous', 'marmose'])
          >>> ab('sreAllege Omultivoltine postelEct>IonK Tpostelectiong ZposteLection')
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['antimonarchial', 'archaeology', 'oopod', 'notchel'])
          >>> ab('Hn`otcHelG packed saNtimonarchial a[ntimOna]rchiaLj dnotche}Lv')
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['cf', 'tylostylus', 'civil', 'teleobjective'])
          >>> ab('bty)loStyl.uss vexillar hciv~ilf oviparousness tylostylus gciviL ^CfH bridger plastochrone')
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['croup', 'accompaniment', 'delabialize', 'erythematous', 'gossipdom'])
          >>> ab('accomp=ani<mentY pleuronectoid petrographical gossi\\[pdomJ toetoe')
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['basidiolichen', 'pruriently', 'elasticness', 'polony'])
          >>> ab('exterior mannerable elastiCnessD bprurienTlyl eLasticneSs')
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['umbellar', 'rambutan', 'southeasternmost', 'correction', 'inadhesion', 'featherfew'])
          >>> ab('UmbellarB sparky coRrectionh tsoutheasternmoStW interradiation lumbEll]art')
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['intercreate', 'sulpholipin', 'inkhornizer', 'lycanthropic', 'optimize'])
          >>> ab('sulpholi*piN proctoparalysis rInkhornizer RlycanthropicY optimi`#zeg -optimizeo lycanthropicB lycanthrOpICK')
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['uniformitarian'])
          >>> ab('U-nif#ormitarianr uniformitarian buNi=formitaRian leucitis enantiopathia uniformitarian U-nif!ormitarian')
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['pulicidal', 'choultry', 'caryopilite', 'unowed', 'overslaugh', 'unshriveled', 'ectodactylism'])
          >>> ab('ectodactylisma ecT${odactylismL transform diaheliotropic carYopi?l~iteT aunowE-d,e ectodactyli]smI Rcaryop,iliT@eG .puli^Cidalk')
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['stowbordman', 'scleromeninx', 'wringstaff'])
          >>> ab('stowbordmaN porkfish scleromenInx updart nether')
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['plumbosolvent', 'nearby', 'atriopore', 'conchiferous', 'zygostyle', 'glottidean', 'temulentive', 'khajur', 'chirognomy'])
          >>> ab('glott;ID|eanD (aTrioPor[ed tem^ulenT/iveg Rplumbosolventt zygo[styleV pseudoacaccia pLumboSolve-ntm tEmulenTivEg sweetbrier')
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['sylvanly', 'infinite', 'uncorked', 'subjacency', 'looplike', 'nasoethmoidal', 'capcase', 'communicableness', 'blown'])
          >>> ab("infi!niTe eu.nCorkEd+ nasoethmoi-daL glooPlikes Bcommu[nicabl'eNesst")
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['sulpholysis', 'kalo', 'cecidiology', 'progne', 'cosiness', 'quotity'])
          >>> ab('kaloI marsoon TcecidIology s`u,Lpholysism uprognez =sulphoLysisL ncec{idiologY')
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['cameograph', 'cnidophore'])
          >>> ab('unhushable monoprionidian UcameographL coccidia cnidophorev')
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['inadequateness', 'capsulate', 'careers', 'sublanceolate'])
          >>> ab('finadeQuate#ness]V clownship Sublan!ceol_atem capsulitis sublanceolatet chantry')
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['kilneye', 'wistful', 'scorbutic', 'chichipe', 'antemeridian', 'metapolitical'])
          >>> ab('Nmetapolitica}lm UmetapoliTica:l unapproximately ch+i@chipeD aNtemeRi^dianq')
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['inefficacity', 'caulicule', 'autositic', 'zimme'])
          >>> ab('ottajanite inEffIcacityv plasmodiocarp cc-Aul(iculex inefficaciTyX')
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['playwrighting', 'hamated', 'encumberingly', 'closh', 'yugada', 'staphyloptosis', 'energeia', 'microclimatologic', 'pasang'])
          >>> ab('=PlAYwrightInGX VpasA&ngw yugada energeia zpla,ywRIgh|ting CpAsangq')
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['saltless', 'bailage', 'nonformation', 'yeven', 'argenteous', 'ha'])
          >>> ab('iy:e.venN A[rgentEo]usT largenteous clamminess gbaILa.geY stoicism')
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['overcrop', 'julian', 'gaub', 'roland'])
          >>> ab('tenectomy UrOland haec Kover`c(ropb pneumatolitic roland overc]ropz GOvercrop Xroland')
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['construction', 'upbid', 'weave'])
          >>> ab('weave, amphidetic weave untotalled weAveN hweave weaveF pasticheur')
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['immortalness', 'powell', 'indifferently', 'palatograph', 'capucine'])
          >>> ab('enterer Qpalatograph implacement shepherdry indiff"er<ently')
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['rorqual', 'tautomeric', 'unprejudicedly', 'disregardance', 'reconveyance', 'rebellow'])
          >>> ab("quabird grebellOw] rebEl'l*owm rebell/]OWh learnt")
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['nightstock', 'catabaptist', 'aloud', 'ultramelancholy'])
          >>> ab('ualouD/c mines push dnightsTock ial&oud')
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['understrain', 'incoherentific'])
          >>> ab('kun+derstraink munderstRain vaporiferousness silly palaeocrystalline cauliculus subnatural')
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['accompliceship', 'dumpish', 'unqueried', 'incedingly', 'sudiform', 'neighborless'])
          >>> ab('incedingly sequency sudiform dumpish YUnqueried Sdumpish Gneig}hbOrlessq KincedinglyX')
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['undishonored', 'counterflange', 'justly', 'contralto', 'erythematous', 'intromissive'])
          >>> ab('counterflange cOntra=\\lto IntromIssiven unperforate j,ustl#yi iNtromissIveS undishonored')
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['replier', 'bending', 'uptree'])
          >>> ab('replier uptr$eeC bantay salpingostaphyline aupTre[Er')
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['matriculate', 'pandemy', 'fruited', 'draughtmanship', 'arboriform', 'oppugner', 'nucleonics', 'reducer'])
          >>> ab('f@rui,ted reducer draughtmanshipD toxa PfrUited ZMatRi[culateA maTricuLatEi lmaTricuLate].D matriculate')
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['unconjecturable', 'lithontriptor', 'paradoctor', 'retinopapilitis', 'unabsolvedness'])
          >>> ab('u/nconjectura{bleJ unco(njEctUrable unconjecturable pAradoct<ord trenchermaking Aretinopapilitis')
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['liminary', 'collectorship'])
          >>> ab('pearlin unbrent vliminary>O Xlim;iNaryf collectorship liminary pretranscription fliminaryQ liminary')
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['stuporose', 'didst', 'hexactinellidan', 'vacuome', 'pulicarious', 'semidead', 'gourdlike', 'powerboat'])
          >>> ab('tvacuome hippometry sgourdlIKe satisfying hexactiNellidanT')
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['surdation', 'piddler', 'unbatten', 'bemar', 'unfeeling', 'thermalgesia'])
          >>> ab('unbatten tracksick pIddleRs munbatten ^BemaR piDdler*] news')
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['undersweep', 'sportswomanly', 'nonlocal', 'lorate', 'histopathologist', 'trichiuroid'])
          >>> ab('zoomorphize trichiuroid SportSwomanlyj Nonlocal nonlOcalA p{lorate/ NundersweepR thisto/pathologisT Klorate<')
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['rewarehouse', 'noggen'])
          >>> ab('CreWarEhous\\e rewarehouse pina desquamatory Mnoggeny threadweed')
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['noologist'])
          >>> ab('bagreef desiredly xnooL+ogist<E warmth unstainableness theomorphic eliasite')
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['mockernut', 'boga', 'unzephyrlike', 'infragenual', 'dimmed', 'derelictness', 'morphologic'])
          >>> ab('gopher lord dimmeDw Xmo$cke`rnuTC bogAY')
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['parapteron'])
          >>> ab('quinaldyl spiritland simply laver untakable nonsensitive xparapter>onA')
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['priesteen', 'parapet', 'linenman', 'noneffervescent', 'metasaccharinic', 'unreversible', 'desiderata'])
          >>> ab('desid@erataP Bnonefferve?s]centr des\\iDEra]tag linenmanx parapet k&unreversible desiderata~L (uNreversi~BleN')
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['pulpit', 'cig', 'orbitelarian', 'overstress', 'voicelessness'])
          >>> ab('xoV_Erst-ressR voi=c:elessness V)oicelessneSs psaltes NoRbitelarian')
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['underdevelop', 'rejumble', 'crowkeeper', 'symphyllous', 'narratress'])
          >>> ab('troolie underdevelOpw sym+phyl`lOusF undecidedly rrEjumbleR nnarRatressF')
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['phonogrammically', 'dumpiness', 'preambition', 'halisteretic'])
          >>> ab('jha}liStEretic" ha%listereti<c interimistic inexhaustive yogin yphonogrammicallyw smokefarthings dauntingly halisteretic')
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['block', 'diluvialist', 'heriot', 'supersalient', 'hate', 'septation'])
          >>> ab('=sep.tatiOnA handmaid hate Hhe}rio(tt zheRiot^$')
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['cyclose', 'acrospore', 'raver', 'balzarine', 'neomorphic', 'lute', 'uranostaphylorrhaphy', 'thirteenfold'])
          >>> ab('balzarine acrospore hluteY ,baLzarine UneOmorphIc')
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['pedestal'])
          >>> ab('valeta counselful pedestal nonstudious matral divata pedes}taL')
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['gynospore', 'apodictically', 'villages', 'algebra', 'uprid', 'disadvise', 'yourselves', 'nondeference', 'overhardy'])
          >>> ab('tetchy Xnondeferencex uovErhardYh dIsadvis}ef bridely orientator')
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['lipomyxoma'])
          >>> ab('shoreyer lipomyxoma cojuror squdge luxuriancy')
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['unchangefulness', 'sublevation', 'protosyntonose', 'saddlelike', 'postlachrymal', 'antetype'])
          >>> ab('OanTety>peW unchangefulness ootocous wuncHangefulnessx bagpipes saddlelike')
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['coccygeal', 'dinothere', 'faradmeter', 'oversubtlety', 'dispensatorily', 'manganapatite'])
          >>> ab('d~is&penSaTorilyc browbeater dIspensatorilyZ Omanganapatiteg amanganapatite mangaNapatItEG Hdispensatorily roulette')
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['diactin', 'stirps', 'waverous', 'qualifying', 'sexuparous', 'realmless'])
          >>> ab('Hstirpsj sexuparOusj waver>ousQ sexuparOus_R cqualIfying st_irPs# sexupaRous')
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['headliner', 'dutiability', 'acquired', 'portfire', 'dilatometric', 'voicelet'])
          >>> ab('Dvo)^icelEtB acquired inhaler sdilatome&trIc pour claut portfire@m Zhe-adlinerm')
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['healsome', 'proceed', 'oxhorn', 'overskim', 'polemicist', 'injure', 'hygrophaneity', 'chairmender'])
          >>> ab('sproceedf y|healso"me vpolemicisTW embrocate hygrophaneity Xproceed ThygroPhaneIty')
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['schemist', 'pentahedrous', 'relativeness', 'solivagant', 'gloriously', 'epistolet'])
          >>> ab('relativenesse pentahedrous Ygloriou#slyq foretalking Agloriously trelativen&esSA dschemist')
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['carbonization', 'micropegmatitic', 'waterhorse', 'antisubstance', 'yucker', 'samely', 'dargsman'])
          >>> ab('whank samely waterhorse usa;me,lYj antisubstance ddargsman micropegmatitic chack')
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['unguidable', 'presentational', 'autoheterosis', 'nitrophytic'])
          >>> ab('utrum cerebralist unguidable tpre,sEnta(tionaL AunguidabLE composure p#resen.tationaL autoheterosis')
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['predative', 'paragrammatist'])
          >>> ab('pRed@ati)veK abhiseka rpredAt(Ive h$paragrammatist/ GparagrammatistD prEdative')
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['ripe', 'spatuliform'])
          >>> ab('monopyrenous zspatuliform E:ripe lr#ip.ey cauligenous tod toddle')
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['appliable', 'dysepulotic', 'opodeldoc', 'brainlessly'])
          >>> ab('ortho hopodeldoc fappliableV postcolumellar rebounder')
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['ameed', 'pneumonopleuritis', 'maidenweed'])
          >>> ab("pnE-umO*NOpleuritis pNeumOnopLeuritis' pneumonopleuritis Eameed tabletary epneumOnopleuritis maidenweed")
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['broomwood', 'relatability', 'pearlite', 'epithecium', 'saddlenose'])
          >>> ab('ape@arlite WrelatabilityR Zsaddl|enos$E piperidine commissariat aphasia')
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['housewarming', 'hymenean', 'crepusculine', 'solecizer', 'overfearful'])
          >>> ab('engloom electrotest crosscutting housewarmings SsoLecizErN solecizer vcrepus"culIn|eY tenementer LhouSewarmingQ')
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['paradisic', 'unaffectionately', 'exordial', 'weaponshowing', 'rhombohedra', 'sparger'])
          >>> ab('Orhombohedra lexordials subjunctively jrhombo@Hedra= paradis#icO')
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['official', 'platybrachycephalous', 'pitometer', 'electrodepositor', 'superambitious'])
          >>> ab('thundersquall pockmark Bpitome}t^er mplatybrachycephalousQ oFficial T;official piTometerH oddsman')
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['hoseless', 'passivity', 'sparrowcide', 'salubrious'])
          >>> ab('hoseless_ tonalist comboy coislander opa_ssivITys pAss[ivIty> psaLubrIousV hoseleSs')
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['mischieve', 'dayfly', 'galvanomagnetic'])
          >>> ab('dayfly\\_V dayflyU mischieVey ydayfly precipitantly dmischievey')
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['notoriety', 'undersorcerer', 'pneumoperitonitis', 'balaenoidean', 'strawbreadth', 'postconnubial', 'cauligenous'])
          >>> ab('siket unwhelped misexpend academically gemmipara cAuligEnous')
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['wold', 'relieved', 'quicksandy', 'guaraguao', 'stalkless', 'unexhilarated', 'strifeproof'])
          >>> ab('wo\\LdT funexhilarAt:ed& ejection comeuppance Erelieve"d woldg')
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['unpermeated', 'myelocytic', 'nonindictable', 'pretuberculous', 'mesoxalyl', 'strombite', 'muscule', 'cheesemongerly'])
          >>> ab('prETUb^eRcu,LoUsK mesoxalylN oxybutyric udal FmUS^*Culeh umye)locyticG')
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['embrail', 'ferryboat', 'picky', 'wheerikins', 'uncrushed', 'monotelephone', 'foist', 'transempirical', 'gawkily'])
          >>> ab('thujene eightpenny afois>tS wh\\eerik<insr Uncru-shed nonlaying ke.mBrail>n Wferryboat ferrybOat')
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['imitationist', 'undershut', 'unmannerly', 'sterneber', 'nonappendicular', 'cityish', 'caimito'])
          >>> ab('cityishu ycityisHm Zcaimito asterneBer On{{onappendiCularK')
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['hookers', 'gardenmaker', 'postnatal', 'private', 'demagogy'])
          >>> ab('gardenMakery teleological WhookersG u:demagogyB JHo=okersV')
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['baillone', 'uncoacted', 'tarnisher', 'unwrinkled', 'pistareen', 'phacometer', 'aphyllous', 'thoraciform', 'megaron'])
          >>> ab('megaronI +phacometeR havenership aphy-llOu/sw Rpistareene Run,cOactedT Gun$wrinkleDo :"pistareenK rpistareen/')
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['unsloped', 'fucous'])
          >>> ab('OunslopEd indissociable clitoridectomy undefectible predisponency multiplex')
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['fracted', 'traducianistic', 'tinwork', 'vortically', 'massicot', 'pinite', 'barbarian', 'shank'])
          >>> ab('ensigncy vortically =tiNwork yvortically fracted tinwork dustuck')
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['angelhood', 'xiphydriid', 'longicorn', 'shadchan', 'mixableness', 'journals'])
          >>> ab('Kmi>xablen"ess xiphydriid saltine longicorN longicornY')
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['cervicectomy', 'vibraculoid', 'feminility', 'voluminously', 'hydroferrocyanate', 'canthotomy', 'unequableness', 'monomerous'])
          >>> ab('dedendum voluminously feminilityJ monomerousr BmoNO%merOU>sM cornerwise')
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['kymbalon', 'plastogamy', 'grumpily', 'tease', 'macrocytosis', 'planterdom', 'pantophile'])
          >>> ab('jkym!b?alon pAntophile pla*stogamyy pAntophileJ phasmatid oligodendroglia')
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['overprovidently', 'obdormition', 'precollect', 'productivity'])
          >>> ab('aesthophysiology obdormition trabant obdo!Rmitionm }obdorMitionD cOverproviDeNtlyG doVe|rProVi+DenTlyK')
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['baker', 'circumscribable', 'apostrophic', 'nap'])
          >>> ab('apostrOphic troopfowl a{postrophic circumscribable foreroyal Z}(bakeR cIrcUmscrib@AbLe D%nApQ')
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['tractioneering', 'contestant', 'berrier'])
          >>> ab("Ktractioneering croucher z'tractioneering nonverminous capper")
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['afterturn', 'semispeculation'])
          >>> ab('semispeculation semispeculationv coarbiter mydatoxine zincograph')
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['subjectiveness'])
          >>> ab('podagra waikness haulage semiprivacy insubordinate LsubjectiveNeSsH IsubjeCtiven-ess')
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['ophiophagous', 'rice', 'piousness', 'vibrissae', 'diplocardiac'])
          >>> ab('cap ophiophagous TdiplocarDIacW vibrissae droud hencote ]vibriss=ae')
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['civicism', 'belletrist', 'vegetocarbonaceous', 'woodchuck', 'phacitis', 'warehouseful', 'intertwine'])
          >>> ab('division rphaciTI]s)P vEgetocarbonaceous intertwineb warehouseful RVegetoCarbonaceouSd')
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['longboat', 'cataria', 'pectination', 'immute', 'dicrotic', 'tressured', 'sluggard', 'hypothenal', 'acrologism'])
          >>> ab('unstintingly t(ressuredt Nslug)gard@P QslUGgard immuteS')
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['discover', 'fixative', 'suprasphanoidal', 'thickbrained'])
          >>> ab('disc[overC suprasphanoidal engraft Psup:raSph@anoidaLU unintromitted ksup^rasphanOi]daLN unsaponifiable dIScoverw SupraspHano^ida\\l')
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['unharnessed', 'fruitist', 'resolicit'])
          >>> ab('U_Fruitis(t Z!unharnessed script VresolicitV mail')
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['tom', 'spurgall', 'rampagious'])
          >>> ab('tOM spurgallU centrosphere arouse tomX')
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['bronze', 'turgidness', 'untailorly', 'untewed'])
          >>> ab('TturgidneSsl rectilineal yuNtaIlorlYL bronzeA turgidness Iu(nTAilOrlY untailorly')
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['gong', 'spondylium', 'agrammatism', 'yad', 'unintrusted', 'nosy'])
          >>> ab('turrigerous dynamitism aminoacetophenone sPondyLiumt GnosyA lspondyliumV')
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['tegularly', 'kilnrib', 'sulphonalism'])
          >>> ab('tkilnrib/M wSulphO:nA"liSmR sUlph,onalismD tetrazolium ksUlphonalism tegularlyy')
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['succeed', 'dumminess', 'tedder', 'bobsleigh', 'tenendum', 'slatternness', 'longsomeness'])
          >>> ab('cs?ucceed longsomenessl lapwork Ab*obSleigh dumMiNes<su')
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['biventer', 'fugle', 'estimated', 'racinglike', 'clavelization'])
          >>> ab("UclavelizationT f@'ugle rfug*le progressionist estimated bi`veNtErj cLa\\vel`izationp esti(matEdG")
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['imbonity', 'axolemma', 'comendite', 'communicableness'])
          >>> ab('foredevote parosteal comendi<}tex consent misken costiform scraggled Zimbo=]nity')
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['carpeting', 'equitriangular', 'unforgeability', 'antiharmonist', 'diasynthesis'])
          >>> ab('cephaloplegic equitriangular antiharmonist unforgeability d`equitr)iangularB')
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ab = about(['autoimmunization', 'stepfatherhood'])
          >>> ab('retinopapilitis encoop autoimmUnizatiOnn Fau]toImmunizAtionL unchance')
          False
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from cats import about
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
