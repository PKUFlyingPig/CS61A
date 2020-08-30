test = {
  'name': 'Question 9',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'answer': 'The lowest num_rolls',
          'choices': [
            'The lowest num_rolls',
            'The highest num_rolls',
            'A random num_rolls'
          ],
          'hidden': False,
          'locked': False,
          'question': r"""
          If multiple num_rolls are tied for the highest scoring
          average, which should you return?
          """
        }
      ],
      'scored': False,
      'type': 'concept'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> dice = make_test_dice(3)   # dice always returns 3
          >>> max_scoring_num_rolls(dice, trials_count=1000)
          10
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> dice = make_test_dice(1, 2, 2, 2, 2, 2, 2, 2)
          >>> max_scoring_num_rolls(dice, trials_count=1000)
          4
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> dice = make_test_dice(*([2] * 55 + [1, 2] * 500)) # test that you are actually using trials_count
          >>> max_scoring_num_rolls(dice, trials_count=1) # dice is 2 for the first 55 rolls, then is 1 followed by 2 for 1000 rolls
          10
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
          >>> dice = make_test_dice(2)     # dice always rolls 2
          >>> max_scoring_num_rolls(dice, trials_count=1000)
          10
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> dice = make_test_dice(1, 2)  # dice alternates 1 and 2
          >>> max_scoring_num_rolls(dice, trials_count=1000)
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # 100 2s and then 100 1s (don't worry about how this works)
          >>> dice = make_test_dice(*([2] * 100 + [1] * 100))
          >>> max_scoring_num_rolls(dice, trials_count=1)
          10
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> dice = make_test_dice(1, 2, 3, 4, 5)  # dice sweeps from 1 through 5
          >>> max_scoring_num_rolls(dice, trials_count=1000)
          3
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
