test = {
  'name': 'Question 6',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'answer': '5e0e1a4c94a7429afae6399105d34f05',
          'choices': [
            'Another commentary function.',
            'An integer representing the score.',
            'None.'
          ],
          'hidden': False,
          'locked': True,
          'question': 'What does a commentary function return?'
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
          >>> def echo(s0, s1):
          ...     print(s0, s1)
          ...     return echo
          >>> s0, s1 = play(always_roll(1), always_roll(1), dice=make_test_dice(3), goal=5, say=echo)
          d7882c94106188a2f424c5383b507923
          b706c6a1e63c19ed82e4eb95fc6ba1cf
          b57f18b04748377f05b1484da01f28e5
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> #
          >>> def count(n):
          ...     def say(s0, s1):
          ...         print(n, s0)
          ...         return count(n + 1)
          ...     return say
          >>> s0, s1 = play(always_roll(1), always_roll(1), dice=make_test_dice(3), goal=10, say=count(1))
          eb6cc5cdf2dcda4c703cdbcd21f5cf2e
          171f8c4ecc4156afed477dca7ce10d2e
          42770ee9d7532fb28c11e9844d8c1e65
          2dcc4e620fd1442ead74430ada359cd7
          28f5c4d1dc504abc4af21b1f88db2f13
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> #
          >>> def echo(s0, s1):
          ...     print(s0, s1)
          ...     return echo
          >>> strat0 = lambda score, opponent: 1 - opponent // 10
          >>> strat1 = always_roll(3)
          >>> s0, s1 = play(strat0, strat1, dice=make_test_dice(4, 2, 6), goal=15, say=echo)
          f4d41f4e29a08f003e0a9a5473c61d5e
          461ff541bd06a2e3310447d10cc6615b
          caedb1cff772abe19708326f743222d2
          25a122abac000b953fec91f46575dbd9
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> #
          >>> # Ensure that say is properly updated within the body of play.
          >>> def total(s0, s1):
          ...     print(s0 + s1)
          ...     return echo
          >>> def echo(s0, s1):
          ...     print(s0, s1)
          ...     return total
          >>> s0, s1 = play(always_roll(1), always_roll(1), dice=make_test_dice(2, 3), goal=15, say=echo)
          accd0f5c57e0f3fad13791aaecafc38b
          26f5762c932a578994ea1c8fc7fa6c02
          e3bcdb2715b868db45692ec2a5971a84
          b5f748b949729bc0225f547dce8206af
          21ec796517d0ce8312bdbd311b5a35c3
          6790f7070fa643e868f99363486b6275
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from hog import play, always_roll
      >>> from dice import make_test_dice
      """,
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> #
          >>> def echo_0(s0, s1):
          ...     print('*', s0)
          ...     return echo_0
          >>> def echo_1(s0, s1):
          ...     print('**', s1)
          ...     return echo_1
          >>> s0, s1 = play(always_roll(1), always_roll(1), dice=make_test_dice(2), goal=3, say=both(echo_0, echo_1))
          3f321d5ce997d2f3989685f56de8bdce
          4a64fe964dc771a219ed773c3a146c75
          3f321d5ce997d2f3989685f56de8bdce
          e4010b4a7d51e81cc1f49e08b015b8eb
          a6ba27fb33805545324a96eadcd30897
          e4010b4a7d51e81cc1f49e08b015b8eb
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> #
          >>> s0, s1 = play(always_roll(3), always_roll(3), dice=make_test_dice(1, 2, 3, 3), goal=8, say=both(say_scores, announce_lead_changes()))
          Player 0 now has 1 and Player 1 now has 0
          Player 0 takes the lead by 1
          Player 0 now has 1 and Player 1 now has 1
          Player 0 now has 5 and Player 1 now has 1
          Player 0 takes the lead by 4
          Player 0 now has 5 and Player 1 now has 12
          Player 1 takes the lead by 7
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from hog import play, always_roll, both, announce_lead_changes, say_scores
      >>> from dice import make_test_dice
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
