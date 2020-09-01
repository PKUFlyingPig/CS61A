test = {
  'name': 'Problem 8',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> typed = ['I', 'have', 'begun']
          >>> prompt = ['I', 'have', 'begun', 'to', 'type']
          >>> print_progress({'id': 1, 'progress': 0.6})
          ID: 1 Progress: 0.6
          >>> report_progress(typed, prompt, 1, print_progress) # print_progress is called on the report
          ID: 1 Progress: 0.6
          0.6
          >>> report_progress(['I', 'begun'], prompt, 2, print_progress)
          ID: 2 Progress: 0.2
          0.2
          >>> report_progress(['I', 'hve', 'begun', 'to', 'type'], prompt, 3, print_progress)
          ID: 3 Progress: 0.2
          0.2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress(['neurine'], ['neurine', 'statutably', 'quantivalent', 'intrarachidian', 'itinerantly'], 21, print_progress)
          ID: 21 Progress: 0.2
          0.2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress([], ['unsimilar', 'conditioning', 'crystallogenical', 'mennom', 'foreannouncement'], 16, print_progress)
          ID: 16 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress(['lactonic', 'ungroaning', 'intraepiphyseal', 'sporangiform', 'saccharate', 'hermeneutic', 'butanal'], ['lactonic', 'ungroaning', 'intraepiphyseal', 'sporangiform', 'saccharate', 'hermeneutic', 'butanal', 'gregariously'], 37, print_progress)
          ID: 37 Progress: 0.875
          0.875
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress(['gendarme'], ['gendarme', 'tigerlike', 'countergabble', 'lollipop', 'regovern', 'acoelomate', 'walnut', 'combat'], 10, print_progress)
          ID: 10 Progress: 0.125
          0.125
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress(['multivoltine', 'nonpacifist'], ['multivoltine', 'nonpacifist', 'oviferous', 'postelection', 'multidigitate', 'reallege', 'intercavernous'], 36, print_progress)
          ID: 36 Progress: 0.2857142857142857
          0.2857142857142857
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress(['baNtimOnarchial', 'archaeology'], ['antimonarchial', 'archaeology', 'oopod'], 82, print_progress)
          ID: 82 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress(['Acf#z', 'tylostylU"sW'], ['cf', 'tylostylus', 'civil'], 15, print_progress)
          ID: 15 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress(['croup', 'accompaniment', 'delabialize'], ['croup', 'accompaniment', 'delabialize', 'erythematous'], 56, print_progress)
          ID: 56 Progress: 0.75
          0.75
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress([], ['basidiolichen', 'pruriently', 'elasticness'], 83, print_progress)
          ID: 83 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress(['umbellar'], ['umbellar', 'rambutan', 'southeasternmost', 'correction', 'inadhesion'], 59, print_progress)
          ID: 59 Progress: 0.2
          0.2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress([], ['intercreate', 'sulpholipin', 'inkhornizer', 'lycanthropic'], 89, print_progress)
          ID: 89 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress([], ['uniformitarian'], 81, print_progress)
          ID: 81 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress([], ['pulicidal', 'choultry', 'caryopilite', 'unowed', 'overslaugh', 'unshriveled'], 22, print_progress)
          ID: 22 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress([], ['stowbordman', 'scleromeninx'], 25, print_progress)
          ID: 25 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress(['Rplumbosolvent', 'nearby', 'atriopore', 'conchiferous', 'zygoStyleJ'], ['plumbosolvent', 'nearby', 'atriopore', 'conchiferous', 'zygostyle', 'glottidean', 'temulentive', 'khajur'], 57, print_progress)
          ID: 57 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress(['sylvanly', 'infinite', 'uncorked'], ['sylvanly', 'infinite', 'uncorked', 'subjacency', 'looplike', 'nasoethmoidal', 'capcase', 'communicableness'], 24, print_progress)
          ID: 24 Progress: 0.375
          0.375
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress(['sulpholysis', 'kalo', 'cecid<iology', 'progne'], ['sulpholysis', 'kalo', 'cecidiology', 'progne', 'cosiness'], 88, print_progress)
          ID: 88 Progress: 0.4
          0.4
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress([], ['cameograph'], 6, print_progress)
          ID: 6 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress(['inadequateness'], ['inadequateness', 'capsulate', 'careers'], 66, print_progress)
          ID: 66 Progress: 0.3333333333333333
          0.3333333333333333
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress(['Ckilneyex', 'wistful'], ['kilneye', 'wistful', 'scorbutic', 'chichipe', 'antemeridian'], 68, print_progress)
          ID: 68 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress([], ['inefficacity', 'caulicule', 'autositic'], 90, print_progress)
          ID: 90 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress([], ['playwrighting', 'hamated', 'encumberingly', 'closh', 'yugada', 'staphyloptosis', 'energeia', 'microclimatologic'], 63, print_progress)
          ID: 63 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress(['saltless', 'bailage', 'nonformation', 'ByevenX'], ['saltless', 'bailage', 'nonformation', 'yeven', 'argenteous'], 1, print_progress)
          ID: 1 Progress: 0.6
          0.6
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress([], ['overcrop', 'julian', 'gaub'], 31, print_progress)
          ID: 31 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress(['construction'], ['construction', 'upbid'], 17, print_progress)
          ID: 17 Progress: 0.5
          0.5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress(['immortalness', 'powell'], ['immortalness', 'powell', 'indifferently', 'palatograph'], 8, print_progress)
          ID: 8 Progress: 0.5
          0.5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress(['rorqual', 'tautomeric'], ['rorqual', 'tautomeric', 'unprejudicedly', 'disregardance', 'reconveyance'], 45, print_progress)
          ID: 45 Progress: 0.4
          0.4
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress([], ['nightstock', 'catabaptist', 'aloud'], 37, print_progress)
          ID: 37 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress([], ['understrain'], 5, print_progress)
          ID: 5 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress(['accompliceship', 'dumpish&', 'unqueried'], ['accompliceship', 'dumpish', 'unqueried', 'incedingly', 'sudiform'], 11, print_progress)
          ID: 11 Progress: 0.2
          0.2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress(['undishonored', 'counterflange'], ['undishonored', 'counterflange', 'justly', 'contralto', 'erythematous'], 46, print_progress)
          ID: 46 Progress: 0.4
          0.4
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress([], ['replier', 'bending'], 23, print_progress)
          ID: 23 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress(['matriculate', 'pandemy', 'fruited', 'draughtmanship'], ['matriculate', 'pandemy', 'fruited', 'draughtmanship', 'arboriform', 'oppugner', 'nucleonics'], 4, print_progress)
          ID: 4 Progress: 0.5714285714285714
          0.5714285714285714
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress(['unconjecturable'], ['unconjecturable', 'lithontriptor', 'paradoctor', 'retinopapilitis'], 61, print_progress)
          ID: 61 Progress: 0.25
          0.25
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress([], ['liminary'], 85, print_progress)
          ID: 85 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress(['stuporose', 'didst', 'hexactinellidan'], ['stuporose', 'didst', 'hexactinellidan', 'vacuome', 'pulicarious', 'semidead', 'gourdlike'], 91, print_progress)
          ID: 91 Progress: 0.42857142857142855
          0.42857142857142855
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress(['tsu/RdAtiony', 'piddler', 'unbatten', 'bemar'], ['surdation', 'piddler', 'unbatten', 'bemar', 'unfeeling'], 30, print_progress)
          ID: 30 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress([], ['undersweep', 'sportswomanly', 'nonlocal', 'lorate', 'histopathologist'], 87, print_progress)
          ID: 87 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress([], ['rewarehouse'], 53, print_progress)
          ID: 53 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress([], ['noologist'], 70, print_progress)
          ID: 70 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress(['mockernut'], ['mockernut', 'boga', 'unzephyrlike', 'infragenual', 'dimmed', 'derelictness'], 71, print_progress)
          ID: 71 Progress: 0.16666666666666666
          0.16666666666666666
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress([], ['parapteron'], 12, print_progress)
          ID: 12 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress(['priesteen'], ['priesteen', 'parapet', 'linenman', 'noneffervescent', 'metasaccharinic', 'unreversible'], 86, print_progress)
          ID: 86 Progress: 0.16666666666666666
          0.16666666666666666
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress([], ['pulpit', 'cig', 'orbitelarian', 'overstress'], 51, print_progress)
          ID: 51 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress([], ['underdevelop', 'rejumble', 'crowkeeper', 'symphyllous'], 84, print_progress)
          ID: 84 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress(['phonogrammically'], ['phonogrammically', 'dumpiness', 'preambition'], 68, print_progress)
          ID: 68 Progress: 0.3333333333333333
          0.3333333333333333
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress(['block', 'diluvialist', 'herIOt'], ['block', 'diluvialist', 'heriot', 'supersalient', 'hate'], 80, print_progress)
          ID: 80 Progress: 0.4
          0.4
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress(['cyclose', 'acrospore', 'raver', 'balzarine', 'neomorphic'], ['cyclose', 'acrospore', 'raver', 'balzarine', 'neomorphic', 'lute', 'uranostaphylorrhaphy'], 65, print_progress)
          ID: 65 Progress: 0.7142857142857143
          0.7142857142857143
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress([], ['pedestal'], 81, print_progress)
          ID: 81 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress(['gynospore'], ['gynospore', 'apodictically', 'villages', 'algebra', 'uprid', 'disadvise', 'yourselves', 'nondeference'], 36, print_progress)
          ID: 36 Progress: 0.125
          0.125
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress([], ['lipomyxoma'], 11, print_progress)
          ID: 11 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress(['unchangefulness', 'sublevation', 'protosyntonose', 'saddlelike'], ['unchangefulness', 'sublevation', 'protosyntonose', 'saddlelike', 'postlachrymal'], 84, print_progress)
          ID: 84 Progress: 0.8
          0.8
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress([], ['coccygeal', 'dinothere', 'faradmeter', 'oversubtlety', 'dispensatorily'], 69, print_progress)
          ID: 69 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress([], ['diactin', 'stirps', 'waverous', 'qualifying', 'sexuparous'], 88, print_progress)
          ID: 88 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress(['headliner'], ['headliner', 'dutiability', 'acquired', 'portfire', 'dilatometric'], 6, print_progress)
          ID: 6 Progress: 0.2
          0.2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress([], ['healsome', 'proceed', 'oxhorn', 'overskim', 'polemicist', 'injure', 'hygrophaneity'], 35, print_progress)
          ID: 35 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress(['schemist'], ['schemist', 'pentahedrous', 'relativeness', 'solivagant', 'gloriously'], 87, print_progress)
          ID: 87 Progress: 0.2
          0.2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress(['carbonization'], ['carbonization', 'micropegmatitic', 'waterhorse', 'antisubstance', 'yucker', 'samely'], 37, print_progress)
          ID: 37 Progress: 0.16666666666666666
          0.16666666666666666
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress(['unguidable', 'presentational'], ['unguidable', 'presentational', 'autoheterosis'], 25, print_progress)
          ID: 25 Progress: 0.6666666666666666
          0.6666666666666666
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress([], ['predative'], 23, print_progress)
          ID: 23 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress([], ['ripe'], 99, print_progress)
          ID: 99 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress(['appliable', 'dysepulotic'], ['appliable', 'dysepulotic', 'opodeldoc'], 42, print_progress)
          ID: 42 Progress: 0.6666666666666666
          0.6666666666666666
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress(['ameed'], ['ameed', 'pneumonopleuritis'], 11, print_progress)
          ID: 11 Progress: 0.5
          0.5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress(['broomwoOd'], ['broomwood', 'relatability', 'pearlite', 'epithecium'], 84, print_progress)
          ID: 84 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress([], ['housewarming', 'hymenean', 'crepusculine', 'solecizer'], 51, print_progress)
          ID: 51 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress(['paradisicX'], ['paradisic', 'unaffectionately', 'exordial', 'weaponshowing', 'rhombohedra'], 68, print_progress)
          ID: 68 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress(['official'], ['official', 'platybrachycephalous', 'pitometer', 'electrodepositor'], 21, print_progress)
          ID: 21 Progress: 0.25
          0.25
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress(['hoseless'], ['hoseless', 'passivity', 'sparrowcide'], 91, print_progress)
          ID: 91 Progress: 0.3333333333333333
          0.3333333333333333
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress([], ['mischieve', 'dayfly'], 28, print_progress)
          ID: 28 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress(['notoriety'], ['notoriety', 'undersorcerer', 'pneumoperitonitis', 'balaenoidean', 'strawbreadth', 'postconnubial'], 99, print_progress)
          ID: 99 Progress: 0.16666666666666666
          0.16666666666666666
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress(['wold', 'relieved', 'quicksandy', 'guaraguao', 'stalkless'], ['wold', 'relieved', 'quicksandy', 'guaraguao', 'stalkless', 'unexhilarated'], 1, print_progress)
          ID: 1 Progress: 0.8333333333333334
          0.8333333333333334
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress(['unpermeated'], ['unpermeated', 'myelocytic', 'nonindictable', 'pretuberculous', 'mesoxalyl', 'strombite', 'muscule'], 9, print_progress)
          ID: 9 Progress: 0.14285714285714285
          0.14285714285714285
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress(['embrail', 'ferryboat', 'picky', 'wheerikins', 'uncrushed', 'monotelephone', 'foist'], ['embrail', 'ferryboat', 'picky', 'wheerikins', 'uncrushed', 'monotelephone', 'foist', 'transempirical'], 34, print_progress)
          ID: 34 Progress: 0.875
          0.875
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress(['imitationist', 'undershut'], ['imitationist', 'undershut', 'unmannerly', 'sterneber', 'nonappendicular', 'cityish'], 53, print_progress)
          ID: 53 Progress: 0.3333333333333333
          0.3333333333333333
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress(["Rhoo'Kers^M", 'gardenmaker', 'LpoStnA|talx'], ['hookers', 'gardenmaker', 'postnatal', 'private'], 66, print_progress)
          ID: 66 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress([], ['baillone', 'uncoacted', 'tarnisher', 'unwrinkled', 'pistareen', 'phacometer', 'aphyllous', 'thoraciform'], 71, print_progress)
          ID: 71 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress([], ['unsloped'], 7, print_progress)
          ID: 7 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress([], ['fracted', 'traducianistic', 'tinwork', 'vortically', 'massicot', 'pinite', 'barbarian'], 57, print_progress)
          ID: 57 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress(['angelhood', 'xiphydriid', 'longicorn', 'shadchan'], ['angelhood', 'xiphydriid', 'longicorn', 'shadchan', 'mixableness'], 20, print_progress)
          ID: 20 Progress: 0.8
          0.8
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress(['cervicectomy'], ['cervicectomy', 'vibraculoid', 'feminility', 'voluminously', 'hydroferrocyanate', 'canthotomy', 'unequableness'], 87, print_progress)
          ID: 87 Progress: 0.14285714285714285
          0.14285714285714285
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress(['kymbalon', 'plastogamy', 'grumpily'], ['kymbalon', 'plastogamy', 'grumpily', 'tease', 'macrocytosis', 'planterdom'], 64, print_progress)
          ID: 64 Progress: 0.5
          0.5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress(['overprovidently'], ['overprovidently', 'obdormition', 'precollect'], 42, print_progress)
          ID: 42 Progress: 0.3333333333333333
          0.3333333333333333
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress(['baker', 'circumscribaBLeg'], ['baker', 'circumscribable', 'apostrophic'], 90, print_progress)
          ID: 90 Progress: 0.3333333333333333
          0.3333333333333333
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress(['tractioneering'], ['tractioneering', 'contestant'], 40, print_progress)
          ID: 40 Progress: 0.5
          0.5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress([], ['afterturn'], 56, print_progress)
          ID: 56 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress([], ['subjectiveness'], 68, print_progress)
          ID: 68 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress([], ['ophiophagous', 'rice', 'piousness', 'vibrissae'], 9, print_progress)
          ID: 9 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress([], ['civicism', 'belletrist', 'vegetocarbonaceous', 'woodchuck', 'phacitis', 'warehouseful'], 9, print_progress)
          ID: 9 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress(['longboat', 'cataria', 'VpectinationU', 'immute', 'dicrotic'], ['longboat', 'cataria', 'pectination', 'immute', 'dicrotic', 'tressured', 'sluggard', 'hypothenal'], 50, print_progress)
          ID: 50 Progress: 0.25
          0.25
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress(['discover', 'fixative'], ['discover', 'fixative', 'suprasphanoidal'], 8, print_progress)
          ID: 8 Progress: 0.6666666666666666
          0.6666666666666666
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress(['unharnessed'], ['unharnessed', 'fruitist'], 58, print_progress)
          ID: 58 Progress: 0.5
          0.5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress([], ['tom', 'spurgall'], 93, print_progress)
          ID: 93 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress([], ['bronze', 'turgidness', 'untailorly'], 58, print_progress)
          ID: 58 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress([], ['gong', 'spondylium', 'agrammatism', 'yad', 'unintrusted'], 77, print_progress)
          ID: 77 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress(['tegularly'], ['tegularly', 'kilnrib'], 22, print_progress)
          ID: 22 Progress: 0.5
          0.5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress(['succeed', 'dumminess'], ['succeed', 'dumminess', 'tedder', 'bobsleigh', 'tenendum', 'slatternness'], 7, print_progress)
          ID: 7 Progress: 0.3333333333333333
          0.3333333333333333
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress(['biventer'], ['biventer', 'fugle', 'estimated', 'racinglike'], 66, print_progress)
          ID: 66 Progress: 0.25
          0.25
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress([], ['imbonity', 'axolemma', 'comendite'], 51, print_progress)
          ID: 51 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress([], ['carpeting', 'equitriangular', 'unforgeability', 'antiharmonist'], 71, print_progress)
          ID: 71 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> report_progress([], ['autoimmunization'], 57, print_progress)
          ID: 57 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from cats import report_progress
      >>> print_progress = lambda d: print('ID:', d['id'], 'Progress:', d['progress'])
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
