test = {'name': 'q6',
 'points': 10,
 'suites': [{'cases': [{'code': '>>> increment = lambda x: x + 1\n'
                                '\n'
                                '>>> square = lambda x: x * x\n'
                                '\n'
                                '>>> do_nothing = make_zipper(increment, '
                                'square, 0)\n'
                                '\n'
                                ">>> do_nothing(2) # Don't call either f1 or "
                                'f2, just return your input untouched\n'
                                '2\n'
                                '\n'
                                '>>> incincsq = make_zipper(increment, square, '
                                '112)\n'
                                '\n'
                                '>>> incincsq(2) # '
                                'increment(increment(square(2))), so 2 -> 4 -> '
                                '5 -> 6\n'
                                '6\n'
                                '\n'
                                '>>> sqincsqinc = make_zipper(increment, '
                                'square, 2121)\n'
                                '\n'
                                '>>> sqincsqinc(2) # '
                                'square(increment(square(increment(2)))), so 2 '
                                '-> 3 -> 9 -> 10 -> 100\n'
                                '100\n'}],
             'scored': True,
             'setup': 'from q6 import *',
             'type': 'doctest'}]}