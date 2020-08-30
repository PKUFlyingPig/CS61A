test = {'name': 'q7',
 'points': 8,
 'suites': [{'cases': [{'code': '>>> t = Tree (1 , [ Tree (2) , Tree (1 , [ '
                                'Tree (2 , [ Tree (3 , [ Tree (0)])])])])\n'
                                '\n'
                                '>>> longest_seq( t) # 1 -> 2 -> 3\n'
                                '3\n'
                                '\n'
                                '>>> t = Tree (1)\n'
                                '\n'
                                '>>> longest_seq( t)\n'
                                '1\n'}],
             'scored': True,
             'setup': 'from q7 import *',
             'type': 'doctest'}]}