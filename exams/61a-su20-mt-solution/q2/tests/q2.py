test = {'name': 'q2',
 'points': 1,
 'suites': [{'cases': [{'code': '>>> int("5")\n'
                                '5\n'
                                '\n'
                                '>>> str(5)\n'
                                "'5'\n"
                                '\n'
                                ">>> 'evocative'[3]\n"
                                "'c'\n"
                                '\n'
                                ">>> 'evocative'[3:]\n"
                                "'cative'\n"
                                '\n'
                                ">>> 'evocative'[:6]\n"
                                "'evocat'\n"
                                '\n'
                                ">>> 'evocative'[3:6]\n"
                                "'cat'\n"
                                '\n'
                                ">>> schedule('?????', 25, 5)\n"
                                "['55555']\n"
                                '\n'
                                ">>> schedule('???', 5, 2)\n"
                                "['122', '212', '221']\n"
                                '\n'
                                ">>> schedule('?2??11?', 5, 3)\n"
                                "['0200111', '0201110', '0210110', "
                                "'1200110']\n"}],
             'scored': True,
             'setup': 'from q2 import *',
             'type': 'doctest'},
            {'cases': [{'code': ">>> schedule('???????', 56, 3)\n"
                                '[]\n'
                                '\n'
                                ">>> schedule('0000???', 4, 2)\n"
                                "['0000022', '0000112', '0000121', '0000202', "
                                "'0000211', '0000220']\n"
                                '\n'
                                ">>> schedule('0?000??', 4, 2)\n"
                                "['0000022', '0100012', '0100021', '0200002', "
                                "'0200011', '0200020']\n"}],
             'scored': True,
             'setup': 'from q2 import *',
             'type': 'doctest'}]}