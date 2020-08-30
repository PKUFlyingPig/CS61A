test = {
  'name': 'Question 8',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'answer': 'It both takes in a function as an argument and returns a function',
          'choices': [
            'It takes in a function as an argument',
            'It returns a function',
            'It both takes in a function as an argument and returns a function',
            'It uses the *args keyword'
          ],
          'hidden': False,
          'locked': False,
          'question': 'What makes make_averaged a higher order function?'
        },
        {
          'answer': 'An arbitrary amount, which is why we need to use *args to call it',
          'choices': [
            'None',
            'Two',
            'An arbitrary amount, which is why we need to use *args to call it'
          ],
          'hidden': False,
          'locked': False,
          'question': 'How many arguments does the function passed into make_averaged take?'
        }
      ],
      'scored': False,
      'type': 'concept'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> dice = make_test_dice(3, 1, 5, 6)
          >>> averaged_dice = make_averaged(dice, 1000)
          >>> # Average of calling dice 1000 times
          >>> averaged_dice()
          3.75
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> dice = make_test_dice(3, 1, 5, 6)
          >>> averaged_roll_dice = make_averaged(roll_dice, 1000)
          >>> # Average of calling roll_dice 1000 times
          >>> # Enter a float (e.g. 1.0) instead of an integer
          >>> averaged_roll_dice(2, dice)
          6.0
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
          >>> hundred_range = range(1, 100)
          >>> hundred_dice = make_test_dice(*hundred_range)
          >>> averaged_hundred_dice = make_averaged(hundred_dice, 5*len(hundred_range))
          >>> correct_average = sum(range(1, 100)) / len(hundred_range)
          >>> averaged_hundred_dice()
          50.0
          >>> averaged_hundred_dice()
          50.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> dice = make_test_dice(3, 1, 5, 6)
          >>> averaged_roll_dice = make_averaged(roll_dice, 1)
          >>> averaged_roll_dice(2, dice)
          1.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> dice = make_test_dice(3, 1, 5, 6)
          >>> averaged_roll_dice = make_averaged(roll_dice, 5)
          >>> averaged_roll_dice(2, dice)
          5.0
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
