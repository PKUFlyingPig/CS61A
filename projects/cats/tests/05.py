test = {
  'name': 'Problem 5',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> abs_diff = lambda w1, w2, limit: abs(len(w2) - len(w1))
          >>> autocorrect("cul", ["culture", "cult", "cultivate"], abs_diff, 10)
          'cult'
          >>> autocorrect("cul", ["culture", "cult", "cultivate"], abs_diff, 0)
          'cul'
          >>> autocorrect("wor", ["worry", "car", "part"], abs_diff, 10)
          'car'
          >>> first_diff = lambda w1, w2, limit: 1 if w1[0] != w2[0] else 0
          >>> autocorrect("wrod", ["word", "rod"], first_diff, 1)
          'word'
          >>> autocorrect("inside", ["idea", "inside"], first_diff, 0.5)
          'inside'
          >>> autocorrect("inside", ["idea", "insider"], first_diff, 0.5)
          'idea'
          >>> autocorrect("outside", ["idea", "insider"], first_diff, 0.5)
          'outside'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> matching_diff = lambda w1, w2, limit: sum([w1[i] != w2[i] for i in range(min(len(w1), len(w2)))]) # Num matching chars
          >>> autocorrect("tosting", ["testing", "asking", "fasting"], matching_diff, 10)
          'testing'
          >>> autocorrect("tsting", ["testing", "rowing"], matching_diff, 10)
          'rowing'
          >>> autocorrect("bwe", ["awe", "bye"], matching_diff, 10)
          'awe'
          >>> autocorrect("bwe", ["bye", "awe"], matching_diff, 10)
          'bye'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> words_list = sorted(lines_from_file('data/words.txt')[:10000])
          >>> autocorrect("testng", words_list, lambda w1, w2, limit: 1, 10)
          'a'
          >>> autocorrect("testing", words_list, lambda w1, w2, limit: 1, 10)
          'testing'
          >>> autocorrect("gesting", words_list, lambda w1, w2, limit: sum([w1[i] != w2[i] for i in range(min(len(w1), len(w2)))]) + abs(len(w1) - len(w2)), 10)
          'getting'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('statutably', ['statutably'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 5)
          'statutably'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('ascetically', ['mennom', 'foreannouncement', 'neomorph', 'artemisic', 'pyrazole', 'sublicense', 'pinchem', 'spiculation', 'boreal', 'semitrimmed'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 8)
          'spiculation'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('gregariously', ['saccharate', 'hermeneutic', 'butanal', 'gregariously', 'splenopexy', 'demolitionary', 'budder'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 8)
          'gregariously'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('fluor', ['nonnaturality'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 1)
          'fluor'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('werefolk', ['supersulcus', 'theorematically', 'dosiology', 'rotundness', 'raash', 'perule', 'untrekked', 'musophagine'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 0)
          'werefolk'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('osmotactic', ['rhopalium', 'saxten', 'transitively', 'retardive', 'emprise', 'marmatite', 'unlivery', 'ultimata'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 0)
          'osmotactic'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('limpin', ['wowserism', 'convictively', 'prepromote', 'amphictyonian', 'reverence', 'unemitted'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 2)
          'limpin'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('delabialize', ['delabialize', 'erythematous', 'gossipdom', 'killinite', 'osteochondropathy', 'tethydan', 'exhibitional'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 9)
          'delabialize'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('cathepsin', ['elasticness', 'polony', 'spoke', 'unshaded', 'uncognoscibility', 'preimportation', 'unthickened', 'constructorship', 'brombenzamide', 'cathepsin'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 1)
          'cathepsin'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('nebularization', ['iambi', 'heterology', 'dorsiflexion', 'depasturable', 'megalophonic', 'unsubvertive', 'bankrupture'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 1)
          'nebularization'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('lycanthropic', ['inkhornizer'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 4)
          'inkhornizer'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('miriness', ['eheu', 'aqueousness', 'loveworthy', 'showish', 'balut', 'cibation', 'pride', 'septuor'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 1)
          'cibation'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('ectodactylism', ['unowed', 'overslaugh', 'unshriveled'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 1)
          'ectodactylism'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('wringstaff', ['scleromeninx'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 0)
          'wringstaff'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('zygostyle', ['conchiferous', 'zygostyle', 'glottidean', 'temulentive', 'khajur', 'chirognomy', 'obitual', 'unfelicitousness'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 6)
          'zygostyle'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('blown', ['subjacency', 'looplike', 'nasoethmoidal', 'capcase', 'communicableness', 'blown'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 5)
          'blown'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('autocatalyze', ['sulpholysis', 'kalo', 'cecidiology', 'progne', 'cosiness', 'quotity'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 9)
          'sulpholysis'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('stichomancy', ['cnidophore', 'orrery', 'bargham', 'iridentropium', 'nickelous', 'cedarbird', 'grandpaternal'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 6)
          'cnidophore'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('prolyl', ['distortional', 'rotaliiform', 'permissive', 'posthemiplegic'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 3)
          'prolyl'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('antemeridian', ['wistful', 'scorbutic', 'chichipe'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 5)
          'scorbutic'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('uninventibleness', ['mudless', 'bromism', 'uneffused', 'waterhead', 'misbelieve', 'gelatined', 'bilk', 'heresy', 'hause'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 4)
          'uninventibleness'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('energeia', ['hamated', 'encumberingly', 'closh', 'yugada', 'staphyloptosis'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 8)
          'hamated'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('betanglement', ['orthopraxis', 'marina', 'gourmet', 'democrats', 'thirsting'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 6)
          'orthopraxis'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('actification', ['laconicum', 'shilpit', 'intercrust'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 1)
          'actification'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('strongheadedness', ['circumvallate', 'sunset', 'dysgenesic'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 0)
          'strongheadedness'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('picul', ['noration', 'tinstuff', 'arpent', 'ketogen', 'picul', 'vitreosity', 'highman', 'expiree'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 6)
          'picul'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('disregardance', ['unprejudicedly'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 6)
          'unprejudicedly'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('intersuperciliary', ['moral', 'intersuperciliary', 'autoheterodyne', 'gypsywort', 'leiomyomatous', 'mercurialization', 'musing', 'balneography', 'clearhearted'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 8)
          'intersuperciliary'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('airt', ['electroreceptive', 'nonpoisonous', 'perth', 'chrematistic', 'proctotomy', 'bicetyl'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 9)
          'perth'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('neighborless', ['unqueried', 'incedingly', 'sudiform'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 3)
          'incedingly'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('meliorist', ['contralto', 'erythematous', 'intromissive', 'tanglement', 'priest'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 5)
          'contralto'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('assimilatory', ['enkindle', 'infections', 'hydrotherapeutic', 'unmilled', 'biotic'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 1)
          'assimilatory'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('shelfmate', ['nucleonics', 'reducer', 'watered', 'tableful', 'loveman', 'deem', 'mimical', 'inarticulacy', 'smeddum'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 6)
          'nucleonics'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('galluses', ['paradoctor', 'retinopapilitis', 'unabsolvedness', 'galluses', 'procuratorial', 'calycate', 'superannuate', 'sternite', 'calorescent'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 7)
          'galluses'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('chrysamminic', ['undeficient', 'haply', 'chancellery', 'ratiocinate', 'pasquinader', 'gamecube', 'externally'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 9)
          'undeficient'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('vacuome', ['didst', 'hexactinellidan'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 7)
          'didst'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('quinoid', ['piddler', 'unbatten', 'bemar', 'unfeeling', 'thermalgesia', 'stolonate', 'potash', 'gemmiparity', 'cuisine'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 2)
          'piddler'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('thieving', ['sportswomanly', 'nonlocal', 'lorate', 'histopathologist', 'trichiuroid', 'thieving', 'melanocratic'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 5)
          'thieving'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('sagacity', ['undimerous', 'engrainedly', 'aschistic', 'nonpregnant'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 5)
          'aschistic'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('limitless', ['scorpioidal', 'noologist', 'borscht', 'spectator', 'semiperimetry', 'decider', 'impaler', 'jesse', 'multipinnate', 'steam'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 9)
          'noologist'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('invisibleness', ['unattackableness', 'chlorellaceous', 'dipolarization', 'unvoicing'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 0)
          'invisibleness'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('delegable', ['mamelonation', 'delegable', 'sunlight'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 3)
          'delegable'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('alcalde', ['schematonics'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 2)
          'alcalde'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('orbitelarian', ['orbitelarian', 'overstress'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 0)
          'orbitelarian'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('crowkeeper', ['rejumble', 'crowkeeper'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 3)
          'crowkeeper'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('dissympathize', ['corticous', 'rollichie', 'palmar', 'outbetter', 'pyrometamorphic', 'saxtie', 'auricularis', 'reputedly', 'custumal', 'cheecha'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 0)
          'dissympathize'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('growthy', ['diluvialist', 'heriot', 'supersalient', 'hate', 'septation', 'nitriding', 'declared', 'supersaturate', 'autodidact'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 5)
          'heriot'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('lung', ['coronion', 'permutableness'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 2)
          'lung'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('colchicine', ['colchicine', 'zincographical'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 3)
          'colchicine'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('wishedly', ['gravitater', 'adipopexia', 'djerib', 'bather'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 1)
          'wishedly'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('dogmaticalness', ['dogmaticalness', 'obstupefy'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 0)
          'dogmaticalness'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('amphicarpogenous', ['overbitter'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 3)
          'amphicarpogenous'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('ingot', ['dispensatorily', 'manganapatite', 'gatemaker', 'hydrosulphocyanic', 'drugshop', 'caracolite', 'unloosen'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 7)
          'drugshop'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('thutter', ['stirps', 'waverous', 'qualifying', 'sexuparous', 'realmless', 'wuzzle'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 5)
          'stirps'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('underaverage', ['portfire', 'dilatometric', 'voicelet', 'aggress', 'overmultitude', 'winder', 'splenolysis', 'unsumptuous'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 2)
          'dilatometric'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('compensating', ['proceed', 'oxhorn', 'overskim', 'polemicist', 'injure', 'hygrophaneity', 'chairmender', 'lacunae', 'diplococcal'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 7)
          'hygrophaneity'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('solivagant', ['relativeness'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 4)
          'relativeness'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('cynical', ['palpitate', 'supraoesophageal'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 0)
          'cynical'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('revivement', ['nitrophytic', 'restrainedness', 'revivement', 'tron', 'interpretably', 'runkly', 'ninebark', 'coemptor', 'bolete', 'larmier'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 7)
          'revivement'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('esuriently', ['nonprofession', 'mojarra', 'ophionine', 'goadster', 'nonappearer', 'accompanimental'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 7)
          'ophionine'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('hyalinization', ['ripe', 'spatuliform', 'serpent', 'truantship', 'epicrystalline', 'endosteitis', 'shark'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 1)
          'epicrystalline'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('hypnosporangium', ['spondean', 'farmership', 'pharmuthi'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 0)
          'hypnosporangium'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('attractiveness', ['phthisipneumony', 'transnature'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 0)
          'attractiveness'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('actinomere', ['pearlite', 'epithecium', 'saddlenose', 'underbeam', 'labyrinthal', 'actinomere', 'collyrite', 'mythopoem'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 4)
          'actinomere'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('autohypnotization', ['crepusculine', 'solecizer', 'overfearful', 'cigar', 'veal', 'gnomonics', 'autohypnotization', 'theopneustic'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 6)
          'autohypnotization'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('grad', ['lighthouse', 'traversewise', 'necessist', 'kinesiology', 'coetaneousness'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 1)
          'grad'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('superambitious', ['electrodepositor', 'superambitious', 'phalacrocoracine', 'taxeme'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 7)
          'superambitious'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('croisette', ['salubrious', 'untactful', 'kava', 'japanese', 'unennobling', 'ungreased', 'enterocinesia', 'pharyngemphraxis'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 5)
          'untactful'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('prionodont', ['rattlebrain', 'unconcertedly', 'pronephridiostome', 'soredioid'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 0)
          'prionodont'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('archiepiscopal', ['bavary'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 5)
          'archiepiscopal'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('franc', ['fanciless'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 0)
          'franc'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('spastically', ['myelocytic', 'nonindictable', 'pretuberculous', 'mesoxalyl', 'strombite', 'muscule', 'cheesemongerly', 'unformularize', 'noninfected'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 7)
          'noninfected'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('choreographical', ['uncrushed', 'monotelephone', 'foist', 'transempirical', 'gawkily', 'choreographical'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 3)
          'choreographical'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('nonappendicular', ['sterneber'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 2)
          'nonappendicular'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('hermaphroditical', ['occluse', 'ramentaceous', 'rhonchus', 'lusterless', 'bewitchingly'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 0)
          'hermaphroditical'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('pistareen', ['tarnisher', 'unwrinkled', 'pistareen', 'phacometer'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 0)
          'pistareen'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('tarmac', ['simile', 'raphis', 'untriable', 'japan', 'overfold', 'perviousness', 'parliamentarism', 'intrathecal'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 7)
          'simile'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('scarabee', ['pinite', 'barbarian', 'shank', 'metadiorite', 'scarabee', 'artificership'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 4)
          'scarabee'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('underlap', ['xiphydriid', 'longicorn', 'shadchan', 'mixableness', 'journals', 'voltaic', 'homiletic', 'declinate'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 6)
          'shadchan'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('dottler', ['hydroferrocyanate', 'canthotomy', 'unequableness', 'monomerous', 'assiduously'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 3)
          'canthotomy'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('macrocytosis', ['plastogamy', 'grumpily', 'tease', 'macrocytosis'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 6)
          'macrocytosis'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('stenocrotaphia', ['european', 'instantly', 'draughts', 'skewings'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 8)
          'instantly'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('postpubertal', ['incomprehensibility', 'fole', 'nerviness', 'velvetry', 'coextensively', 'prepotency', 'ness', 'undetrimental'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 0)
          'postpubertal'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('outwrangle', ['angiotripsy'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 0)
          'outwrangle'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('maltreat', ['breathlessness'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 0)
          'maltreat'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('myohematin', ['myristic', 'yoicks', 'filcher', 'caddle', 'annexa'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 0)
          'myohematin'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('clithral', ['diplocardiac', 'enwind', 'clithral', 'tarworks'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 0)
          'clithral'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('impishly', ['paryphodrome', 'fratricide', 'unfeignedness', 'issueless', 'henad', 'unprettiness', 'mycohaemia', 'vacillation', 'bagattini'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 0)
          'impishly'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('dicrotic', ['immute', 'dicrotic'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 0)
          'dicrotic'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('catelectrotonic', ['sharpish', 'mashy'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 6)
          'catelectrotonic'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('chondrosin', ['resolicit', 'gangsman', 'tailorize', 'pluriseriate'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 2)
          'resolicit'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('telophase', ['thymy', 'unnobly', 'cephalometric', 'louty', 'granulet', 'surly', 'mysophobia'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 0)
          'telophase'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('planoorbicular', ['turgidness', 'untailorly', 'untewed'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 3)
          'planoorbicular'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('depository', ['yad', 'unintrusted', 'nosy', 'unguinous', 'pachydermia', 'plainsoled', 'nonbleeding', 'protosalt', 'unnoticeable'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 4)
          'plainsoled'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('semivulcanized', ['sulphonalism', 'indignly', 'phylogeny', 'indicial', 'tepidarium', 'expansible'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 0)
          'semivulcanized'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('hypocotylous', ['cord', 'longbow', 'heterodontism', 'alisier', 'duskingtide', 'eugenically', 'inequality', 'heatful'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 0)
          'hypocotylous'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('cooing', ['clavelization', 'cooing', 'pedestrian', 'laryngoscleroma', 'primiparity'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 6)
          'cooing'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('rafflesia', ['toilsomeness', 'enantioblastic'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 0)
          'rafflesia'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('nunky', ['washproof', 'soullessly'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 0)
          'nunky'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect('multicuspidate', ['semiprofessional', 'diplomatist', 'hucksteress', 'autoreinfusion', 'emollient', 'apoxesis', 'entelam', 'oathworthy', 'anaplasty', 'potator'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 3)
          'autoreinfusion'
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from cats import autocorrect, lines_from_file
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
