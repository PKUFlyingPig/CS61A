test = {
  'name': 'Problem 10',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> p0 = [2, 2, 3]
          >>> p1 = [6, 1, 2]
          >>> fastest_words(game(['What', 'great', 'luck'], [p0, p1]))
          c32c930f01f8eb69bdbf7fd0aa69abfd
          # locked
          >>> p0 = [2, 2, 3]
          >>> p1 = [6, 1, 3]
          >>> fastest_words(game(['What', 'great', 'luck'], [p0, p1]))  # with a tie, choose the first player
          16d01ed6b3bcddbf19f54bd51db828e8
          # locked
          >>> p2 = [4, 3, 1]
          >>> fastest_words(game(['What', 'great', 'luck'], [p0, p1, p2]))
          212b9d436fcf404d25883f3c7b637515
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> p = [[2, 4, 3, 5, 1]]
          >>> fastest_words(game(['neurine', 'statutably', 'quantivalent', 'intrarachidian', 'itinerantly'], p))
          [['neurine', 'statutably', 'quantivalent', 'intrarachidian', 'itinerantly']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[4, 1, 1], [2, 5, 5]]
          >>> fastest_words(game(['unsimilar', 'conditioning', 'crystallogenical'], p))
          [['conditioning', 'crystallogenical'], ['unsimilar']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[1, 3, 2, 4, 3]]
          >>> fastest_words(game(['intraepiphyseal', 'sporangiform', 'saccharate', 'hermeneutic', 'butanal'], p))
          [['intraepiphyseal', 'sporangiform', 'saccharate', 'hermeneutic', 'butanal']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[], [], []]
          >>> fastest_words(game([], p))
          [[], [], []]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[2, 3, 5, 2, 1, 5], [3, 5, 3, 5, 4, 1], [2, 1, 3, 1, 2, 3]]
          >>> fastest_words(game(['multivoltine', 'nonpacifist', 'oviferous', 'postelection', 'multidigitate', 'reallege'], p))
          [['multivoltine', 'multidigitate'], ['oviferous', 'reallege'], ['nonpacifist', 'postelection']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[4, 1, 1, 5, 2], [1, 4, 5, 4, 2], [5, 3, 2, 2, 3]]
          >>> fastest_words(game(['notchel', 'phengitical', 'dollier', 'bushlet', 'sciographic'], p))
          [['phengitical', 'dollier', 'sciographic'], ['notchel'], ['bushlet']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[5], [3], [3]]
          >>> fastest_words(game(['cisplatine'], p))
          [[], ['cisplatine'], []]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[4]]
          >>> fastest_words(game(['accompaniment'], p))
          [['accompaniment']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[1]]
          >>> fastest_words(game(['elasticness'], p))
          [['elasticness']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[4, 2, 5, 4], [1, 3, 2, 1], [4, 2, 5, 1]]
          >>> fastest_words(game(['temporomandibular', 'unannexed', 'umbellar', 'rambutan'], p))
          [['unannexed'], ['temporomandibular', 'umbellar', 'rambutan'], []]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[2, 1, 2, 3, 1], [2, 1, 3, 1, 5]]
          >>> fastest_words(game(['intercreate', 'sulpholipin', 'inkhornizer', 'lycanthropic', 'optimize'], p))
          [['intercreate', 'sulpholipin', 'inkhornizer', 'optimize'], ['lycanthropic']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[], []]
          >>> fastest_words(game([], p))
          [[], []]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[1, 2, 5, 2, 3], [4, 3, 1, 1, 5], [3, 2, 4, 5, 4]]
          >>> fastest_words(game(['choultry', 'caryopilite', 'unowed', 'overslaugh', 'unshriveled'], p))
          [['choultry', 'caryopilite', 'unshriveled'], ['unowed', 'overslaugh'], []]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[], [], []]
          >>> fastest_words(game([], p))
          [[], [], []]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[3, 5, 3, 1]]
          >>> fastest_words(game(['nearby', 'atriopore', 'conchiferous', 'zygostyle'], p))
          [['nearby', 'atriopore', 'conchiferous', 'zygostyle']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[4, 4, 2, 1, 3]]
          >>> fastest_words(game(['infinite', 'uncorked', 'subjacency', 'looplike', 'nasoethmoidal'], p))
          [['infinite', 'uncorked', 'subjacency', 'looplike', 'nasoethmoidal']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[5, 2, 1, 1, 1, 3], [3, 5, 1, 2, 3, 3]]
          >>> fastest_words(game(['pauldron', 'kairine', 'sulpholysis', 'kalo', 'cecidiology', 'progne'], p))
          [['kairine', 'sulpholysis', 'kalo', 'cecidiology', 'progne'], ['pauldron']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[5, 2, 2, 2, 1, 3], [3, 4, 4, 4, 2, 2]]
          >>> fastest_words(game(['cnidophore', 'orrery', 'bargham', 'iridentropium', 'nickelous', 'cedarbird'], p))
          [['orrery', 'bargham', 'iridentropium', 'nickelous'], ['cnidophore', 'cedarbird']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[2, 3, 3], [1, 1, 3], [2, 3, 3]]
          >>> fastest_words(game(['inadequateness', 'capsulate', 'careers'], p))
          [['careers'], ['inadequateness', 'capsulate'], []]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[3, 1, 3, 2, 3, 3], [5, 1, 2, 4, 2, 5]]
          >>> fastest_words(game(['havent', 'kilneye', 'wistful', 'scorbutic', 'chichipe', 'antemeridian'], p))
          [['havent', 'kilneye', 'scorbutic', 'antemeridian'], ['wistful', 'chichipe']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[3, 1, 1, 3], [3, 4, 4, 1], [1, 2, 3, 3]]
          >>> fastest_words(game(['bran', 'stratum', 'onager', 'drinking'], p))
          [['stratum', 'onager'], ['drinking'], ['bran']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[], []]
          >>> fastest_words(game([], p))
          [[], []]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[4, 5, 1, 5], [3, 5, 1, 3]]
          >>> fastest_words(game(['saltless', 'bailage', 'nonformation', 'yeven'], p))
          [['bailage', 'nonformation'], ['saltless', 'yeven']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[], [], []]
          >>> fastest_words(game([], p))
          [[], [], []]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[2, 5, 4], [5, 4, 3], [4, 4, 4]]
          >>> fastest_words(game(['upbid', 'weave', 'titterer'], p))
          [['upbid'], ['weave', 'titterer'], []]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[3, 1, 5, 5, 2, 5]]
          >>> fastest_words(game(['powell', 'indifferently', 'palatograph', 'capucine', 'scowlful', 'noration'], p))
          [['powell', 'indifferently', 'palatograph', 'capucine', 'scowlful', 'noration']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[1, 5, 3, 2, 4, 2], [5, 1, 3, 4, 1, 3]]
          >>> fastest_words(game(['tautomeric', 'unprejudicedly', 'disregardance', 'reconveyance', 'rebellow', 'gaiety'], p))
          [['tautomeric', 'disregardance', 'reconveyance', 'gaiety'], ['unprejudicedly', 'rebellow']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[]]
          >>> fastest_words(game([], p))
          [[]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[5], [1]]
          >>> fastest_words(game(['incoherentific'], p))
          [[], ['incoherentific']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[2, 1, 4], [2, 1, 2]]
          >>> fastest_words(game(['accompliceship', 'dumpish', 'unqueried'], p))
          [['accompliceship', 'dumpish'], ['unqueried']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[4, 2, 4, 2, 2], [2, 4, 3, 3, 5]]
          >>> fastest_words(game(['counterflange', 'justly', 'contralto', 'erythematous', 'intromissive'], p))
          [['justly', 'erythematous', 'intromissive'], ['counterflange', 'contralto']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[], [], []]
          >>> fastest_words(game([], p))
          [[], [], []]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[2, 4, 3, 2, 5, 4], [2, 4, 2, 3, 4, 1]]
          >>> fastest_words(game(['draughtmanship', 'arboriform', 'oppugner', 'nucleonics', 'reducer', 'watered'], p))
          [['draughtmanship', 'arboriform', 'nucleonics'], ['oppugner', 'reducer', 'watered']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[]]
          >>> fastest_words(game([], p))
          [[]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[5, 4], [4, 3]]
          >>> fastest_words(game(['collectorship', 'radome'], p))
          [[], ['collectorship', 'radome']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[1, 2, 1, 4], [4, 1, 1, 2]]
          >>> fastest_words(game(['clinometrical', 'stuporose', 'didst', 'hexactinellidan'], p))
          [['clinometrical', 'didst'], ['stuporose', 'hexactinellidan']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[3, 3], [5, 2]]
          >>> fastest_words(game(['surdation', 'piddler'], p))
          [['surdation'], ['piddler']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[3, 4, 4]]
          >>> fastest_words(game(['unbattered', 'ridicule', 'undersweep'], p))
          [['unbattered', 'ridicule', 'undersweep']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[5, 3, 2], [2, 5, 1]]
          >>> fastest_words(game(['noggen', 'goofy', 'undimerous'], p))
          [['goofy'], ['noggen', 'undimerous']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[1], [5]]
          >>> fastest_words(game(['unidigitate'], p))
          [['unidigitate'], []]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[1, 3, 2], [5, 3, 4], [3, 4, 4]]
          >>> fastest_words(game(['boga', 'unzephyrlike', 'infragenual'], p))
          [['boga', 'unzephyrlike', 'infragenual'], [], []]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[4, 2, 3]]
          >>> fastest_words(game(['dysanalyte', 'whiffletree', 'mamelonation'], p))
          [['dysanalyte', 'whiffletree', 'mamelonation']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[5, 5, 2], [3, 3, 3], [5, 4, 3]]
          >>> fastest_words(game(['parapet', 'linenman', 'noneffervescent'], p))
          [['noneffervescent'], ['parapet', 'linenman'], []]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[]]
          >>> fastest_words(game([], p))
          [[]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[1, 5, 4]]
          >>> fastest_words(game(['rejumble', 'crowkeeper', 'symphyllous'], p))
          [['rejumble', 'crowkeeper', 'symphyllous']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[4, 5, 2], [1, 2, 2], [1, 1, 5]]
          >>> fastest_words(game(['phonogrammically', 'dumpiness', 'preambition'], p))
          [['preambition'], ['phonogrammically'], ['dumpiness']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[4, 5, 4, 1, 4], [3, 1, 1, 3, 4]]
          >>> fastest_words(game(['block', 'diluvialist', 'heriot', 'supersalient', 'hate'], p))
          [['supersalient', 'hate'], ['block', 'diluvialist', 'heriot']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[], [], []]
          >>> fastest_words(game([], p))
          [[], [], []]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[1, 3, 5]]
          >>> fastest_words(game(['plunderingly', 'colchicine', 'zincographical'], p))
          [['plunderingly', 'colchicine', 'zincographical']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[5, 2, 3, 5, 5], [1, 3, 4, 3, 4], [2, 5, 5, 1, 4]]
          >>> fastest_words(game(['gynospore', 'apodictically', 'villages', 'algebra', 'uprid'], p))
          [['apodictically', 'villages'], ['gynospore', 'uprid'], ['algebra']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[]]
          >>> fastest_words(game([], p))
          [[]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[1], [2], [1]]
          >>> fastest_words(game(['proker'], p))
          [['proker'], [], []]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[1, 3, 4, 4], [3, 4, 4, 2]]
          >>> fastest_words(game(['dinothere', 'faradmeter', 'oversubtlety', 'dispensatorily'], p))
          [['dinothere', 'faradmeter', 'oversubtlety'], ['dispensatorily']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[5, 1, 1, 3, 5], [2, 3, 3, 3, 2]]
          >>> fastest_words(game(['capuchin', 'diactin', 'stirps', 'waverous', 'qualifying'], p))
          [['diactin', 'stirps', 'waverous'], ['capuchin', 'qualifying']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[2, 1], [1, 2]]
          >>> fastest_words(game(['dutiability', 'acquired'], p))
          [['acquired'], ['dutiability']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[4, 2], [1, 4]]
          >>> fastest_words(game(['ribaudequin', 'healsome'], p))
          [['healsome'], ['ribaudequin']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[2, 4, 5, 2], [3, 2, 1, 5]]
          >>> fastest_words(game(['schemist', 'pentahedrous', 'relativeness', 'solivagant'], p))
          [['schemist', 'solivagant'], ['pentahedrous', 'relativeness']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[2, 2, 1, 4, 1], [2, 3, 2, 3, 1], [2, 5, 2, 3, 1]]
          >>> fastest_words(game(['micropegmatitic', 'waterhorse', 'antisubstance', 'yucker', 'samely'], p))
          [['micropegmatitic', 'waterhorse', 'antisubstance', 'samely'], ['yucker'], []]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[4]]
          >>> fastest_words(game(['nitrophytic'], p))
          [['nitrophytic']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[2, 1, 4, 1], [4, 2, 1, 2]]
          >>> fastest_words(game(['predative', 'paragrammatist', 'plurennial', 'rangership'], p))
          [['predative', 'paragrammatist', 'rangership'], ['plurennial']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[4], [1]]
          >>> fastest_words(game(['ripe'], p))
          [[], ['ripe']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[3, 4], [3, 2], [5, 4]]
          >>> fastest_words(game(['opodeldoc', 'brainlessly'], p))
          [['opodeldoc'], ['brainlessly'], []]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[], [], []]
          >>> fastest_words(game([], p))
          [[], [], []]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[2, 1, 4, 3]]
          >>> fastest_words(game(['broomwood', 'relatability', 'pearlite', 'epithecium'], p))
          [['broomwood', 'relatability', 'pearlite', 'epithecium']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[1, 1, 3, 1, 3, 1]]
          >>> fastest_words(game(['hymenean', 'crepusculine', 'solecizer', 'overfearful', 'cigar', 'veal'], p))
          [['hymenean', 'crepusculine', 'solecizer', 'overfearful', 'cigar', 'veal']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[2, 1, 2, 1, 2], [2, 3, 5, 3, 3], [3, 3, 1, 4, 1]]
          >>> fastest_words(game(['paradisic', 'unaffectionately', 'exordial', 'weaponshowing', 'rhombohedra'], p))
          [['paradisic', 'unaffectionately', 'weaponshowing'], [], ['exordial', 'rhombohedra']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[3, 4, 3, 1]]
          >>> fastest_words(game(['platybrachycephalous', 'pitometer', 'electrodepositor', 'superambitious'], p))
          [['platybrachycephalous', 'pitometer', 'electrodepositor', 'superambitious']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[2, 4], [4, 2]]
          >>> fastest_words(game(['sparrowcide', 'salubrious'], p))
          [['sparrowcide'], ['salubrious']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[5, 5, 5, 4], [4, 4, 1, 4], [4, 2, 2, 1]]
          >>> fastest_words(game(['galvanomagnetic', 'loir', 'dividedness', 'nonlipoidal'], p))
          [[], ['galvanomagnetic', 'dividedness'], ['loir', 'nonlipoidal']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[5, 2, 2], [1, 2, 1], [1, 5, 3]]
          >>> fastest_words(game(['undersorcerer', 'pneumoperitonitis', 'balaenoidean'], p))
          [['pneumoperitonitis'], ['undersorcerer', 'balaenoidean'], []]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[5, 1, 1, 5, 2, 5], [3, 2, 1, 5, 2, 3], [1, 5, 3, 3, 3, 4]]
          >>> fastest_words(game(['wold', 'relieved', 'quicksandy', 'guaraguao', 'stalkless', 'unexhilarated'], p))
          [['relieved', 'quicksandy', 'stalkless'], ['unexhilarated'], ['wold', 'guaraguao']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[3, 2, 1], [3, 2, 4]]
          >>> fastest_words(game(['tamelessly', 'unpermeated', 'myelocytic'], p))
          [['tamelessly', 'unpermeated', 'myelocytic'], []]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[3, 5, 1]]
          >>> fastest_words(game(['ferryboat', 'picky', 'wheerikins'], p))
          [['ferryboat', 'picky', 'wheerikins']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[1, 1], [4, 2], [3, 2]]
          >>> fastest_words(game(['undershut', 'unmannerly'], p))
          [['undershut', 'unmannerly'], [], []]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[5, 2, 5], [3, 4, 2], [4, 4, 1]]
          >>> fastest_words(game(['davidson', 'toadpipe', 'achete'], p))
          [['toadpipe'], ['davidson'], ['achete']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[]]
          >>> fastest_words(game([], p))
          [[]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[], []]
          >>> fastest_words(game([], p))
          [[], []]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[1, 2, 5, 4]]
          >>> fastest_words(game(['vortically', 'massicot', 'pinite', 'barbarian'], p))
          [['vortically', 'massicot', 'pinite', 'barbarian']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[4, 5, 1, 4, 5, 5], [1, 4, 5, 2, 3, 5]]
          >>> fastest_words(game(['xiphydriid', 'longicorn', 'shadchan', 'mixableness', 'journals', 'voltaic'], p))
          [['shadchan', 'voltaic'], ['xiphydriid', 'longicorn', 'mixableness', 'journals']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[1, 3], [1, 2]]
          >>> fastest_words(game(['feminility', 'voluminously'], p))
          [['feminility'], ['voluminously']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[4, 2, 3, 5, 1, 2]]
          >>> fastest_words(game(['kymbalon', 'plastogamy', 'grumpily', 'tease', 'macrocytosis', 'planterdom'], p))
          [['kymbalon', 'plastogamy', 'grumpily', 'tease', 'macrocytosis', 'planterdom']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[], []]
          >>> fastest_words(game([], p))
          [[], []]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[1, 3, 2], [5, 2, 4], [4, 4, 2]]
          >>> fastest_words(game(['apostrophic', 'nap', 'materialistical'], p))
          [['apostrophic', 'materialistical'], ['nap'], []]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[], [], []]
          >>> fastest_words(game([], p))
          [[], [], []]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[1], [5], [1]]
          >>> fastest_words(game(['afterturn'], p))
          [['afterturn'], [], []]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[], [], []]
          >>> fastest_words(game([], p))
          [[], [], []]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[]]
          >>> fastest_words(game([], p))
          [[]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[1, 2, 5, 1, 3], [1, 4, 4, 1, 4], [1, 4, 3, 4, 2]]
          >>> fastest_words(game(['belletrist', 'vegetocarbonaceous', 'woodchuck', 'phacitis', 'warehouseful'], p))
          [['belletrist', 'vegetocarbonaceous', 'phacitis'], [], ['woodchuck', 'warehouseful']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[]]
          >>> fastest_words(game([], p))
          [[]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[1, 3, 5, 2], [3, 4, 1, 1], [5, 2, 1, 2]]
          >>> fastest_words(game(['suprasphanoidal', 'thickbrained', 'pharyngographic', 'punch'], p))
          [['suprasphanoidal'], ['pharyngographic', 'punch'], ['thickbrained']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[5, 3], [3, 3]]
          >>> fastest_words(game(['unharnessed', 'fruitist'], p))
          [['fruitist'], ['unharnessed']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[3, 5, 3, 5, 2, 2], [1, 3, 2, 3, 5, 1], [2, 3, 5, 2, 4, 4]]
          >>> fastest_words(game(['spurgall', 'rampagious', 'coralberry', 'crossways', 'coconsecrator', 'afterwork'], p))
          [['coconsecrator'], ['spurgall', 'rampagious', 'coralberry', 'afterwork'], ['crossways']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[4, 5], [3, 3], [3, 2]]
          >>> fastest_words(game(['bovicide', 'bronze'], p))
          [[], ['bovicide'], ['bronze']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[2, 1, 5], [5, 2, 4]]
          >>> fastest_words(game(['spondylium', 'agrammatism', 'yad'], p))
          [['spondylium', 'agrammatism'], ['yad']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[], [], []]
          >>> fastest_words(game([], p))
          [[], [], []]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[3], [5], [3]]
          >>> fastest_words(game(['dumminess'], p))
          [['dumminess'], [], []]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[5, 2]]
          >>> fastest_words(game(['fugle', 'estimated'], p))
          [['fugle', 'estimated']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[5, 4, 5], [1, 3, 4], [5, 5, 5]]
          >>> fastest_words(game(['imbonity', 'axolemma', 'comendite'], p))
          [[], ['imbonity', 'axolemma', 'comendite'], []]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[4, 2], [2, 5], [2, 3]]
          >>> fastest_words(game(['wavement', 'carpeting'], p))
          [['carpeting'], ['wavement'], []]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[5, 5, 2], [4, 2, 2]]
          >>> fastest_words(game(['stepfatherhood', 'semiprofessional', 'diplomatist'], p))
          [['diplomatist'], ['stepfatherhood', 'semiprofessional']]
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from cats import game, fastest_words
      """,
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> test.swap_implementations(cats)
          >>> p0 = [2, 2, 3]
          >>> p1 = [6, 1, 2]
          >>> cats.fastest_words(cats.game(['What', 'great', 'luck'], [p0, p1]))
          [['What'], ['great', 'luck']]
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> import cats
      >>> import tests.abstraction_check as test #ake sure the abstraction barrier isn't crossed!
      """,
      'teardown': r"""
      >>> test.restore_implementations(cats)
      """,
      'type': 'doctest'
    }
  ]
}
