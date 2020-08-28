test = {
  'name': 'Problem 3',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> accuracy("12345", "12345") # Returns 100.0
          29b153c9e33f1f3e87e909e781b23549
          # locked
          >>> accuracy("a b c", "a b c")
          29b153c9e33f1f3e87e909e781b23549
          # locked
          >>> accuracy("a  b  c  d", "b  a  c  d")
          e790dcd7d02c731a14852c9762530dff
          # locked
          >>> accuracy("a b", "c d e")
          c724dae4a49e254e46460a5c2ce9f821
          # locked
          >>> accuracy("Cat", "cat") # the function is case-sensitive
          c724dae4a49e254e46460a5c2ce9f821
          # locked
          >>> accuracy("a b c d", " a d ")
          7cbad8c4359bad70d88711ccbdb3b0d5
          # locked
          >>> accuracy("abc", " ")
          c724dae4a49e254e46460a5c2ce9f821
          # locked
          >>> accuracy(" a b \tc" , "a b c") # Tabs don't count as words
          29b153c9e33f1f3e87e909e781b23549
          # locked
          >>> accuracy("abc", "")
          c724dae4a49e254e46460a5c2ce9f821
          # locked
          >>> accuracy("", "abc")
          c724dae4a49e254e46460a5c2ce9f821
          # locked
          >>> accuracy("cats.", "cats") # punctuation counts
          c724dae4a49e254e46460a5c2ce9f821
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> reference_text = "Abstraction, in general, is a fundamental concept to computer science and software development. The process of abstraction can also be referred to as modeling and is closely related to the concepts of theory and design. Models can also be considered types of abstractions per their generalization of aspects of reality. Abstraction in computer science is also closely related to abstraction in mathematics due to their common focus on building abstractions as objects, but is also related to other notions of abstraction used in other fields such as art."
          >>> typed_string1 = "Abstraction, in general, is a fundamental concept to computer science and software development. The process of abstraction can also be referred to as modeling and is closely related to the concepts of theory and design. Models can also be considered types of abstractions per their generalization of aspects of reality. Abstraction in computer science is also closely related to abstraction in mathematics due to their common focus on building abstractions as objects, but is also related to other notions of abstraction used in other fields such as art."
          >>> typed_string2 = "Abstraction, in general, is a fundamentl concept to computer science and software development. The process of abstraction can also be referred to as modeling and is closely related to the concepts of theory and design. Models can also be considered types of abstractions per their generalization of aspects of reality. Abstraction in computer science is also closely related to abstraction in mathematics due to their common focus on building abstractions as objects, but is also related to other notions of abstraction usd in other fields such as art."
          >>> typed_string3 = "Abstraction,"
          >>> typed_string4 = "Abstraction, in general, is a fundamental concept to computer science and software development. The process of abstraction can also be referred to as modeling and is closely related to the concepts of theory and design. Models can also be considered types of abstractions per their generalization of aspects of reality. Abstraction in computer science is also closely related to abstraction in mathematics due to their common focus on building abstractions as objects, but is also related to other notions of abstraction used in other fields such as art. extra"
          >>> typed_string5 = "Abstraction, in general, is a fundamental concept to computer science and software development. The process of abstraction can also be referred to as modeling and is closely related to the concepts of theory and design. Models can also be considered types of abstractions per their generalization of aspects of reality. Abstraction in computer science is also closely related to abstraction in mathematics due to their common focus on building abstractions as objects, but is also related to other notions of abstraction used in other fields such as art. Abstraction, in general, is a fundamental concept to computer science and software development. The process of abstraction can also be referred to as modeling and is closely related to the concepts of theory and design. Models can also be considered types of abstractions per their generalization of aspects of reality. Abstraction in computer science is also closely related to abstraction in mathematics due to their common focus on building abstractions as objects, but is also related to other notions of abstraction used in other fields such as art. art"
          >>> typed_string6 = "abstraction"
          >>> round(accuracy(typed_string2, reference_text), 1)
          97.7
          >>> round(accuracy(typed_string3, reference_text), 1)
          100.0
          >>> round(accuracy(typed_string4, reference_text), 1)
          98.9
          >>> round(accuracy(typed_string5, reference_text), 1)
          49.7
          >>> round(accuracy(typed_string6, reference_text), 1)
          0.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy('statu>tably tautit up]ti]ll a\\nhydrat(e h)arpula sidecheck }shapeless structuration bra>inlike', 'statu>tably tautit up]ti]ll a\\nhydrat(e h)arpula'), 2)
          55.56
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy('condi,tioning neomorph pyrazole pinche{m asce=tically turgidness appetent theatro%=phile', 'condi,tioning neomorph pyrazole pinche{m asce=tically turgidness appetent theatro%=phile \\pterygoidal'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy('sp)orang,iform bu:dder ungothic wem(less minimus', 'sp)orang,iform bu:dder ungothic wem(less minimus'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy('gendarme lol|lipop co*mbat lumpsuc!?ker finder_ i~m{portune erratu)m', 'gendarme lol|lipop co*mbat lumpsuc!?ker finder_'), 2)
          71.43
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy("oviferous realleg_e grasswor\\m\\ nutt'ishnes-s foul lemoni@sh rotun]dn#ess", "oviferous realleg_e grasswor\\m\\ nutt'ishnes-s foul lemoni@sh"), 2)
          85.71
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy('dollier `sciogr;aphic rhopali@um retardive unli:very wenneberg}^ite a}naphroditous corresponsion', 'dollier `sciogr;aphic rhopali@um retardive unli:very'), 2)
          62.5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy('cisplatine cf: teleobjecti"ve d_ubber in"sectol%ogy pawnage passen|ger&', 'cisplatine cf: teleobjecti"ve d_ubber in"sectol%ogy pawnage'), 2)
          85.71
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy("accompaniment osteochond)ropa\\thy bellower ;apocryp%hon goall'es>s ;conformal riband str%addl'e barrenness", "accompaniment osteochond)ropa\\thy bellower ;apocryp%hon goall'es>s ;conformal"), 2)
          66.67
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy("pruriently& polony unshaded p{reimportation ca-thepsin` 'nowel/ of sheephearte(d", "pruriently& polony unshaded p{reimportation ca-thepsin` 'nowel/ of sheephearte(d xy_lotypography"), 2)
          100.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy('southeas|ternmost" d`ustbin nontreated halakah redstart cataractal +c{omplin ungarbed pseudoangelic', 'southeas|ternmost" d`ustbin nontreated halakah redstart'), 2)
          55.56
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy('intercreate inkhornizer polea;xe )anaerobio*us %ins>ubordinately s,ubprefect]orial', 'intercreate inkhornizer polea;xe )anaerobio*us %ins>ubordinately s,ubprefect]orial electromagnetism barbit>urate rhi.pidistian'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy('uniformitaria\\n di(scrimination {aqueousness cibation septuor trich"ophyl-lous', 'uniformitaria\\n di(scrimination {aqueousness cibation septuor'), 2)
          83.33
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy('pul#icidal overslaugh ectod<actylis?m [arfvedsoni,te portrayer apo=geotropically tutorials undishe}d', 'pul#icidal overslaugh ectod<actylis?m [arfvedsoni,te portrayer apo=geotropically tutorials undishe}d'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy('scleromeninx epirogeny se?ric}ipary supermoro+se uneffeminate ozone a@,thletics', 'scleromeninx epirogeny se?ric}ipary supermoro+se uneffeminate'), 2)
          71.43
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy('plumbo(sol^vent temulent;i|ve trid!ent,ate pang!en+etically morbify cystere)thism ambient `ferned', 'plumbo(sol^vent temulent;i|ve trid!ent,ate pang!en+etically morbify'), 2)
          62.5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy('uncorked nasoethmoidal[ patrist~ic i:mpa+rl effect>ive', 'uncorked nasoethmoidal[ patrist~ic i:mpa+rl effect>ive triddler "unsighting c,a#nticle magistrat\'ic'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy('kair`ine progne quotity dupery =?shisham #biog?raphies', 'kair`ine progne quotity dupery =?shisham #biog?raphies'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy('orre[ry nickelous g/randpaternal mesarteritis antony~$m u}nchewed', 'orre[ry nickelous g/randpaternal mesarteritis antony~$m u}nchewed'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy('i}nadequateness #f)eudist marc@hland sanidinic kratogeni$c hemimellitene{ mi|l!liner', 'i}nadequateness #f)eudist marc@hland sanidinic kratogeni$c hemimellitene{ mi|l!liner saltativen,ess'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy('scorbutic an]te[meridian =dunt[ hold,fast warm(er zenog#raphy preobstruction', 'scorbutic an]te[meridian =dunt[ hold,fast warm(er'), 2)
          71.43
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy("caulicule bra?n radio[log!ic incorrigible 'spiderle}ss ri~tualless nonresisti,ng rev,accin|ate", "caulicule bra?n radio[log!ic incorrigible 'spiderle}ss ri~tualless nonresisti,ng"), 2)
          87.5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy('playwrighting encumberingly <yu~gada pasang cryptogrammatist* wonder', 'playwrighting encumberingly <yu~gada pasang cryptogrammatist*'), 2)
          83.33
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy('saltless nonf?orma,tion {marin/a ca(sh undamming stringmakin:g r=ipa bra>nsolder phlebecto+m\\y', 'saltless nonf?orma,tion {marin/a ca(sh undamming stringmakin:g r=ipa bra>nsolder phlebecto+m\\y'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy('gaub unf-oxy anaphr^odis>iac completory @anaph,yte intercrust a^ct}ification cytase', 'gaub unf-oxy anaphr^odis>iac completory @anaph,yte'), 2)
          62.5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy('u<pbid dam con`,ductivity b=urion ~bevillain somesthesia muffler{', 'u<pbid dam con`,ductivity b=urion ~bevillain somesthesia muffler{ semisq<uare'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy('indiffe[rently nora|tion) highman end(ite amethodically [bolometer ph;otoshop cliqueless heterocentric', 'indiffe[rently nora|tion) highman end(ite amethodically [bolometer ph;otoshop'), 2)
          77.78
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy('_disregardance saw<er unexcuse?dness diacoe+l:e silhouettist', '_disregardance saw<er unexcuse?dness diacoe+l:e silhouettist -tash'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy('catabaptist m]oral leiomyomat#ous belive%< sto!@ve deontol[ogist- unfixedness #metamerization', 'catabaptist m]oral leiomyomat#ous belive%< sto!@ve'), 2)
          62.5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy('inc?ohe!rentific bicetyl geromorp)hism staphyl{o,ncus .an/thropomorphite furrow', 'inc?ohe!rentific bicetyl geromorp)hism staphyl{o,ncus .an/thropomorphite furrow'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy('a!ccomplic)eship s>udiform nonprotection crinoid?al bubalis ~nas(eberry umbriferously scopti-/cal', 'a!ccomplic)eship s>udiform nonprotection crinoid?al bubalis ~nas(eberry umbriferously scopti-/cal grounder'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy('e@r`ythematous mel<iorist ?endode?rmis `decentrali/st dallier c\\ondiction journalizer^) ferganite( forescene', 'e@r`ythematous mel<iorist ?endode?rmis `decentrali/st dallier c\\ondiction journalizer^) ferganite( forescene'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy('bend\\i_ng bu/lldo+zer fineles<s caesaropapacy superaward<? a(nthropotomical] enkindle', 'bend\\i_ng bu/lldo+zer fineles<s caesaropapacy superaward<?'), 2)
          71.43
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy('arboriform nucleonics wate$r^ed plu#mbism bi+se=xed diaphanometric redkne^es spor]ophyll,', 'arboriform nucleonics wate$r^ed plu#mbism bi+se=xed diaphanometric redkne^es spor]ophyll, yah:oo!'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy('par*ad^octor c+al{ycate sclerodactylia saucerlike gridir;;on demigriffin dhoti tre$ading in$(framandibular', 'par*ad^octor c+al{ycate sclerodactylia saucerlike gridir;;on'), 2)
          55.56
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy("colle[ctorship ha,ply externall=y lenti'cularis seisma!l telephone", "colle[ctorship ha,ply externall=y lenti'cularis seisma!l telephone accounti@ng"), 2)
          100.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy('-clinometrical pulicarious gourdlike unordin}arin-ess unwakened analytically', '-clinometrical pulicarious gourdlike unordin}arin-ess unwakened analytically art@:hritis vou.ge kidnap]'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy("p_idd-ler stolonate g'emmipar[ity inconglomerate hulk unmin^uted satiny{", "p_idd-ler stolonate g'emmipar[ity inconglomerate hulk"), 2)
          71.43
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy('sabered rid_i$cule thieving conferrable s-ubsero]sa counteraddress anc+onagra officeless', 'sabered rid_i$cule thieving conferrable s-ubsero]sa counteraddress anc+onagra officeless retroce$ssi^on'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy('noggen engrained"ly\\ mis"m+atchment q|uietso.me neg~ationist brom`/iodide', 'noggen engrained"ly\\ mis"m+atchment q|uietso.me neg~ationist brom`/iodide pos`+tural zei$sm'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy('unidigitate $noo`logist jesse} invernacular ?apterygot<e outdevil', 'unidigitate $noo`logist jesse} invernacular ?apterygot<e outdevil'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy('di"-mmed pin>\\ked krausite symbolry* amph/ibiousne:ss per[+fectionizement nigra>niline str:adi_ne', 'di"-mmed pin>\\ked krausite symbolry* amph/ibiousne:ss'), 2)
          62.5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy('dys;analy"te overa_rm deprivate phym\'a;toid dentinal>', 'dys;analy"te overa_rm deprivate phym\'a;toid dentinal> podium ny@ctinasti<c vagabondager'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy('line(n{man pho+toelect[ricity t@ormen?table t&ripletree antenna vicissitude@ pa}lladous_ ev~angeli>stics', "line(n{man pho+toelect[ricity t@ormen?table t&ripletree antenna vicissitude@ pa}lladous_ ev~angeli>stics extrav?as'ate"), 2)
          100.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy('_cig discrepantl`y }pr\\oclamation s,`purrer morb@$ific -abysmal acetamidine libelee #bigger', '_cig discrepantl`y }pr\\oclamation s,`purrer morb@$ific'), 2)
          55.56
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy('rejumble peripl\\e]gmatic null.@ipore spatchco/ck oviductal >zygosperm profound |p)ed _ma=mmalogical', 'rejumble peripl\\e]gmatic null.@ipore spatchco/ck oviductal >zygosperm profound |p)ed'), 2)
          88.89
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy("phonogrammically pre@ambition odalisk] crownl@e^ss subhuman flyway amorphousness dext'raural", "phonogrammically pre@ambition odalisk] crownl@e^ss subhuman flyway amorphousness dext'raural"), 2)
          100.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy('her|i,ot autodi!d)act fr#act#ional insect ri{ngmaster;', 'her|i,ot autodi!d)act fr#act#ional insect ri{ngmaster; brickcroft ideas l{ymphocystosis unacceptant'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy('balzarine lute thirtee<nfold p=aradi,ng permutableness', 'balzarine lute thirtee<nfold p=aradi,ng permutableness'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy("plunderingly colchicine 'misph#rase rela;ta` an=thr#opolater", "plunderingly colchicine 'misph#rase rela;ta` an=thr#opolater ph^otomicrographic dome in~going"), 2)
          100.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy("gynos=?pore yourselves %o-verhardy w'orkm`aster dichotomously unsociality naphthalene", "gynos=?pore yourselves %o-verhardy w'orkm`aster dichotomously"), 2)
          71.43
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy("ramp}acious devalo'ka tect(a:l tournament h'ass_ock", "ramp}acious devalo'ka tect(a:l tournament h'ass_ock"), 2)
          100.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy('suble;vation postlachrymal auto&/cinesis mu+yu{sa hemo"pexis bang', 'suble;vation postlachrymal auto&/cinesis mu+yu{sa hemo"pexis'), 2)
          83.33
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy('{dino\\there d$r$ugshop <cicindelid unilluminating d+iy| forese%t chromatophilia toss,y irradicate', '{dino\\there d$r$ugshop <cicindelid unilluminating d+iy| forese%t chromatophilia toss,y'), 2)
          88.89
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy('?waverou~s acrogenous e=x&cuss gaugeable obsequien_c\\e prevari_cation', '?waverou~s acrogenous e=x&cuss gaugeable obsequien_c\\e prevari_cation /preco-nclusion bec;a:use'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy('portfire voicele\'t unsumptuous relict} indiscre;\'etly exclam"ative=ly bi<fl]ex', 'portfire voicele\'t unsumptuous relict} indiscre;\'etly exclam"ative=ly'), 2)
          85.71
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy('proce|ed [injure lacun}ae| hypophr@enosis (transcolorati|on li.a,na stophound', 'proce|ed [injure lacun}ae| hypophr@enosis (transcolorati|on'), 2)
          71.43
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy('relativ*enes/s psalmographer m\\yomorp:hic ,zoomechanic}s horse^"herd crassly mi*nimalism thigh;t =denatur-e', 'relativ*enes/s psalmographer m\\yomorp:hic ,zoomechanic}s horse^"herd'), 2)
          55.56
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy('yucker dargsman& albuminoidal #applaudably palaeoal&chemic%al', 'yucker dargsman& albuminoidal #applaudably palaeoal&chemic%al oscurrantist zeolitizatio!<n'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy('prese/ntational revivement" runkly {co+emptor autovaccine funambulo \'pardoner lapstreaked', 'prese/ntational revivement" runkly {co+emptor autovaccine'), 2)
          62.5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy('^predative ophionine accompani}mental snift?er ur,osom"e ungymnas#tic', '^predative ophionine accompani}mental snift?er ur,osom"e ungymnas#tic +atropic circumhorizontal non^speculation'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy('ripe t#ruantship shar|)k fanioned palatize pitchi', 'ripe t#ruantship shar|)k fanioned palatize pitchi re$c:ure'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy("dysepulotic b`rainlessl#y aut.onomasy riftless tetr>a:coralline antic>holagogu+e fa't.uism p*:urism", "dysepulotic b`rainlessl#y aut.onomasy riftless tetr>a:coralline antic>holagogu+e fa't.uism"), 2)
          87.5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy('pneumonople>uritis marm<ose v&entpiece pho)tocopier nem!atode quinquev+alvous penury', 'pneumonople>uritis marm<ose v&entpiece pho)tocopier nem!atode'), 2)
          71.43
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy('!b<roomwood myt{hopoem unremova_bly devitrification monarchess calamitous undet*ain(ed denationalize worth', '!b<roomwood myt{hopoem unremova_bly devitrification monarchess calamitous undet*ain(ed denationalize worth'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy("overfear;ful )th|eopneustic swoo#ny% `thearchy morei+sh sh'are-ware exp,iati_on unnumberable postbrachial", "overfear;ful )th|eopneustic swoo#ny% `thearchy morei+sh sh'are-ware"), 2)
          66.67
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy('\'spar"ger developmentalist miscanoniz_e deformal_iz_e unerring', '\'spar"ger developmentalist miscanoniz_e deformal_iz_e unerring'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy('platybrach:ycephalou.s token screen|like ga!+slighting unrebutt`able! d-o*pper draw ve}(rsemaking encompa{ss', 'platybrach:ycephalou.s token screen|like ga!+slighting unrebutt`able! d-o*pper draw ve}(rsemaking encompa{ss'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy('sparrowcide* jap^ane.se croise$tte es". preconflict gla@ri*ngly justic{ial` male+volent', 'sparrowcide* jap^ane.se croise$tte es". preconflict gla@ri*ngly justic{ial`'), 2)
          87.5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy('galvanomagnetic dividedness nonlipoidal attitude vraic unaccusto"m clup"_eine', 'galvanomagnetic dividedness nonlipoidal attitude vraic unaccusto"m clup"_eine luc\\k{ relationist'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy('pneumoperitonitis p*ostc]onnubial quippishness nucleolocen+trosome semiseafaring reproachless between chlorobromi_de', 'pneumoperitonitis p*ostc]onnubial quippishness nucleolocen+trosome semiseafaring reproachless'), 2)
          75.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy('relieved stalk@less retroactive conducingly unvirulent filiopietistic hexadiene', 'relieved stalk@less retroactive conducingly unvirulent'), 2)
          71.43
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy('tamelessly ~myelocyti"c muscul}e spastica!lly mucivore; uplad;der jo,unce" indigna[tor`y', 'tamelessly ~myelocyti"c muscul}e spastica!lly mucivore; uplad;der jo,unce" indigna[tor`y'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy('ferry&boat} transempirica@l sneaksby week carc_ake', 'ferry&boat} transempirica@l sneaksby week carc_ake acquainted po|pu)lar suprat~emporal'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy('sterneb\'er patria meningora\\ch(idian palp=at$e harangu"er cavernulous drip-', 'sterneb\'er patria meningora\\ch(idian palp=at$e harangu"er cavernulous drip-'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy('toadp%ipe* private su&bsa~cral c@larif~y ir%redeem?able facetenes*s( anter(ointerio*r fre<eheartedly', 'toadp%ipe* private su&bsa~cral c@larif~y ir%redeem?able facetenes*s('), 2)
          75.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy(')uncoacted #phacom<eter scolecolo|gy> ?cess+ion assoilzie', ')uncoacted #phacom<eter scolecolo|gy> ?cess+ion assoilzie'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy('ra"ph:is overfold parli)amentar{ism maldigesti?on de>ca[pod debo%}sh', 'ra"ph:is overfold parli)amentar{ism maldigesti?on de>ca[pod'), 2)
          83.33
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy(']vortically met-adiorite pell%[icule col+lage:n cyto^pl<asmic phlebotome o)therworld cro>sstra%ck unpunishedly', ']vortically met-adiorite pell%[icule col+lage:n cyto^pl<asmic phlebotome o)therworld cro>sstra%ck unpunishedly'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy("longicorn shadchan jour-nals$ pla'ck! me\\senchyme", "longicorn shadchan jour-nals$ pla'ck! me\\senchyme uns\\calably"), 2)
          100.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy('voluminously canthotomy monomerous\\ re:warehouse. mi?am~i sacking grayly|', 'voluminously canthotomy monomerous\\ re:warehouse. mi?am~i sacking grayly| sov;ere:ignly'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy('plastog[$amy pa&ntophile cinchotoxine ultraradic{al $p{ayer phantoml!ike >pi(nyl un=congenially p{ausati]on', 'plastog[$amy pa&ntophile cinchotoxine ultraradic{al $p{ayer phantoml!ike >pi(nyl un=congenially'), 2)
          88.89
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy('o,bd,ormition i+nstantly ste%nocrotaphia ?a+xometry v?entrose h}y%lology `erythrogenesis improcurable', 'o,bd,ormition i+nstantly ste%nocrotaphia ?a+xometry v?entrose h}y%lology'), 2)
          75.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy('circum|scribable m/aterialis;tical por,tless tice& askance^ gran>dma fetishization noninfantry', 'circum|scribable m/aterialis;tical por,tless tice& askance^ gran>dma fetishization'), 2)
          87.5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy('berrier paroarion )hept%aploid shastraik exce:pt=ious /aortoptosis talky*', 'berrier paroarion )hept%aploid shastraik exce:pt=ious'), 2)
          71.43
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy('afterturn celadon t!hin crani"osto%sis cash^ eking archaeologist', 'afterturn celadon t!hin crani"osto%sis cash^ eking'), 2)
          85.71
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy('subjectiveness myr?istic caddl]"e artiod\\actyl` refectorian punner divisibil(ity', 'subjectiveness myr?istic caddl]"e artiod\\actyl` refectorian'), 2)
          71.43
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy('rice vibrissae enwind- influentia<lly calcareocorneous postcommissure crystallographical ?magnil<oquy quillaja', 'rice vibrissae enwind- influentia<lly calcareocorneous'), 2)
          55.56
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy('>phaciti!s ludicropathetic zo[odynamic lenticul>othalamic cratches azox|yphenetol^e hydropo?ni^cs revi)ewer', '>phaciti!s ludicropathetic zo[odynamic lenticul>othalamic cratches azox|yphenetol^e hydropo?ni^cs revi)ewer'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy('cata+ria tress"ured; ther"ea,fter misexpl(ain tai|pa[n', 'cata+ria tress"ured; ther"ea,fter misexpl(ain tai|pa[n'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy('suprasph&an,oidal (tubemaki`ng seriog<rotesqu?e ontoge["ny ent~omologize vertible< jurisprudentialist songwright;', 'suprasph&an,oidal (tubemaki`ng seriog<rotesqu?e ontoge["ny ent~omologize vertible< jurisprudentialist songwright; r|edigest'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy('unharnessed !tai+lorize allozooid= malefactory rerummage veep ;dustma*n at/"miatry', 'unharnessed !tai+lorize allozooid= malefactory rerummage veep ;dustma*n'), 2)
          87.5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy('ramp/agious a+fter{work vicety evan=escence inco<rruptn|ess temporarily| mu%corrhe|a', 'ramp/agious a+fter{work vicety evan=escence inco<rruptn|ess temporarily| mu%corrhe|a'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy('b\'ovicid,e tachyglossa!l he{avyheart\\ed p,alatalism. pragmatical wonderin"g enterprisingl?y', 'b\'ovicid,e tachyglossa!l he{avyheart\\ed p,alatalism. pragmatical wonderin"g enterprisingl?y'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy('@agrammatism pach?ydermia unnoticeab<le feretory attributes o&verbrigh,t t:etrahedro!n a-s>sure', '@agrammatism pach?ydermia unnoticeab<le feretory attributes o&verbrigh,t t:etrahedro!n a-s>sure chromatograph,y'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy('te$gularly phylogen^y )expansi;ble a_perture unending!\\ly vernaculari_st ca/pping @.monarchian', 'te$gularly phylogen^y )expansi;ble a_perture unending!\\ly vernaculari_st ca/pping'), 2)
          87.5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy('tedd&er# nutp!ecker pep<s)inate atl:,antic psalmodize shel#l@', 'tedd&er# nutp!ecker pep<s)inate atl:,antic psalmodize shel#l@ pursley hemang#iosarco-ma'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy('fugle ra"cinglike pedest`rian h&eteropoly# c$osmog{onist poly?phon:e taeniaci-de foregame ci~st', 'fugle ra"cinglike pedest`rian h&eteropoly# c$osmog{onist poly?phon:e taeniaci-de'), 2)
          77.78
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy('imb(onity riziform sodd>ing kickup wiresmith .differe|nt inflicter', 'imb(onity riziform sodd>ing kickup wiresmith .differe|nt inflicter s}ummon'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy('wave"ment co#nfess* wh@eelery pendulumlik$e noctambulous charkhana catst*[one', 'wave"ment co#nfess* wh@eelery pendulumlik$e noctambulous charkhana catst*[one'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(accuracy('stepfatherhood diplomatist autoreinfusion a\\$poxesis formal`dehyde omophagia', 'stepfatherhood diplomatist autoreinfusion a\\$poxesis formal`dehyde omophagia !rooklet- veuglai`re'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from cats import accuracy
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
