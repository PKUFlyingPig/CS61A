test = {'name': 'q3',
 'points': 1,
 'suites': [{'cases': [{'code': '>>> painting_a = microscope()\n'
                                '\n'
                                '>>> painting_b, x = painting_a(2)\n'
                                '\n'
                                '>>> x                                   # 2\n'
                                '2\n'
                                '\n'
                                '>>> painting_c, x = painting_b(8)\n'
                                '\n'
                                '>>> x                                   # 2 - '
                                '8\n'
                                '-6\n'
                                '\n'
                                '>>> painting_d, x = painting_c(12)\n'
                                '\n'
                                '>>> x                                   # 2 - '
                                '8 + 12\n'
                                '6\n'
                                '\n'
                                '>>> painting_e, x = painting_d(30)\n'
                                '\n'
                                '>>> x                                   # 2 - '
                                '8 + 12 - 30\n'
                                '-24\n'
                                '\n'
                                '>>> painting_b_again, x = painting_a(100)\n'
                                '\n'
                                '>>> x                                   # 100 '
                                '[note that we are using painting_a not '
                                'painting_d here]\n'
                                '100\n'
                                '\n'
                                '>>> plush(microscope(), [1, 2, 3, 4, 5])\n'
                                '3\n'
                                '\n'
                                '>>> plush(microscope(), [4000])\n'
                                '4000\n'
                                '\n'
                                '>>> plush(microscope(), [2, 90])\n'
                                '-88\n'
                                '\n'
                                '>>> plush(identity_painting, [2, 90])\n'
                                '90\n'}],
             'scored': True,
             'setup': 'from q3 import *',
             'type': 'doctest'},
            {'cases': [{'code': ''}],
             'scored': True,
             'setup': 'from q3 import *',
             'type': 'doctest'}]}