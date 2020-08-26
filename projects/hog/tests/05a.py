test = {
  'name': 'Question 5a',
  'points': 3,
  'suites': [
    {
      'cases': [
        {
          'answer': 'a4d959d6146005b45f9590c6bc256e37',
          'choices': [
            'While score0 and score1 are both less than goal',
            'While at least one of score0 or score1 is less than goal',
            'While score0 is less than goal',
            'While score1 is less than goal'
          ],
          'hidden': False,
          'locked': True,
          'question': r"""
          The variables score0 and score1 are the scores for Player 0
          and Player 1, respectively. Under what conditions should the
          game continue?
          """
        },
        {
          'answer': 'bcda62bd369acb79a636e354f5ef2f48',
          'choices': [
            'The number of dice a player will roll',
            'A function that returns the number of dice a player will roll',
            "A player's desired turn outcome"
          ],
          'hidden': False,
          'locked': True,
          'question': 'What is a strategy in the context of this game?'
        },
        {
          'answer': '6092933b58b128fe246b574b1aa79389',
          'choices': [
            'strategy1(score1, score0)',
            'strategy1(score0, score1)',
            'strategy1(score1)',
            'strategy1(score0)'
          ],
          'hidden': False,
          'locked': True,
          'question': r"""
          If strategy1 is Player 1's strategy function, score0 is
          Player 0's current score, and score1 is Player 1's current
          score, then which of the following demonstrates correct
          usage of strategy1?
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
          >>> #
          >>> # Play function stops at goal
          >>> s0, s1 = hog.play(always(5), always(3), score0=91, score1=10, dice=always_three, feral_hogs=False)
          >>> s0
          17a90ac6d84565b47483000c22f1f6de
          # locked
          >>> s1
          70e71b420a966665c548a3bb2cb30d7d
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> #
          >>> # Goal score is not hardwired
          >>> s0, s1 = hog.play(always(5), always(5), goal=10, dice=always_three, feral_hogs=False)
          >>> s0
          af0b3285304485122429774c0ea3182a
          # locked
          >>> s1
          962aea5f59fc55bd65ccacf4603c8f22
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> #
          >>> # Swap occurs
          >>> s0, s1 = hog.play(always(5), always(2), goal=25, dice=always_three, feral_hogs=False)
          >>> s0
          36
          >>> s1
          21
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> #
          >>> # Goal score is not hardwired
          >>> s0, s1 = hog.play(always(5), always(5), goal=15, dice=always_three, feral_hogs=False)
          >>> s0
          15
          >>> s1
          0
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> import hog
      >>> always_three = hog.make_test_dice(3)
      >>> always = hog.always_roll
      """,
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> #
          >>> # Use strategies
          >>> # We recommend working this out turn-by-turn on a piece of paper (use Python for difficult calculations).
          >>> strat0 = lambda score, opponent: opponent % 10
          >>> strat1 = lambda score, opponent: max((score // 10) - 4, 0)
          >>> s0, s1 = hog.play(strat0, strat1, score0=71, score1=80, dice=always_seven, feral_hogs=False)
          >>> s0
          9f23ad72a8164a1f8ecf40817db73cf3
          # locked
          >>> s1
          c8735a01952a81cf365b4c80d8fbb832
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': True,
      'setup': r"""
      >>> import hog
      >>> always_three = hog.make_test_dice(3)
      >>> always_seven = hog.make_test_dice(7)
      """,
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> #
          >>> # Player 0 win
          >>> s0, s1 = hog.play(always(4), always(4), score0=87, score1=88, dice=always_three, feral_hogs=False)
          >>> s0
          100
          >>> s1
          99
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> #
          >>> # Free bacon refers to correct opponent score
          >>> s0, s1 = hog.play(always(0), always(0), score0=9, score1=92, dice=always_three, feral_hogs=False)
          >>> s0
          26
          >>> s1
          104
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> #
          >>> # Handle multiple turns with many swaps
          >>> s0, s1 = hog.play(always(1), always(1), goal=20, dice=hog.make_test_dice(2, 10, 10, 5, 5), feral_hogs=False)
          >>> s0
          27
          >>> s1
          17
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> import hog
      >>> always_one = hog.make_test_dice(1)
      >>> always_two = hog.make_test_dice(2)
      >>> always_three = hog.make_test_dice(3)
      >>> always = hog.always_roll
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
