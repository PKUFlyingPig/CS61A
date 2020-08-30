test = {'name': 'q4',
 'points': 1,
 'suites': [{'cases': [{'code': '>>> isinstance("abc", str)\n'
                                'True\n'
                                '\n'
                                '>>> isinstance("abc", list)\n'
                                'False\n'
                                '\n'
                                '>>> x = [200, 300]\n'
                                '\n'
                                '>>> x.append(x)\n'
                                '\n'
                                '>>> y = [x, x]              # this is the `y` '
                                'from the doctests\n'
                                '\n'
                                '>>> lemon_y = lemon(y)      # this is the '
                                '`lemon_y` from the doctests\n'
                                '\n'
                                '>>> len(lemon_y)\n'
                                '2\n'
                                '\n'
                                '>>> lemon_y[0] is lemon_y[1]\n'
                                'True\n'
                                '\n'
                                '>>> len(lemon_y[0])\n'
                                '3\n'
                                '\n'
                                '>>> lemon_y[0][0]\n'
                                '200\n'
                                '\n'
                                '>>> lemon_y[0][1]\n'
                                '300\n'
                                '\n'
                                '>>> lemon_y[0][2] is lemon_y[0]\n'
                                'True\n'
                                '\n'
                                '>>> lemon_y is y\n'
                                'False\n'
                                '\n'
                                '>>> lemon_y[0] is y[0]\n'
                                'False\n'}],
             'scored': True,
             'setup': 'from q4 import *',
             'type': 'doctest'},
            {'cases': [{'code': '>>> a = []\n'
                                '\n'
                                '>>> lemon_a = lemon(a)\n'
                                '\n'
                                '>>> lemon_a\n'
                                '[]\n'
                                '\n'
                                '>>> lemon_a is a\n'
                                'False\n'}],
             'scored': True,
             'setup': 'from q4 import *',
             'type': 'doctest'},
            {'cases': [{'code': '>>> b = []\n'
                                '\n'
                                '>>> b.append(b)\n'
                                '\n'
                                '>>> lemon_b = lemon(b)\n'
                                '\n'
                                '>>> len(lemon_b)\n'
                                '1\n'
                                '\n'
                                '>>> lemon_b is lemon_b[0]\n'
                                'True\n'
                                '\n'
                                '>>> lemon_b is b\n'
                                'False\n'}],
             'scored': True,
             'setup': 'from q4 import *',
             'type': 'doctest'}]}