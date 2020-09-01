test = {
  'name': 'Problem 9',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> p = [[1, 4, 6, 7], [0, 4, 6, 9]]
          >>> words = ['This', 'is', 'fun']
          >>> game = time_per_word(p, words)
          >>> all_words(game)
          ['This', 'is', 'fun']
          >>> all_times(game)
          [[3, 2, 1], [4, 2, 3]]
          >>> p = [[0, 2, 3], [2, 4, 7]]
          >>> game = time_per_word(p, ['hello', 'world'])
          >>> word_at(game, 1)
          'world'
          >>> all_times(game)
          [[2, 1], [2, 3]]
          >>> time(game, 0, 1)
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[83, 86, 87, 92, 94], [21, 26, 27, 30, 31]]
          >>> game = time_per_word(p, ['colliquativeness', 'soshed', 'neurine', 'statutably'])
          >>> all_words(game)
          ['colliquativeness', 'soshed', 'neurine', 'statutably']
          >>> all_times(game)
          [[3, 1, 5, 2], [5, 1, 3, 1]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[16, 18, 23, 28, 30, 33]]
          >>> game = time_per_word(p, ['unsimilar', 'conditioning', 'crystallogenical', 'mennom', 'foreannouncement'])
          >>> all_words(game)
          ['unsimilar', 'conditioning', 'crystallogenical', 'mennom', 'foreannouncement']
          >>> all_times(game)
          [[2, 5, 5, 2, 3]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[72], [22]]
          >>> game = time_per_word(p, [])
          >>> all_words(game)
          []
          >>> all_times(game)
          [[], []]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[72, 73, 77]]
          >>> game = time_per_word(p, ['unceasingness', 'gendarme'])
          >>> all_words(game)
          ['unceasingness', 'gendarme']
          >>> all_times(game)
          [[1, 4]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[87, 90, 93], [72, 74, 79]]
          >>> game = time_per_word(p, ['unliquidated', 'multivoltine'])
          >>> all_words(game)
          ['unliquidated', 'multivoltine']
          >>> all_times(game)
          [[3, 3], [2, 5]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[16, 21, 22, 23], [73, 77, 82, 86], [8, 9, 11, 16]]
          >>> game = time_per_word(p, ['antimonarchial', 'archaeology', 'oopod'])
          >>> all_words(game)
          ['antimonarchial', 'archaeology', 'oopod']
          >>> all_times(game)
          [[5, 1, 1], [4, 5, 4], [1, 2, 5]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[79, 82, 83]]
          >>> game = time_per_word(p, ['nehiloth', 'cisplatine'])
          >>> all_words(game)
          ['nehiloth', 'cisplatine']
          >>> all_times(game)
          [[3, 1]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[57, 58, 60, 63, 66]]
          >>> game = time_per_word(p, ['croup', 'accompaniment', 'delabialize', 'erythematous'])
          >>> all_words(game)
          ['croup', 'accompaniment', 'delabialize', 'erythematous']
          >>> all_times(game)
          [[1, 2, 3, 3]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[83, 84, 85, 90]]
          >>> game = time_per_word(p, ['basidiolichen', 'pruriently', 'elasticness'])
          >>> all_words(game)
          ['basidiolichen', 'pruriently', 'elasticness']
          >>> all_times(game)
          [[1, 1, 5]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[65, 69, 71, 73, 78, 81, 86], [22, 23, 24, 29, 33, 34, 35], [52, 55, 59, 60, 61, 64, 69]]
          >>> game = time_per_word(p, ['homotypical', 'temporomandibular', 'unannexed', 'umbellar', 'rambutan', 'southeasternmost'])
          >>> all_words(game)
          ['homotypical', 'temporomandibular', 'unannexed', 'umbellar', 'rambutan', 'southeasternmost']
          >>> all_times(game)
          [[4, 2, 2, 5, 3, 5], [1, 1, 5, 4, 1, 1], [3, 4, 1, 1, 3, 5]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[28, 30]]
          >>> game = time_per_word(p, ['intercreate'])
          >>> all_words(game)
          ['intercreate']
          >>> all_times(game)
          [[2]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[91, 93]]
          >>> game = time_per_word(p, ['cashable'])
          >>> all_words(game)
          ['cashable']
          >>> all_times(game)
          [[2]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[48, 50, 55, 57]]
          >>> game = time_per_word(p, ['pulicidal', 'choultry', 'caryopilite'])
          >>> all_words(game)
          ['pulicidal', 'choultry', 'caryopilite']
          >>> all_times(game)
          [[2, 5, 2]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[25, 30, 33]]
          >>> game = time_per_word(p, ['stowbordman', 'scleromeninx'])
          >>> all_words(game)
          ['stowbordman', 'scleromeninx']
          >>> all_times(game)
          [[5, 3]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[28, 29, 32, 36], [10, 11, 13, 14]]
          >>> game = time_per_word(p, ['gonfalonierate', 'plumbosolvent', 'nearby'])
          >>> all_words(game)
          ['gonfalonierate', 'plumbosolvent', 'nearby']
          >>> all_times(game)
          [[1, 3, 4], [1, 2, 1]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[12], [5]]
          >>> game = time_per_word(p, [])
          >>> all_words(game)
          []
          >>> all_times(game)
          [[], []]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[65, 70], [68, 70]]
          >>> game = time_per_word(p, ['pauldron'])
          >>> all_words(game)
          ['pauldron']
          >>> all_times(game)
          [[5], [2]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[22, 27], [57, 62], [45, 50]]
          >>> game = time_per_word(p, ['cameograph'])
          >>> all_words(game)
          ['cameograph']
          >>> all_times(game)
          [[5], [5], [5]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[62, 65, 66], [49, 52, 53]]
          >>> game = time_per_word(p, ['intent', 'inadequateness'])
          >>> all_words(game)
          ['intent', 'inadequateness']
          >>> all_times(game)
          [[3, 1], [3, 1]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[74, 77, 78, 81, 83, 86]]
          >>> game = time_per_word(p, ['unrefined', 'havent', 'kilneye', 'wistful', 'scorbutic'])
          >>> all_words(game)
          ['unrefined', 'havent', 'kilneye', 'wistful', 'scorbutic']
          >>> all_times(game)
          [[3, 1, 3, 2, 3]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[90, 92, 97, 101]]
          >>> game = time_per_word(p, ['inefficacity', 'caulicule', 'autositic'])
          >>> all_words(game)
          ['inefficacity', 'caulicule', 'autositic']
          >>> all_times(game)
          [[2, 5, 4]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[4, 5]]
          >>> game = time_per_word(p, ['fewtrils'])
          >>> all_words(game)
          ['fewtrils']
          >>> all_times(game)
          [[1]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[8, 13, 16, 21, 22, 25]]
          >>> game = time_per_word(p, ['saltless', 'bailage', 'nonformation', 'yeven', 'argenteous'])
          >>> all_words(game)
          ['saltless', 'bailage', 'nonformation', 'yeven', 'argenteous']
          >>> all_times(game)
          [[5, 3, 5, 1, 3]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[31, 36, 40, 43]]
          >>> game = time_per_word(p, ['overcrop', 'julian', 'gaub'])
          >>> all_words(game)
          ['overcrop', 'julian', 'gaub']
          >>> all_times(game)
          [[5, 4, 3]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[17, 22, 27], [1, 5, 9]]
          >>> game = time_per_word(p, ['construction', 'upbid'])
          >>> all_words(game)
          ['construction', 'upbid']
          >>> all_times(game)
          [[5, 5], [4, 4]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[23, 24, 26, 30, 35], [44, 49, 54, 55, 59], [50, 55, 57, 61, 63]]
          >>> game = time_per_word(p, ['immortalness', 'powell', 'indifferently', 'palatograph'])
          >>> all_words(game)
          ['immortalness', 'powell', 'indifferently', 'palatograph']
          >>> all_times(game)
          [[1, 2, 4, 5], [5, 5, 1, 4], [5, 2, 4, 2]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[90, 95, 97, 99, 100, 104], [32, 35, 39, 44, 47, 48]]
          >>> game = time_per_word(p, ['rorqual', 'tautomeric', 'unprejudicedly', 'disregardance', 'reconveyance'])
          >>> all_words(game)
          ['rorqual', 'tautomeric', 'unprejudicedly', 'disregardance', 'reconveyance']
          >>> all_times(game)
          [[5, 2, 2, 1, 4], [3, 4, 5, 3, 1]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[37, 38, 40, 42]]
          >>> game = time_per_word(p, ['nightstock', 'catabaptist', 'aloud'])
          >>> all_words(game)
          ['nightstock', 'catabaptist', 'aloud']
          >>> all_times(game)
          [[1, 2, 2]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[22, 26], [32, 37]]
          >>> game = time_per_word(p, ['understrain'])
          >>> all_words(game)
          ['understrain']
          >>> all_times(game)
          [[4], [5]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[83, 84, 88, 93, 98, 101], [97, 99, 103, 104, 107, 111]]
          >>> game = time_per_word(p, ['accompliceship', 'dumpish', 'unqueried', 'incedingly', 'sudiform'])
          >>> all_words(game)
          ['accompliceship', 'dumpish', 'unqueried', 'incedingly', 'sudiform']
          >>> all_times(game)
          [[1, 4, 5, 5, 3], [2, 4, 1, 3, 4]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[53, 57, 59, 62, 67, 68], [17, 19, 23, 28, 29, 33], [46, 48, 51, 56, 60, 65]]
          >>> game = time_per_word(p, ['undishonored', 'counterflange', 'justly', 'contralto', 'erythematous'])
          >>> all_words(game)
          ['undishonored', 'counterflange', 'justly', 'contralto', 'erythematous']
          >>> all_times(game)
          [[4, 2, 3, 5, 1], [2, 4, 5, 1, 4], [2, 3, 5, 4, 5]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[23, 28, 31], [58, 63, 66], [28, 31, 34]]
          >>> game = time_per_word(p, ['replier', 'bending'])
          >>> all_words(game)
          ['replier', 'bending']
          >>> all_times(game)
          [[5, 3], [5, 3], [3, 3]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[88, 90, 92, 94], [19, 23, 28, 32], [71, 74, 78, 80]]
          >>> game = time_per_word(p, ['pandemy', 'fruited', 'draughtmanship'])
          >>> all_words(game)
          ['pandemy', 'fruited', 'draughtmanship']
          >>> all_times(game)
          [[2, 2, 2], [4, 5, 4], [3, 4, 2]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[67, 71, 74, 76, 79], [61, 66, 70, 75, 80]]
          >>> game = time_per_word(p, ['unconjecturable', 'lithontriptor', 'paradoctor', 'retinopapilitis'])
          >>> all_words(game)
          ['unconjecturable', 'lithontriptor', 'paradoctor', 'retinopapilitis']
          >>> all_times(game)
          [[4, 3, 2, 3], [5, 4, 5, 5]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[85, 89], [68, 71], [35, 38]]
          >>> game = time_per_word(p, ['liminary'])
          >>> all_words(game)
          ['liminary']
          >>> all_times(game)
          [[4], [3], [3]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[55, 57]]
          >>> game = time_per_word(p, ['myelencephalous'])
          >>> all_words(game)
          ['myelencephalous']
          >>> all_times(game)
          [[2]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[55, 60, 64, 66, 71, 75], [6, 7, 9, 14, 19, 23]]
          >>> game = time_per_word(p, ['surdation', 'piddler', 'unbatten', 'bemar', 'unfeeling'])
          >>> all_words(game)
          ['surdation', 'piddler', 'unbatten', 'bemar', 'unfeeling']
          >>> all_times(game)
          [[5, 4, 2, 5, 4], [1, 2, 5, 5, 4]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[22, 26, 27, 28], [35, 38, 39, 43]]
          >>> game = time_per_word(p, ['unmunched', 'sabered', 'unbattered'])
          >>> all_words(game)
          ['unmunched', 'sabered', 'unbattered']
          >>> all_times(game)
          [[4, 1, 1], [3, 1, 4]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[83, 88], [60, 63]]
          >>> game = time_per_word(p, ['rewarehouse'])
          >>> all_words(game)
          ['rewarehouse']
          >>> all_times(game)
          [[5], [3]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[20, 24]]
          >>> game = time_per_word(p, ['unidigitate'])
          >>> all_words(game)
          ['unidigitate']
          >>> all_times(game)
          [[4]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[12, 15, 18, 22, 24, 26, 27], [71, 75, 79, 83, 84, 86, 91]]
          >>> game = time_per_word(p, ['mockernut', 'boga', 'unzephyrlike', 'infragenual', 'dimmed', 'derelictness'])
          >>> all_words(game)
          ['mockernut', 'boga', 'unzephyrlike', 'infragenual', 'dimmed', 'derelictness']
          >>> all_times(game)
          [[3, 3, 4, 2, 2, 1], [4, 4, 4, 1, 2, 5]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[98]]
          >>> game = time_per_word(p, [])
          >>> all_words(game)
          []
          >>> all_times(game)
          [[]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[82, 85, 88, 92, 97, 99, 100], [86, 91, 96, 98, 99, 104, 105], [74, 78, 80, 84, 88, 92, 95]]
          >>> game = time_per_word(p, ['priesteen', 'parapet', 'linenman', 'noneffervescent', 'metasaccharinic', 'unreversible'])
          >>> all_words(game)
          ['priesteen', 'parapet', 'linenman', 'noneffervescent', 'metasaccharinic', 'unreversible']
          >>> all_times(game)
          [[3, 3, 4, 5, 2, 1], [5, 5, 2, 1, 5, 1], [4, 2, 4, 4, 4, 3]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[51, 53, 57, 61, 64]]
          >>> game = time_per_word(p, ['pulpit', 'cig', 'orbitelarian', 'overstress'])
          >>> all_words(game)
          ['pulpit', 'cig', 'orbitelarian', 'overstress']
          >>> all_times(game)
          [[2, 4, 4, 3]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[84, 88, 91, 92, 94]]
          >>> game = time_per_word(p, ['underdevelop', 'rejumble', 'crowkeeper', 'symphyllous'])
          >>> all_words(game)
          ['underdevelop', 'rejumble', 'crowkeeper', 'symphyllous']
          >>> all_times(game)
          [[4, 3, 1, 2]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[95, 99, 104, 106]]
          >>> game = time_per_word(p, ['phraseological', 'tristfulness', 'phonogrammically'])
          >>> all_words(game)
          ['phraseological', 'tristfulness', 'phonogrammically']
          >>> all_times(game)
          [[4, 5, 2]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[75, 79, 82, 85, 88, 89], [93, 94, 95, 99, 102, 107], [60, 64, 65, 68, 69, 70]]
          >>> game = time_per_word(p, ['zenana', 'block', 'diluvialist', 'heriot', 'supersalient'])
          >>> all_words(game)
          ['zenana', 'block', 'diluvialist', 'heriot', 'supersalient']
          >>> all_times(game)
          [[4, 3, 3, 3, 1], [1, 1, 4, 3, 5], [4, 1, 3, 1, 1]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[55, 58, 62, 66, 67, 70, 72], [50, 53, 55, 60, 62, 64, 65]]
          >>> game = time_per_word(p, ['acrospore', 'raver', 'balzarine', 'neomorphic', 'lute', 'uranostaphylorrhaphy'])
          >>> all_words(game)
          ['acrospore', 'raver', 'balzarine', 'neomorphic', 'lute', 'uranostaphylorrhaphy']
          >>> all_times(game)
          [[3, 4, 4, 1, 3, 2], [3, 2, 5, 2, 2, 1]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[68], [91]]
          >>> game = time_per_word(p, [])
          >>> all_words(game)
          []
          >>> all_times(game)
          [[], []]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[12, 17, 22], [69, 71, 76], [5, 8, 9]]
          >>> game = time_per_word(p, ['tatting', 'gynospore'])
          >>> all_words(game)
          ['tatting', 'gynospore']
          >>> all_times(game)
          [[5, 5], [2, 5], [3, 1]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[11]]
          >>> game = time_per_word(p, [])
          >>> all_words(game)
          []
          >>> all_times(game)
          [[]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[94, 96, 101, 106, 110, 115, 120], [52, 55, 60, 65, 69, 72, 75]]
          >>> game = time_per_word(p, ['krait', 'proker', 'unchangefulness', 'sublevation', 'protosyntonose', 'saddlelike'])
          >>> all_words(game)
          ['krait', 'proker', 'unchangefulness', 'sublevation', 'protosyntonose', 'saddlelike']
          >>> all_times(game)
          [[2, 5, 5, 4, 5, 5], [3, 5, 5, 4, 3, 3]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[69, 72, 76, 80, 83, 87]]
          >>> game = time_per_word(p, ['coccygeal', 'dinothere', 'faradmeter', 'oversubtlety', 'dispensatorily'])
          >>> all_words(game)
          ['coccygeal', 'dinothere', 'faradmeter', 'oversubtlety', 'dispensatorily']
          >>> all_times(game)
          [[3, 4, 4, 3, 4]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[37, 42], [61, 62]]
          >>> game = time_per_word(p, ['thiswise'])
          >>> all_words(game)
          ['thiswise']
          >>> all_times(game)
          [[5], [1]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[9, 11, 16, 21, 22, 26], [6, 11, 16, 17, 19, 22]]
          >>> game = time_per_word(p, ['headliner', 'dutiability', 'acquired', 'portfire', 'dilatometric'])
          >>> all_words(game)
          ['headliner', 'dutiability', 'acquired', 'portfire', 'dilatometric']
          >>> all_times(game)
          [[2, 5, 5, 1, 4], [5, 5, 1, 2, 3]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[55, 59, 60, 65, 67, 71], [37, 39, 43, 44, 45, 48]]
          >>> game = time_per_word(p, ['jessica', 'ribaudequin', 'healsome', 'proceed', 'oxhorn'])
          >>> all_words(game)
          ['jessica', 'ribaudequin', 'healsome', 'proceed', 'oxhorn']
          >>> all_times(game)
          [[4, 1, 5, 2, 4], [2, 4, 1, 1, 3]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[87, 92, 95, 96, 99, 103], [22, 24, 26, 31, 35, 36]]
          >>> game = time_per_word(p, ['schemist', 'pentahedrous', 'relativeness', 'solivagant', 'gloriously'])
          >>> all_words(game)
          ['schemist', 'pentahedrous', 'relativeness', 'solivagant', 'gloriously']
          >>> all_times(game)
          [[5, 3, 1, 3, 4], [2, 2, 5, 4, 1]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[37, 41, 43, 45, 46, 51, 54], [72, 73, 76, 79, 81, 83, 84]]
          >>> game = time_per_word(p, ['carbonization', 'micropegmatitic', 'waterhorse', 'antisubstance', 'yucker', 'samely'])
          >>> all_words(game)
          ['carbonization', 'micropegmatitic', 'waterhorse', 'antisubstance', 'yucker', 'samely']
          >>> all_times(game)
          [[4, 2, 2, 1, 5, 3], [1, 3, 3, 2, 2, 1]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[21, 23, 28, 33], [35, 38, 43, 46], [25, 26, 29, 30]]
          >>> game = time_per_word(p, ['unguidable', 'presentational', 'autoheterosis'])
          >>> all_words(game)
          ['unguidable', 'presentational', 'autoheterosis']
          >>> all_times(game)
          [[2, 5, 5], [3, 5, 3], [1, 3, 1]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[57, 61], [0, 1]]
          >>> game = time_per_word(p, ['predative'])
          >>> all_words(game)
          ['predative']
          >>> all_times(game)
          [[4], [1]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[33, 38, 42, 47, 51, 52], [87, 90, 95, 96, 99, 103], [40, 41, 44, 47, 52, 57]]
          >>> game = time_per_word(p, ['ripe', 'spatuliform', 'serpent', 'truantship', 'epicrystalline'])
          >>> all_words(game)
          ['ripe', 'spatuliform', 'serpent', 'truantship', 'epicrystalline']
          >>> all_times(game)
          [[5, 4, 5, 4, 1], [3, 5, 1, 3, 4], [1, 3, 3, 5, 5]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[34, 39, 41, 46], [42, 46, 49, 52], [65, 66, 70, 74]]
          >>> game = time_per_word(p, ['appliable', 'dysepulotic', 'opodeldoc'])
          >>> all_words(game)
          ['appliable', 'dysepulotic', 'opodeldoc']
          >>> all_times(game)
          [[5, 2, 5], [4, 3, 3], [1, 4, 4]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[11, 13, 15], [58, 63, 65]]
          >>> game = time_per_word(p, ['ameed', 'pneumonopleuritis'])
          >>> all_words(game)
          ['ameed', 'pneumonopleuritis']
          >>> all_times(game)
          [[2, 2], [5, 2]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[17, 18, 22, 25, 30]]
          >>> game = time_per_word(p, ['acrid', 'broomwood', 'relatability', 'pearlite'])
          >>> all_words(game)
          ['acrid', 'broomwood', 'relatability', 'pearlite']
          >>> all_times(game)
          [[1, 4, 3, 5]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[51, 52, 53, 56, 57]]
          >>> game = time_per_word(p, ['housewarming', 'hymenean', 'crepusculine', 'solecizer'])
          >>> all_words(game)
          ['housewarming', 'hymenean', 'crepusculine', 'solecizer']
          >>> all_times(game)
          [[1, 1, 3, 1]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[6, 7, 8, 10, 15, 18, 21], [1, 3, 5, 8, 11, 14, 15]]
          >>> game = time_per_word(p, ['absolve', 'paradisic', 'unaffectionately', 'exordial', 'weaponshowing', 'rhombohedra'])
          >>> all_words(game)
          ['absolve', 'paradisic', 'unaffectionately', 'exordial', 'weaponshowing', 'rhombohedra']
          >>> all_times(game)
          [[1, 1, 2, 5, 3, 3], [2, 2, 3, 3, 3, 1]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[79, 83, 84, 88, 91], [90, 93, 97, 100, 101]]
          >>> game = time_per_word(p, ['official', 'platybrachycephalous', 'pitometer', 'electrodepositor'])
          >>> all_words(game)
          ['official', 'platybrachycephalous', 'pitometer', 'electrodepositor']
          >>> all_times(game)
          [[4, 1, 4, 3], [3, 4, 3, 1]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[9, 13, 17, 21], [91, 93, 94, 99]]
          >>> game = time_per_word(p, ['hoseless', 'passivity', 'sparrowcide'])
          >>> all_words(game)
          ['hoseless', 'passivity', 'sparrowcide']
          >>> all_times(game)
          [[4, 4, 4], [2, 1, 5]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[28, 33, 37], [24, 29, 33], [23, 28, 32]]
          >>> game = time_per_word(p, ['mischieve', 'dayfly'])
          >>> all_words(game)
          ['mischieve', 'dayfly']
          >>> all_times(game)
          [[5, 4], [5, 4], [5, 4]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[9, 10, 13, 17, 20, 21, 25], [56, 57, 62, 63, 67, 69, 74], [97, 102, 106, 107, 108, 111, 115]]
          >>> game = time_per_word(p, ['notoriety', 'undersorcerer', 'pneumoperitonitis', 'balaenoidean', 'strawbreadth', 'postconnubial'])
          >>> all_words(game)
          ['notoriety', 'undersorcerer', 'pneumoperitonitis', 'balaenoidean', 'strawbreadth', 'postconnubial']
          >>> all_times(game)
          [[1, 3, 4, 3, 1, 4], [1, 5, 1, 4, 2, 5], [5, 4, 1, 1, 3, 4]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[84, 89, 92, 97, 98, 101, 105], [72, 74, 76, 78, 83, 86, 89], [96, 101, 102, 105, 108, 112, 113]]
          >>> game = time_per_word(p, ['wold', 'relieved', 'quicksandy', 'guaraguao', 'stalkless', 'unexhilarated'])
          >>> all_words(game)
          ['wold', 'relieved', 'quicksandy', 'guaraguao', 'stalkless', 'unexhilarated']
          >>> all_times(game)
          [[5, 3, 5, 1, 3, 4], [2, 2, 2, 5, 3, 3], [5, 1, 3, 3, 4, 1]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[40, 43, 45, 46]]
          >>> game = time_per_word(p, ['metonymically', 'acomia', 'tamelessly'])
          >>> all_words(game)
          ['metonymically', 'acomia', 'tamelessly']
          >>> all_times(game)
          [[3, 2, 1]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[74], [94], [69]]
          >>> game = time_per_word(p, [])
          >>> all_words(game)
          []
          >>> all_times(game)
          [[], [], []]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[71, 76, 80, 85, 86, 90, 95], [97, 101, 104, 108, 112, 114, 116], [53, 55, 60, 62, 64, 69, 72]]
          >>> game = time_per_word(p, ['imitationist', 'undershut', 'unmannerly', 'sterneber', 'nonappendicular', 'cityish'])
          >>> all_words(game)
          ['imitationist', 'undershut', 'unmannerly', 'sterneber', 'nonappendicular', 'cityish']
          >>> all_times(game)
          [[5, 4, 5, 1, 4, 5], [4, 3, 4, 4, 2, 2], [2, 5, 2, 2, 5, 3]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[11, 13, 17, 20, 24, 27, 31], [31, 35, 36, 39, 43, 45, 48]]
          >>> game = time_per_word(p, ['afterwale', 'davidson', 'toadpipe', 'achete', 'twankle', 'hookers'])
          >>> all_words(game)
          ['afterwale', 'davidson', 'toadpipe', 'achete', 'twankle', 'hookers']
          >>> all_times(game)
          [[2, 4, 3, 4, 3, 4], [4, 1, 3, 4, 2, 3]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[19]]
          >>> game = time_per_word(p, [])
          >>> all_words(game)
          []
          >>> all_times(game)
          [[]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[26, 29]]
          >>> game = time_per_word(p, ['unsloped'])
          >>> all_words(game)
          ['unsloped']
          >>> all_times(game)
          [[3]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[57, 62, 66, 67, 71]]
          >>> game = time_per_word(p, ['tinwork', 'vortically', 'massicot', 'pinite'])
          >>> all_words(game)
          ['tinwork', 'vortically', 'massicot', 'pinite']
          >>> all_times(game)
          [[5, 4, 1, 4]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[78, 82, 87, 88, 92, 97]]
          >>> game = time_per_word(p, ['angelhood', 'xiphydriid', 'longicorn', 'shadchan', 'mixableness'])
          >>> all_words(game)
          ['angelhood', 'xiphydriid', 'longicorn', 'shadchan', 'mixableness']
          >>> all_times(game)
          [[4, 5, 1, 4, 5]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[1, 3, 6, 10, 13, 16]]
          >>> game = time_per_word(p, ['vibraculoid', 'feminility', 'voluminously', 'hydroferrocyanate', 'canthotomy'])
          >>> all_words(game)
          ['vibraculoid', 'feminility', 'voluminously', 'hydroferrocyanate', 'canthotomy']
          >>> all_times(game)
          [[2, 3, 4, 3, 3]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[23, 26, 28, 31, 36], [15, 20, 22, 27, 30], [81, 82, 87, 91, 96]]
          >>> game = time_per_word(p, ['aperient', 'kymbalon', 'plastogamy', 'grumpily'])
          >>> all_words(game)
          ['aperient', 'kymbalon', 'plastogamy', 'grumpily']
          >>> all_times(game)
          [[3, 2, 3, 5], [5, 2, 5, 3], [1, 5, 4, 5]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[49, 51, 53, 57], [42, 46, 51, 52]]
          >>> game = time_per_word(p, ['overprovidently', 'obdormition', 'precollect'])
          >>> all_words(game)
          ['overprovidently', 'obdormition', 'precollect']
          >>> all_times(game)
          [[2, 2, 4], [4, 5, 1]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[31, 34, 36, 40], [98, 100, 104, 106], [80, 85, 89, 94]]
          >>> game = time_per_word(p, ['baker', 'circumscribable', 'apostrophic'])
          >>> all_words(game)
          ['baker', 'circumscribable', 'apostrophic']
          >>> all_times(game)
          [[3, 2, 4], [2, 4, 2], [5, 4, 5]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[0, 1, 5]]
          >>> game = time_per_word(p, ['tractioneering', 'contestant'])
          >>> all_words(game)
          ['tractioneering', 'contestant']
          >>> all_times(game)
          [[1, 4]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[78, 79, 81]]
          >>> game = time_per_word(p, ['insecurity', 'afterturn'])
          >>> all_words(game)
          ['insecurity', 'afterturn']
          >>> all_times(game)
          [[1, 2]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[51, 56, 60]]
          >>> game = time_per_word(p, ['blankbook', 'subjectiveness'])
          >>> all_words(game)
          ['blankbook', 'subjectiveness']
          >>> all_times(game)
          [[5, 4]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[9, 13, 15, 20, 22]]
          >>> game = time_per_word(p, ['ophiophagous', 'rice', 'piousness', 'vibrissae'])
          >>> all_words(game)
          ['ophiophagous', 'rice', 'piousness', 'vibrissae']
          >>> all_times(game)
          [[4, 2, 5, 2]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[9, 14, 15, 18, 19, 23, 27]]
          >>> game = time_per_word(p, ['civicism', 'belletrist', 'vegetocarbonaceous', 'woodchuck', 'phacitis', 'warehouseful'])
          >>> all_words(game)
          ['civicism', 'belletrist', 'vegetocarbonaceous', 'woodchuck', 'phacitis', 'warehouseful']
          >>> all_times(game)
          [[5, 1, 3, 1, 4, 4]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[79]]
          >>> game = time_per_word(p, [])
          >>> all_words(game)
          []
          >>> all_times(game)
          [[]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[43, 46, 49, 50], [58, 63, 67, 72], [8, 10, 11, 13]]
          >>> game = time_per_word(p, ['discover', 'fixative', 'suprasphanoidal'])
          >>> all_words(game)
          ['discover', 'fixative', 'suprasphanoidal']
          >>> all_times(game)
          [[3, 3, 1], [5, 4, 5], [2, 1, 2]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[58, 61, 64, 65]]
          >>> game = time_per_word(p, ['semicompact', 'philopolemic', 'unharnessed'])
          >>> all_words(game)
          ['semicompact', 'philopolemic', 'unharnessed']
          >>> all_times(game)
          [[3, 3, 1]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[93, 96, 101], [29, 34, 36], [36, 39, 41]]
          >>> game = time_per_word(p, ['tom', 'spurgall'])
          >>> all_words(game)
          ['tom', 'spurgall']
          >>> all_times(game)
          [[3, 5], [5, 2], [3, 2]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[11, 16, 19], [70, 73, 75], [15, 18, 23]]
          >>> game = time_per_word(p, ['insubordination', 'bovicide'])
          >>> all_words(game)
          ['insubordination', 'bovicide']
          >>> all_times(game)
          [[5, 3], [3, 2], [3, 5]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[48, 53, 55, 57, 59, 60], [77, 82, 86, 89, 90, 91]]
          >>> game = time_per_word(p, ['gong', 'spondylium', 'agrammatism', 'yad', 'unintrusted'])
          >>> all_words(game)
          ['gong', 'spondylium', 'agrammatism', 'yad', 'unintrusted']
          >>> all_times(game)
          [[5, 2, 2, 2, 1], [5, 4, 3, 1, 1]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[22, 26, 27, 30], [93, 94, 97, 102], [56, 57, 59, 61]]
          >>> game = time_per_word(p, ['honolulu', 'tegularly', 'kilnrib'])
          >>> all_words(game)
          ['honolulu', 'tegularly', 'kilnrib']
          >>> all_times(game)
          [[4, 1, 3], [1, 3, 5], [1, 2, 2]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[97, 100, 105, 109, 113, 118, 123], [96, 97, 101, 105, 110, 112, 116], [20, 22, 26, 31, 34, 35, 38]]
          >>> game = time_per_word(p, ['succeed', 'dumminess', 'tedder', 'bobsleigh', 'tenendum', 'slatternness'])
          >>> all_words(game)
          ['succeed', 'dumminess', 'tedder', 'bobsleigh', 'tenendum', 'slatternness']
          >>> all_times(game)
          [[3, 5, 4, 4, 5, 5], [1, 4, 4, 5, 2, 4], [2, 4, 5, 3, 1, 3]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[97, 101, 104, 109, 111], [66, 68, 73, 76, 79]]
          >>> game = time_per_word(p, ['biventer', 'fugle', 'estimated', 'racinglike'])
          >>> all_words(game)
          ['biventer', 'fugle', 'estimated', 'racinglike']
          >>> all_times(game)
          [[4, 3, 5, 2], [2, 5, 3, 3]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[71, 75, 76], [28, 33, 36]]
          >>> game = time_per_word(p, ['gangliar', 'imbonity'])
          >>> all_words(game)
          ['gangliar', 'imbonity']
          >>> all_times(game)
          [[4, 1], [5, 3]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[65, 67, 70], [68, 71, 73]]
          >>> game = time_per_word(p, ['oculigerous', 'wavement'])
          >>> all_words(game)
          ['oculigerous', 'wavement']
          >>> all_times(game)
          [[2, 3], [3, 2]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[40, 41], [73, 76]]
          >>> game = time_per_word(p, ['autoimmunization'])
          >>> all_words(game)
          ['autoimmunization']
          >>> all_times(game)
          [[1], [3]]
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from cats import game, game_string, time_per_word, all_words, all_times, word_at, time
      """,
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> test.swap_implementations(cats) # Make sure the abstraction barrier isn't crossed!
          >>> p = [[1, 4, 6, 7], [0, 4, 6, 9]]
          >>> words = ['This', 'is', 'fun']
          >>> game = cats.time_per_word(p, words)
          >>> cats.all_words(game)
          ['This', 'is', 'fun']
          >>> cats.all_times(game)
          [[3, 2, 1], [4, 2, 3]]
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> import cats
      >>> import tests.abstraction_check as test
      """,
      'teardown': r"""
      >>> test.restore_implementations(cats)
      """,
      'type': 'doctest'
    }
  ]
}
