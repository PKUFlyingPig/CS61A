test = {
  'name': 'Question 10',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> bacon_strategy(0, 9, cutoff=8, num_rolls=5)
          5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> bacon_strategy(9, 0, cutoff=6, num_rolls=5)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> bacon_strategy(50, 2, cutoff=9, num_rolls=5)
          5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> bacon_strategy(32, 0, cutoff=5, num_rolls=4)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> bacon_strategy(20, 1, cutoff=1, num_rolls=4)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> from tests.check_strategy import check_strategy
          >>> check_strategy(bacon_strategy)
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from hog import *
      """,
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> bacon_strategy(44, 47, 0, 4)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> bacon_strategy(37, 12, 8, 10)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> bacon_strategy(40, 15, 13, 9)
          9
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> bacon_strategy(24, 3, 8, 1)
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> bacon_strategy(46, 55, 5, 2)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> bacon_strategy(99, 78, 15, 7)
          7
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> bacon_strategy(10, 73, 3, 5)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> bacon_strategy(47, 68, 3, 4)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> bacon_strategy(67, 84, 17, 10)
          10
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> bacon_strategy(92, 54, 1, 7)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> bacon_strategy(9, 15, 0, 2)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> bacon_strategy(25, 63, 16, 2)
          2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> bacon_strategy(75, 27, 6, 2)
          2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> bacon_strategy(82, 48, 10, 1)
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> bacon_strategy(88, 12, 7, 10)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> bacon_strategy(72, 12, 5, 8)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> bacon_strategy(41, 69, 1, 5)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> bacon_strategy(15, 6, 16, 7)
          7
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> bacon_strategy(42, 19, 5, 2)
          2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> bacon_strategy(93, 98, 8, 4)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> bacon_strategy(99, 90, 15, 10)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> bacon_strategy(73, 79, 4, 1)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> bacon_strategy(4, 44, 0, 5)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> bacon_strategy(83, 40, 9, 7)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> bacon_strategy(34, 3, 0, 8)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> bacon_strategy(4, 62, 15, 7)
          7
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> bacon_strategy(53, 62, 6, 1)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> bacon_strategy(19, 56, 8, 9)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> bacon_strategy(1, 5, 0, 4)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> bacon_strategy(85, 34, 8, 1)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> bacon_strategy(37, 37, 13, 5)
          5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> bacon_strategy(82, 87, 16, 3)
          3
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> bacon_strategy(87, 43, 5, 7)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> bacon_strategy(20, 7, 2, 3)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> bacon_strategy(33, 85, 4, 4)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> bacon_strategy(73, 15, 12, 8)
          8
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> bacon_strategy(5, 98, 8, 2)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> bacon_strategy(15, 76, 3, 4)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> bacon_strategy(33, 75, 19, 5)
          5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> bacon_strategy(9, 41, 0, 5)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> bacon_strategy(70, 91, 7, 6)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> bacon_strategy(64, 35, 12, 3)
          3
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> bacon_strategy(51, 92, 14, 8)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> bacon_strategy(68, 64, 17, 6)
          6
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> bacon_strategy(20, 35, 17, 4)
          4
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> bacon_strategy(75, 30, 3, 1)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> bacon_strategy(61, 69, 8, 5)
          5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> bacon_strategy(7, 6, 7, 9)
          9
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> bacon_strategy(0, 51, 17, 5)
          5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> bacon_strategy(42, 45, 8, 6)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> bacon_strategy(48, 96, 11, 2)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> bacon_strategy(57, 96, 9, 6)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> bacon_strategy(28, 11, 13, 8)
          8
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> bacon_strategy(25, 29, 5, 7)
          7
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> bacon_strategy(69, 2, 15, 8)
          8
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> bacon_strategy(77, 26, 7, 9)
          9
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> bacon_strategy(85, 15, 0, 3)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> bacon_strategy(79, 86, 5, 7)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> bacon_strategy(35, 32, 14, 6)
          6
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> bacon_strategy(49, 44, 13, 8)
          8
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> bacon_strategy(77, 65, 6, 4)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> bacon_strategy(99, 18, 2, 1)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> bacon_strategy(18, 24, 17, 10)
          10
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> bacon_strategy(44, 11, 18, 1)
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> bacon_strategy(68, 38, 17, 5)
          5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> bacon_strategy(46, 63, 8, 6)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> bacon_strategy(20, 60, 19, 6)
          6
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> bacon_strategy(67, 53, 10, 6)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> bacon_strategy(63, 39, 4, 1)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> bacon_strategy(54, 75, 9, 8)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> bacon_strategy(78, 86, 18, 9)
          9
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> bacon_strategy(45, 11, 8, 9)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> bacon_strategy(88, 19, 14, 6)
          6
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> bacon_strategy(22, 18, 14, 1)
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> bacon_strategy(30, 91, 9, 10)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> bacon_strategy(19, 81, 8, 1)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> bacon_strategy(33, 7, 0, 2)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> bacon_strategy(87, 95, 11, 6)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> bacon_strategy(69, 86, 8, 10)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> bacon_strategy(87, 61, 10, 4)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> bacon_strategy(47, 60, 6, 4)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> bacon_strategy(67, 65, 14, 4)
          4
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> bacon_strategy(3, 66, 3, 7)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> bacon_strategy(82, 23, 8, 8)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> bacon_strategy(42, 89, 14, 1)
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> bacon_strategy(32, 13, 4, 4)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> bacon_strategy(20, 96, 12, 4)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> bacon_strategy(77, 59, 15, 7)
          7
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> bacon_strategy(88, 32, 15, 2)
          2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> bacon_strategy(19, 30, 4, 7)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> bacon_strategy(91, 29, 18, 4)
          4
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> bacon_strategy(50, 46, 10, 3)
          3
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> bacon_strategy(42, 67, 18, 7)
          7
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> bacon_strategy(37, 91, 4, 9)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> bacon_strategy(59, 82, 0, 6)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> bacon_strategy(22, 41, 19, 7)
          7
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> bacon_strategy(84, 90, 6, 5)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> bacon_strategy(90, 35, 9, 4)
          4
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> bacon_strategy(90, 42, 1, 5)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> bacon_strategy(1, 35, 8, 10)
          0
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from hog import *
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
