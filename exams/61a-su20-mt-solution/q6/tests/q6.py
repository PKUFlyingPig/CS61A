test = {'name': 'q6',
 'points': 1,
 'suites': [{'cases': [{'code': ">>> copycat(['a', 'b', 'c'], [1, 2, 3])\n"
                                "['a', 'b', 'b', 'c', 'c', 'c']\n"
                                '\n'
                                ">>> copycat(['a', 'b', 'c'], [3])\n"
                                "['a', 'a', 'a']\n"
                                '\n'
                                ">>> copycat(['a', 'b', 'c'], [0, 2, 0])\n"
                                "['b', 'b']\n"
                                '\n'
                                '>>> copycat([], [1,2,3])\n'
                                '[]\n'
                                '\n'
                                ">>> copycat(['a', 'b', 'c'], [1, -1, 3])\n"
                                "['c', 'c', 'c']\n"}],
             'scored': True,
             'setup': 'from q6 import *',
             'type': 'doctest'}]}