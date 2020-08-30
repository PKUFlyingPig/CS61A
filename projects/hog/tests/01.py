test = {
  'name': 'Question 1',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> roll_dice(2, make_test_dice(4, 6, 1))
          10
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> roll_dice(3, make_test_dice(4, 6, 1))
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> roll_dice(4, make_test_dice(2, 2, 3))
          9
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> roll_dice(4, make_test_dice(1, 2, 3))
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> counted_dice = make_test_dice(4, 1, 2, 6)
          >>> roll_dice(3, counted_dice)
          1
          >>> # Make sure you call dice exactly num_rolls times!
          >>> # If you call it fewer or more than that, it won't be at the right spot in the cycle for the next roll
          >>> # Note that a return statement in a for loop ends the loop
          >>> roll_dice(1, counted_dice)
          6
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> roll_dice(9, make_test_dice(6))
          54
          >>> roll_dice(7, make_test_dice(2, 2, 2, 2, 2, 2, 1))
          1
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
          >>> roll_dice(5, make_test_dice(4, 2, 3, 3, 4, 1))
          16
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> roll_dice(2, make_test_dice(1))
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> dice = make_test_dice(5, 4, 3, 2, 1)
          >>> roll_dice(1, dice)    # Roll 1 (5)
          5
          >>> roll_dice(4, dice)    # Reset (4, 3, 2, 1)
          1
          >>> roll_dice(2, dice)    # Roll 2 (5, 4)
          9
          >>> roll_dice(3, dice)    # Reset (3, 2, 1)
          1
          >>> roll_dice(3, dice)    # Roll 3 (5, 4, 3)
          12
          >>> roll_dice(2, dice)    # Reset (2, 1)
          1
          >>> roll_dice(4, dice)    # Roll 4 (5, 4, 3, 2)
          14
          >>> roll_dice(1, dice)    # Reset (1)
          1
          >>> roll_dice(5, dice)    # Roll 5 (5, 4, 3, 2, 1)
          1
          >>> roll_dice(10, dice)    # Roll 10 (5, 4, 3, 2, 1, 5, 4, 3, 2, 1)
          1
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
          >>> dice = make_test_dice(1, 4, 4, 4, 2)
          >>> roll_dice(3, dice)
          1
          >>> roll_dice(5, dice)
          1
          >>> roll_dice(1, dice)
          4
          >>> roll_dice(1, dice)
          2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> dice = make_test_dice(4, 5, 1, 2, 4, 1)
          >>> roll_dice(2, dice)
          9
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> dice = make_test_dice(1,)
          >>> roll_dice(4, dice)
          1
          >>> roll_dice(3, dice)
          1
          >>> roll_dice(4, dice)
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> dice = make_test_dice(1, 2, 4)
          >>> roll_dice(1, dice)
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> dice = make_test_dice(2, 1, 1)
          >>> roll_dice(2, dice)
          1
          >>> roll_dice(3, dice)
          1
          >>> roll_dice(5, dice)
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> dice = make_test_dice(1, 2, 1, 5)
          >>> roll_dice(4, dice)
          1
          >>> roll_dice(1, dice)
          1
          >>> roll_dice(1, dice)
          2
          >>> roll_dice(5, dice)
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> dice = make_test_dice(2, 4, 5)
          >>> roll_dice(3, dice)
          11
          >>> roll_dice(1, dice)
          2
          >>> roll_dice(2, dice)
          9
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> dice = make_test_dice(2, 4, 4, 5, 2)
          >>> roll_dice(1, dice)
          2
          >>> roll_dice(2, dice)
          8
          >>> roll_dice(3, dice)
          9
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> dice = make_test_dice(5, 2, 2, 3)
          >>> roll_dice(4, dice)
          12
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> dice = make_test_dice(1, 4, 2, 5, 4)
          >>> roll_dice(3, dice)
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> dice = make_test_dice(5, 1)
          >>> roll_dice(4, dice)
          1
          >>> roll_dice(5, dice)
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> dice = make_test_dice(1, 4)
          >>> roll_dice(5, dice)
          1
          >>> roll_dice(2, dice)
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> dice = make_test_dice(4, 2, 3, 4)
          >>> roll_dice(5, dice)
          17
          >>> roll_dice(1, dice)
          2
          >>> roll_dice(2, dice)
          7
          >>> roll_dice(5, dice)
          17
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> dice = make_test_dice(1, 3, 1)
          >>> roll_dice(3, dice)
          1
          >>> roll_dice(5, dice)
          1
          >>> roll_dice(2, dice)
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> dice = make_test_dice(1, 5, 2, 3)
          >>> roll_dice(3, dice)
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> dice = make_test_dice(5,)
          >>> roll_dice(1, dice)
          5
          >>> roll_dice(5, dice)
          25
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> dice = make_test_dice(2, 2)
          >>> roll_dice(5, dice)
          10
          >>> roll_dice(5, dice)
          10
          >>> roll_dice(2, dice)
          4
          >>> roll_dice(1, dice)
          2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> dice = make_test_dice(2, 1)
          >>> roll_dice(5, dice)
          1
          >>> roll_dice(5, dice)
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> dice = make_test_dice(4, 1, 2)
          >>> roll_dice(3, dice)
          1
          >>> roll_dice(3, dice)
          1
          >>> roll_dice(1, dice)
          4
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> dice = make_test_dice(3, 1, 4, 5, 3, 3)
          >>> roll_dice(3, dice)
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> dice = make_test_dice(3, 5, 3, 2)
          >>> roll_dice(4, dice)
          13
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> dice = make_test_dice(1, 5)
          >>> roll_dice(1, dice)
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> dice = make_test_dice(5, 5, 1, 5, 4, 5)
          >>> roll_dice(5, dice)
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> dice = make_test_dice(1, 2, 1, 5)
          >>> roll_dice(3, dice)
          1
          >>> roll_dice(2, dice)
          1
          >>> roll_dice(4, dice)
          1
          >>> roll_dice(4, dice)
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> dice = make_test_dice(4, 1, 2)
          >>> roll_dice(2, dice)
          1
          >>> roll_dice(5, dice)
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> dice = make_test_dice(3, 5, 3, 1, 5)
          >>> roll_dice(2, dice)
          8
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> dice = make_test_dice(1, 2, 4, 3, 1, 5)
          >>> roll_dice(2, dice)
          1
          >>> roll_dice(4, dice)
          1
          >>> roll_dice(2, dice)
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> dice = make_test_dice(1, 1, 1, 1)
          >>> roll_dice(1, dice)
          1
          >>> roll_dice(2, dice)
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> dice = make_test_dice(2, 5)
          >>> roll_dice(4, dice)
          14
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> dice = make_test_dice(4, 5, 3, 1, 1, 2)
          >>> roll_dice(1, dice)
          4
          >>> roll_dice(4, dice)
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> dice = make_test_dice(5, 5, 3, 4, 2, 4)
          >>> roll_dice(2, dice)
          10
          >>> roll_dice(2, dice)
          7
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> dice = make_test_dice(1, 3, 3)
          >>> roll_dice(5, dice)
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> dice = make_test_dice(5, 1, 4, 5)
          >>> roll_dice(2, dice)
          1
          >>> roll_dice(4, dice)
          1
          >>> roll_dice(3, dice)
          14
          >>> roll_dice(2, dice)
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> dice = make_test_dice(1, 3, 3, 2, 2)
          >>> roll_dice(4, dice)
          1
          >>> roll_dice(5, dice)
          1
          >>> roll_dice(3, dice)
          1
          >>> roll_dice(4, dice)
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> dice = make_test_dice(3, 3)
          >>> roll_dice(5, dice)
          15
          >>> roll_dice(4, dice)
          12
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> dice = make_test_dice(5, 2)
          >>> roll_dice(1, dice)
          5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> dice = make_test_dice(3, 1, 2, 3, 3, 5)
          >>> roll_dice(5, dice)
          1
          >>> roll_dice(1, dice)
          5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> dice = make_test_dice(5, 4, 5, 3)
          >>> roll_dice(4, dice)
          17
          >>> roll_dice(3, dice)
          14
          >>> roll_dice(1, dice)
          3
          >>> roll_dice(1, dice)
          5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> dice = make_test_dice(4, 4)
          >>> roll_dice(5, dice)
          20
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> dice = make_test_dice(2, 2)
          >>> roll_dice(5, dice)
          10
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> dice = make_test_dice(1, 1, 3, 2)
          >>> roll_dice(3, dice)
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> dice = make_test_dice(4,)
          >>> roll_dice(3, dice)
          12
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> dice = make_test_dice(5, 3, 5, 5)
          >>> roll_dice(2, dice)
          8
          >>> roll_dice(3, dice)
          15
          >>> roll_dice(3, dice)
          13
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> dice = make_test_dice(1, 2, 3, 1, 4)
          >>> roll_dice(4, dice)
          1
          >>> roll_dice(4, dice)
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> dice = make_test_dice(4, 2, 4, 4, 1)
          >>> roll_dice(4, dice)
          14
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> dice = make_test_dice(4, 5, 1, 4)
          >>> roll_dice(2, dice)
          9
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> dice = make_test_dice(1, 5, 3, 4, 3, 4)
          >>> roll_dice(5, dice)
          1
          >>> roll_dice(4, dice)
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> dice = make_test_dice(1,)
          >>> roll_dice(1, dice)
          1
          >>> roll_dice(4, dice)
          1
          >>> roll_dice(1, dice)
          1
          >>> roll_dice(2, dice)
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> dice = make_test_dice(4,)
          >>> roll_dice(5, dice)
          20
          >>> roll_dice(4, dice)
          16
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> dice = make_test_dice(1, 5, 3)
          >>> roll_dice(5, dice)
          1
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> # generated case
      >>> from hog import *
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
