test = {
  'name': 'Problem 4',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> wpm("12345", 3) # Note: wpm returns a float (with a decimal point)
          20.0
          >>> wpm("a b c", 20)
          3.0
          >>> wpm("", 10)
          0.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> wpm("a  b  c  d", 5)
          24.0
          >>> wpm("a b c", 120)
          0.5
          >>> wpm("abc", 1)
          36.0
          >>> wpm(" a b \tc" , 1)
          84.0
          >>> wpm("", 10)
          0.0
          """,
          'hidden': False,
          'locked': False
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
          >>> round(wpm(typed_string1, 67), 1)
          99.2
          >>> round(wpm(typed_string2, 67), 1)
          98.9
          >>> round(wpm(typed_string3, 67), 1)
          2.1
          >>> round(wpm(typed_string4, 67), 1)
          100.3
          >>> round(wpm(typed_string5, 67), 1)
          199.3
          >>> round(wpm(typed_string6, 1), 1)
          132.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('neurine statutably quantivalent intrarachidian itinerantly', 18.95), 2)
          36.73
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('unsimilar conditioning crystallogenical mennom foreannouncement', 3.15), 2)
          240.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('lactonic ungroaning intraepiphyseal sporangiform saccharate hermeneutic butanal gregariously', 11.27), 2)
          97.96
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('gendarme tigerlike countergabble lollipop regovern acoelomate walnut combat', 2.58), 2)
          348.84
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('multivoltine nonpacifist oviferous postelection multidigitate reallege intercavernous', 5.67), 2)
          179.89
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('antimonarchial archaeology oopod', 5.27), 2)
          72.87
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('cisplatine cf tylostylus civil teleobjective humorsomely tubiporous picnic dubber', 18.54), 2)
          52.43
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('croup accompaniment delabialize erythematous', 21.76), 2)
          24.26
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('basidiolichen pruriently elasticness', 29.18), 2)
          14.8
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('umbellar rambutan southeasternmost correction inadhesion', 1.02), 2)
          658.82
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('intercreate sulpholipin inkhornizer lycanthropic optimize poleaxe centerable anthokyan meconin', 4.92), 2)
          229.27
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('cashable arthrosyrinx uniformitarian itemization lecithalbumin heelpiece discrimination rowdydowdy crowshay', 24.56), 2)
          52.28
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('pulicidal choultry caryopilite unowed overslaugh unshriveled', 13.28), 2)
          54.22
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('stowbordman scleromeninx', 94.27), 2)
          3.06
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('plumbosolvent nearby atriopore conchiferous zygostyle glottidean temulentive khajur', 5.93), 2)
          167.96
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('sylvanly infinite uncorked subjacency looplike nasoethmoidal capcase communicableness', 86.87), 2)
          11.74
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('pauldron kairine sulpholysis kalo cecidiology progne cosiness quotity autocatalyze', 43.75), 2)
          22.49
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('cameograph', 72.27), 2)
          1.66
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('inadequateness capsulate careers', 6.98), 2)
          55.01
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('kilneye wistful scorbutic chichipe antemeridian', 11.99), 2)
          47.04
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('inefficacity caulicule autositic', 80.48), 2)
          4.77
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('fewtrils unflashing playwrighting hamated encumberingly closh yugada staphyloptosis energeia', 10.14), 2)
          108.88
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('saltless bailage nonformation yeven argenteous', 3.93), 2)
          140.46
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('overcrop julian gaub', 62.1), 2)
          3.86
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('construction upbid', 1.28), 2)
          168.75
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('immortalness powell indifferently palatograph', 1.98), 2)
          272.73
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('rorqual tautomeric unprejudicedly disregardance reconveyance', 1.99), 2)
          361.81
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('nightstock catabaptist aloud', 55.08), 2)
          6.1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('understrain', 32.5), 2)
          4.06
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('accompliceship dumpish unqueried incedingly sudiform', 30.41), 2)
          20.52
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('undishonored counterflange justly contralto erythematous', 42.35), 2)
          15.87
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('replier bending', 60.34), 2)
          2.98
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('matriculate pandemy fruited draughtmanship arboriform oppugner nucleonics', 55.27), 2)
          15.85
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('unconjecturable lithontriptor paradoctor retinopapilitis', 7.78), 2)
          86.38
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('liminary', 61.86), 2)
          1.55
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('myelencephalous clinometrical stuporose didst hexactinellidan vacuome pulicarious semidead gourdlike', 27.71), 2)
          43.31
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('surdation piddler unbatten bemar unfeeling', 1.83), 2)
          275.41
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('undersweep sportswomanly nonlocal lorate histopathologist', 1.45), 2)
          471.72
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('rewarehouse', 74.91), 2)
          1.76
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('unidigitate scorpioidal noologist borscht spectator semiperimetry decider impaler jesse', 17.82), 2)
          58.59
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('mockernut boga unzephyrlike infragenual dimmed derelictness', 3.1), 2)
          228.39
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('', 47.32), 2)
          0.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('priesteen parapet linenman noneffervescent metasaccharinic unreversible', 3.43), 2)
          248.4
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('pulpit cig orbitelarian overstress', 6.79), 2)
          60.09
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('underdevelop rejumble crowkeeper symphyllous', 14.0), 2)
          37.71
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('phonogrammically dumpiness preambition', 1.6), 2)
          285.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('block diluvialist heriot supersalient hate', 5.2), 2)
          96.92
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('cyclose acrospore raver balzarine neomorphic lute uranostaphylorrhaphy', 64.94), 2)
          12.94
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('', 19.19), 2)
          0.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('gynospore apodictically villages algebra uprid disadvise yourselves nondeference', 30.92), 2)
          31.05
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('', 2.67), 2)
          0.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('proker unchangefulness sublevation protosyntonose saddlelike postlachrymal antetype autocinesis feces', 69.26), 2)
          17.5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('coccygeal dinothere faradmeter oversubtlety dispensatorily', 69.53), 2)
          10.01
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('thiswise capuchin diactin stirps waverous qualifying sexuparous realmless wuzzle', 29.7), 2)
          32.32
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('headliner dutiability acquired portfire dilatometric', 1.01), 2)
          617.82
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('healsome proceed oxhorn overskim polemicist injure hygrophaneity', 10.71), 2)
          71.71
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('schemist pentahedrous relativeness solivagant gloriously', 13.56), 2)
          49.56
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('carbonization micropegmatitic waterhorse antisubstance yucker samely', 66.0), 2)
          12.36
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('unguidable presentational autoheterosis', 25.61), 2)
          18.27
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('predative', 41.63), 2)
          2.59
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('ripe', 40.9), 2)
          1.17
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('appliable dysepulotic opodeldoc', 77.97), 2)
          4.77
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('ameed pneumonopleuritis', 22.8), 2)
          12.11
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('broomwood relatability pearlite epithecium', 28.63), 2)
          17.6
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('housewarming hymenean crepusculine solecizer', 21.24), 2)
          24.86
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('paradisic unaffectionately exordial weaponshowing rhombohedra', 18.64), 2)
          39.27
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('official platybrachycephalous pitometer electrodepositor', 7.19), 2)
          93.46
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('hoseless passivity sparrowcide', 39.57), 2)
          9.1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('mischieve dayfly', 34.88), 2)
          5.5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('notoriety undersorcerer pneumoperitonitis balaenoidean strawbreadth postconnubial', 32.51), 2)
          29.9
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('wold relieved quicksandy guaraguao stalkless unexhilarated', 3.19), 2)
          218.18
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('unpermeated myelocytic nonindictable pretuberculous mesoxalyl strombite muscule', 53.22), 2)
          17.81
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('embrail ferryboat picky wheerikins uncrushed monotelephone foist transempirical', 35.56), 2)
          26.66
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('imitationist undershut unmannerly sterneber nonappendicular cityish', 25.3), 2)
          31.78
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('toadpipe achete twankle hookers gardenmaker postnatal private demagogy distributor', 51.48), 2)
          19.11
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('baillone uncoacted tarnisher unwrinkled pistareen phacometer aphyllous thoraciform', 30.62), 2)
          32.14
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('unsloped', 68.07), 2)
          1.41
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('fracted traducianistic tinwork vortically massicot pinite barbarian', 1.76), 2)
          456.82
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('angelhood xiphydriid longicorn shadchan mixableness', 58.85), 2)
          10.4
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('cervicectomy vibraculoid feminility voluminously hydroferrocyanate canthotomy unequableness', 68.29), 2)
          15.99
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('kymbalon plastogamy grumpily tease macrocytosis planterdom', 47.94), 2)
          14.52
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('overprovidently obdormition precollect', 88.07), 2)
          5.18
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('baker circumscribable apostrophic', 61.53), 2)
          6.44
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('tractioneering contestant', 70.62), 2)
          4.25
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('afterturn', 23.9), 2)
          4.52
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('', 26.9), 2)
          0.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('ophiophagous rice piousness vibrissae', 2.27), 2)
          195.59
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('civicism belletrist vegetocarbonaceous woodchuck phacitis warehouseful', 6.8), 2)
          123.53
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('longboat cataria pectination immute dicrotic tressured sluggard hypothenal', 52.02), 2)
          17.07
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('discover fixative suprasphanoidal', 7.66), 2)
          51.7
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('unharnessed fruitist', 10.6), 2)
          22.64
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('tom spurgall', 23.86), 2)
          6.04
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('bronze turgidness untailorly', 1.01), 2)
          332.67
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('gong spondylium agrammatism yad unintrusted', 93.55), 2)
          5.52
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('tegularly kilnrib', 48.59), 2)
          4.2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('succeed dumminess tedder bobsleigh tenendum slatternness', 29.41), 2)
          22.85
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('biventer fugle estimated racinglike', 1.07), 2)
          392.52
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('imbonity axolemma comendite', 2.55), 2)
          127.06
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('carpeting equitriangular unforgeability antiharmonist', 60.78), 2)
          10.46
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(wpm('autoimmunization', 24.82), 2)
          7.74
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from cats import wpm
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
