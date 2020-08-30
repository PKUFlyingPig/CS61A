test = {'name': 'q7',
 'points': 1,
 'suites': [{'cases': [{'code': '>>> t = tree(10, [tree(20), tree(30)])\n'
                                '\n'
                                '>>> apple = lambda x: tree(x, [tree(x + 1), '
                                'tree(x + 2)])\n'
                                '\n'
                                '>>> print_tree(village(apple, t))\n'
                                '10\n'
                                '  11\n'
                                '    20\n'
                                '      21\n'
                                '      22\n'
                                '    30\n'
                                '      31\n'
                                '      32\n'
                                '  12\n'
                                '    20\n'
                                '      21\n'
                                '      22\n'
                                '    30\n'
                                '      31\n'
                                '      32\n'}],
             'scored': True,
             'setup': 'from q7 import *',
             'type': 'doctest'},
            {'cases': [{'code': '>>> t = tree(1, [tree(2, [tree(3)])])\n'
                                '\n'
                                '>>> f = lambda x: tree(x * 10, [tree(x * 10 + '
                                '1)])\n'
                                '\n'
                                '>>> print_tree(village(f, t))\n'
                                '10\n'
                                '  11\n'
                                '    20\n'
                                '      21\n'
                                '        30\n'
                                '          31\n'}],
             'scored': True,
             'setup': 'from q7 import *',
             'type': 'doctest'}]}