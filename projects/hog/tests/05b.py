test = {
  'name': 'Question 5b',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # example 1
          >>> def strat0(s0, s1):
          ...     if s0 == 0: return 3
          ...     if s0 == 7: return 5
          ...     return 8
          >>> def strat1(s0, s1):
          ...     if s0 == 0: return 1
          ...     if s0 == 4: return 2
          ...     return 6
          >>> s0, s1 = hog.play(
          ...   strat0, strat1, score0=0, score1=0, goal=21,
          ...   dice=hog.make_test_dice(2, 2, 3, 4, 2, 2, 2, 2, 2, 3, 5, 2, 2, 2, 2, 2, 2, 2, 6, 1))
          >>> s0
          43
          >>> s1
          15
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # example 2
          >>> s0, s1 = hog.play(always(2), always(1), score0=0, score1=0, goal=5, dice=hog.make_test_dice(2, 2))
          >>> s0
          7
          >>> s1
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # swap after feral hogs
          >>> s0, s1 = hog.play(always(2), always(1), score0=17, score1=6, goal=21, dice=hog.make_test_dice(1, 2))
          >>> s0
          21
          >>> s1
          6
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
    },
    {
      'cases': [
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=45891, score0=47, score1=53, goal=54, feral_hogs=True)
          >>> print(turns[0])
          Start scores = (47, 53).
          Player 0 rolls 9 dice and gets outcomes [5, 1, 1, 2, 6, 1, 1, 1, 5].
          End scores = (53, 48)
          >>> print(turns[1])
          Start scores = (53, 48).
          Player 1 rolls 3 dice and gets outcomes [3, 2, 6].
          End scores = (53, 59)
          >>> print(turns[2])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=5192, score0=43, score1=12, goal=47, feral_hogs=True)
          >>> print(turns[0])
          Start scores = (43, 12).
          Player 0 rolls 8 dice and gets outcomes [2, 1, 5, 1, 3, 3, 2, 3].
          End scores = (44, 12)
          >>> print(turns[1])
          Start scores = (44, 12).
          Player 1 rolls 8 dice and gets outcomes [5, 2, 5, 3, 5, 4, 2, 1].
          End scores = (44, 13)
          >>> print(turns[2])
          Start scores = (44, 13).
          Player 0 rolls 6 dice and gets outcomes [2, 3, 1, 1, 6, 1].
          End scores = (45, 13)
          >>> print(turns[3])
          Start scores = (45, 13).
          Player 1 rolls 3 dice and gets outcomes [4, 6, 5].
          End scores = (31, 45)
          >>> print(turns[4])
          Start scores = (31, 45).
          Player 0 rolls 1 dice and gets outcomes [4].
          End scores = (35, 45)
          >>> print(turns[5])
          Start scores = (35, 45).
          Player 1 rolls 5 dice and gets outcomes [5, 2, 6, 1, 1].
          End scores = (35, 46)
          >>> print(turns[6])
          Start scores = (35, 46).
          Player 0 rolls 9 dice and gets outcomes [3, 6, 6, 6, 2, 6, 2, 2, 6].
          End scores = (74, 46)
          >>> print(turns[7])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=95816, score0=15, score1=45, goal=50, feral_hogs=False)
          >>> print(turns[0])
          Start scores = (15, 45).
          Player 0 rolls 8 dice and gets outcomes [2, 3, 1, 6, 5, 1, 5, 6].
          End scores = (16, 45)
          >>> print(turns[1])
          Start scores = (16, 45).
          Player 1 rolls 10 dice and gets outcomes [5, 2, 4, 3, 6, 3, 4, 5, 1, 2].
          End scores = (16, 46)
          >>> print(turns[2])
          Start scores = (16, 46).
          Player 0 rolls 2 dice and gets outcomes [4, 6].
          End scores = (26, 46)
          >>> print(turns[3])
          Start scores = (26, 46).
          Player 1 rolls 1 dice and gets outcomes [2].
          End scores = (48, 26)
          >>> print(turns[4])
          Start scores = (48, 26).
          Player 0 rolls 5 dice and gets outcomes [2, 1, 4, 2, 6].
          End scores = (49, 26)
          >>> print(turns[5])
          Start scores = (49, 26).
          Player 1 rolls 8 dice and gets outcomes [6, 3, 4, 6, 5, 6, 5, 3].
          End scores = (49, 64)
          >>> print(turns[6])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=25365, score0=3, score1=8, goal=34, feral_hogs=True)
          >>> print(turns[0])
          Start scores = (3, 8).
          Player 0 rolls 6 dice and gets outcomes [2, 5, 4, 6, 5, 1].
          End scores = (4, 8)
          >>> print(turns[1])
          Start scores = (4, 8).
          Player 1 rolls 0 dice and gets outcomes [].
          End scores = (14, 4)
          >>> print(turns[2])
          Start scores = (14, 4).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (20, 4)
          >>> print(turns[3])
          Start scores = (20, 4).
          Player 1 rolls 2 dice and gets outcomes [2, 2].
          End scores = (20, 8)
          >>> print(turns[4])
          Start scores = (20, 8).
          Player 0 rolls 3 dice and gets outcomes [3, 1, 1].
          End scores = (21, 8)
          >>> print(turns[5])
          Start scores = (21, 8).
          Player 1 rolls 7 dice and gets outcomes [6, 2, 6, 5, 5, 2, 4].
          End scores = (21, 38)
          >>> print(turns[6])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=11863, score0=55, score1=5, goal=56, feral_hogs=False)
          >>> print(turns[0])
          Start scores = (55, 5).
          Player 0 rolls 6 dice and gets outcomes [5, 1, 2, 1, 3, 5].
          End scores = (56, 5)
          >>> print(turns[1])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=59465, score0=61, score1=16, goal=88, feral_hogs=False)
          >>> print(turns[0])
          Start scores = (61, 16).
          Player 0 rolls 4 dice and gets outcomes [2, 2, 3, 4].
          End scores = (72, 16)
          >>> print(turns[1])
          Start scores = (72, 16).
          Player 1 rolls 2 dice and gets outcomes [2, 3].
          End scores = (72, 21)
          >>> print(turns[2])
          Start scores = (72, 21).
          Player 0 rolls 9 dice and gets outcomes [2, 6, 3, 6, 2, 1, 5, 1, 3].
          End scores = (21, 73)
          >>> print(turns[3])
          Start scores = (21, 73).
          Player 1 rolls 10 dice and gets outcomes [2, 2, 2, 2, 2, 1, 1, 1, 3, 1].
          End scores = (21, 74)
          >>> print(turns[4])
          Start scores = (21, 74).
          Player 0 rolls 9 dice and gets outcomes [5, 5, 3, 1, 2, 2, 6, 3, 4].
          End scores = (22, 74)
          >>> print(turns[5])
          Start scores = (22, 74).
          Player 1 rolls 2 dice and gets outcomes [4, 4].
          End scores = (22, 82)
          >>> print(turns[6])
          Start scores = (22, 82).
          Player 0 rolls 5 dice and gets outcomes [5, 4, 4, 2, 4].
          End scores = (41, 82)
          >>> print(turns[7])
          Start scores = (41, 82).
          Player 1 rolls 4 dice and gets outcomes [2, 2, 3, 2].
          End scores = (41, 91)
          >>> print(turns[8])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=4714, score0=9, score1=3, goal=20, feral_hogs=True)
          >>> print(turns[0])
          Start scores = (9, 3).
          Player 0 rolls 2 dice and gets outcomes [3, 2].
          End scores = (17, 3)
          >>> print(turns[1])
          Start scores = (17, 3).
          Player 1 rolls 2 dice and gets outcomes [2, 6].
          End scores = (17, 14)
          >>> print(turns[2])
          Start scores = (17, 14).
          Player 0 rolls 6 dice and gets outcomes [4, 4, 6, 3, 2, 3].
          End scores = (39, 14)
          >>> print(turns[3])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=10742, score0=4, score1=25, goal=57, feral_hogs=True)
          >>> print(turns[0])
          Start scores = (4, 25).
          Player 0 rolls 8 dice and gets outcomes [2, 3, 1, 3, 6, 4, 3, 6].
          End scores = (5, 25)
          >>> print(turns[1])
          Start scores = (5, 25).
          Player 1 rolls 5 dice and gets outcomes [5, 3, 5, 6, 4].
          End scores = (5, 48)
          >>> print(turns[2])
          Start scores = (5, 48).
          Player 0 rolls 6 dice and gets outcomes [1, 3, 3, 2, 6, 6].
          End scores = (6, 48)
          >>> print(turns[3])
          Start scores = (6, 48).
          Player 1 rolls 9 dice and gets outcomes [4, 3, 5, 6, 1, 1, 3, 4, 2].
          End scores = (6, 49)
          >>> print(turns[4])
          Start scores = (6, 49).
          Player 0 rolls 9 dice and gets outcomes [5, 6, 2, 4, 5, 1, 2, 1, 2].
          End scores = (7, 49)
          >>> print(turns[5])
          Start scores = (7, 49).
          Player 1 rolls 6 dice and gets outcomes [6, 1, 3, 6, 4, 2].
          End scores = (7, 50)
          >>> print(turns[6])
          Start scores = (7, 50).
          Player 0 rolls 7 dice and gets outcomes [5, 1, 6, 1, 4, 1, 6].
          End scores = (8, 50)
          >>> print(turns[7])
          Start scores = (8, 50).
          Player 1 rolls 4 dice and gets outcomes [4, 6, 2, 3].
          End scores = (8, 65)
          >>> print(turns[8])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=5480, score0=5, score1=8, goal=77, feral_hogs=True)
          >>> print(turns[0])
          Start scores = (5, 8).
          Player 0 rolls 7 dice and gets outcomes [3, 6, 3, 3, 4, 4, 6].
          End scores = (34, 8)
          >>> print(turns[1])
          Start scores = (34, 8).
          Player 1 rolls 2 dice and gets outcomes [1, 4].
          End scores = (34, 12)
          >>> print(turns[2])
          Start scores = (34, 12).
          Player 0 rolls 4 dice and gets outcomes [2, 5, 4, 4].
          End scores = (49, 12)
          >>> print(turns[3])
          Start scores = (49, 12).
          Player 1 rolls 10 dice and gets outcomes [4, 4, 5, 1, 1, 2, 4, 5, 5, 4].
          End scores = (49, 13)
          >>> print(turns[4])
          Start scores = (49, 13).
          Player 0 rolls 9 dice and gets outcomes [5, 4, 1, 1, 2, 1, 3, 1, 4].
          End scores = (50, 13)
          >>> print(turns[5])
          Start scores = (50, 13).
          Player 1 rolls 1 dice and gets outcomes [3].
          End scores = (50, 16)
          >>> print(turns[6])
          Start scores = (50, 16).
          Player 0 rolls 5 dice and gets outcomes [6, 1, 5, 2, 4].
          End scores = (51, 16)
          >>> print(turns[7])
          Start scores = (51, 16).
          Player 1 rolls 9 dice and gets outcomes [4, 6, 4, 5, 6, 5, 2, 2, 3].
          End scores = (51, 53)
          >>> print(turns[8])
          Start scores = (51, 53).
          Player 0 rolls 3 dice and gets outcomes [5, 5, 2].
          End scores = (66, 53)
          >>> print(turns[9])
          Start scores = (66, 53).
          Player 1 rolls 6 dice and gets outcomes [3, 5, 1, 1, 4, 6].
          End scores = (66, 54)
          >>> print(turns[10])
          Start scores = (66, 54).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (77, 54)
          >>> print(turns[11])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=5014, score0=56, score1=59, goal=64, feral_hogs=True)
          >>> print(turns[0])
          Start scores = (56, 59).
          Player 0 rolls 6 dice and gets outcomes [1, 3, 1, 4, 5, 1].
          End scores = (57, 59)
          >>> print(turns[1])
          Start scores = (57, 59).
          Player 1 rolls 1 dice and gets outcomes [4].
          End scores = (57, 63)
          >>> print(turns[2])
          Start scores = (57, 63).
          Player 0 rolls 8 dice and gets outcomes [5, 6, 5, 4, 2, 5, 6, 5].
          End scores = (95, 63)
          >>> print(turns[3])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=50496, score0=4, score1=15, goal=19, feral_hogs=True)
          >>> print(turns[0])
          Start scores = (4, 15).
          Player 0 rolls 9 dice and gets outcomes [6, 4, 2, 6, 1, 5, 5, 2, 6].
          End scores = (5, 15)
          >>> print(turns[1])
          Start scores = (5, 15).
          Player 1 rolls 9 dice and gets outcomes [3, 1, 1, 4, 5, 1, 1, 6, 4].
          End scores = (5, 16)
          >>> print(turns[2])
          Start scores = (5, 16).
          Player 0 rolls 2 dice and gets outcomes [1, 6].
          End scores = (6, 16)
          >>> print(turns[3])
          Start scores = (6, 16).
          Player 1 rolls 9 dice and gets outcomes [6, 4, 1, 2, 5, 6, 1, 5, 6].
          End scores = (6, 17)
          >>> print(turns[4])
          Start scores = (6, 17).
          Player 0 rolls 1 dice and gets outcomes [1].
          End scores = (7, 17)
          >>> print(turns[5])
          Start scores = (7, 17).
          Player 1 rolls 2 dice and gets outcomes [5, 5].
          End scores = (27, 7)
          >>> print(turns[6])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=97617, score0=16, score1=27, goal=35, feral_hogs=True)
          >>> print(turns[0])
          Start scores = (16, 27).
          Player 0 rolls 6 dice and gets outcomes [4, 3, 5, 1, 5, 2].
          End scores = (17, 27)
          >>> print(turns[1])
          Start scores = (17, 27).
          Player 1 rolls 2 dice and gets outcomes [6, 2].
          End scores = (38, 17)
          >>> print(turns[2])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=19709, score0=27, score1=6, goal=85, feral_hogs=True)
          >>> print(turns[0])
          Start scores = (27, 6).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (31, 6)
          >>> print(turns[1])
          Start scores = (31, 6).
          Player 1 rolls 7 dice and gets outcomes [4, 4, 4, 1, 3, 6, 2].
          End scores = (31, 7)
          >>> print(turns[2])
          Start scores = (31, 7).
          Player 0 rolls 3 dice and gets outcomes [4, 4, 6].
          End scores = (45, 7)
          >>> print(turns[3])
          Start scores = (45, 7).
          Player 1 rolls 10 dice and gets outcomes [3, 1, 6, 2, 3, 4, 2, 4, 5, 6].
          End scores = (45, 8)
          >>> print(turns[4])
          Start scores = (45, 8).
          Player 0 rolls 1 dice and gets outcomes [1].
          End scores = (46, 8)
          >>> print(turns[5])
          Start scores = (46, 8).
          Player 1 rolls 8 dice and gets outcomes [1, 3, 4, 5, 2, 2, 2, 2].
          End scores = (46, 9)
          >>> print(turns[6])
          Start scores = (46, 9).
          Player 0 rolls 1 dice and gets outcomes [2].
          End scores = (48, 9)
          >>> print(turns[7])
          Start scores = (48, 9).
          Player 1 rolls 8 dice and gets outcomes [4, 2, 1, 2, 5, 3, 4, 2].
          End scores = (48, 10)
          >>> print(turns[8])
          Start scores = (48, 10).
          Player 0 rolls 3 dice and gets outcomes [4, 5, 4].
          End scores = (10, 61)
          >>> print(turns[9])
          Start scores = (10, 61).
          Player 1 rolls 2 dice and gets outcomes [6, 4].
          End scores = (71, 10)
          >>> print(turns[10])
          Start scores = (71, 10).
          Player 0 rolls 1 dice and gets outcomes [1].
          End scores = (72, 10)
          >>> print(turns[11])
          Start scores = (72, 10).
          Player 1 rolls 5 dice and gets outcomes [6, 2, 5, 2, 5].
          End scores = (72, 30)
          >>> print(turns[12])
          Start scores = (72, 30).
          Player 0 rolls 2 dice and gets outcomes [1, 6].
          End scores = (30, 73)
          >>> print(turns[13])
          Start scores = (30, 73).
          Player 1 rolls 2 dice and gets outcomes [1, 1].
          End scores = (30, 74)
          >>> print(turns[14])
          Start scores = (30, 74).
          Player 0 rolls 7 dice and gets outcomes [4, 1, 4, 3, 2, 6, 2].
          End scores = (31, 74)
          >>> print(turns[15])
          Start scores = (31, 74).
          Player 1 rolls 5 dice and gets outcomes [3, 6, 4, 4, 6].
          End scores = (31, 97)
          >>> print(turns[16])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=33634, score0=48, score1=74, goal=92, feral_hogs=False)
          >>> print(turns[0])
          Start scores = (48, 74).
          Player 0 rolls 8 dice and gets outcomes [3, 5, 1, 3, 3, 4, 3, 1].
          End scores = (49, 74)
          >>> print(turns[1])
          Start scores = (49, 74).
          Player 1 rolls 8 dice and gets outcomes [3, 6, 3, 3, 4, 6, 6, 2].
          End scores = (49, 107)
          >>> print(turns[2])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=22855, score0=12, score1=22, goal=98, feral_hogs=True)
          >>> print(turns[0])
          Start scores = (12, 22).
          Player 0 rolls 8 dice and gets outcomes [3, 6, 5, 3, 3, 2, 5, 3].
          End scores = (42, 22)
          >>> print(turns[1])
          Start scores = (42, 22).
          Player 1 rolls 6 dice and gets outcomes [3, 5, 2, 6, 4, 6].
          End scores = (42, 48)
          >>> print(turns[2])
          Start scores = (42, 48).
          Player 0 rolls 4 dice and gets outcomes [2, 3, 1, 4].
          End scores = (43, 48)
          >>> print(turns[3])
          Start scores = (43, 48).
          Player 1 rolls 8 dice and gets outcomes [4, 1, 4, 5, 5, 3, 1, 2].
          End scores = (43, 49)
          >>> print(turns[4])
          Start scores = (43, 49).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (48, 49)
          >>> print(turns[5])
          Start scores = (48, 49).
          Player 1 rolls 2 dice and gets outcomes [6, 6].
          End scores = (48, 61)
          >>> print(turns[6])
          Start scores = (48, 61).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (63, 61)
          >>> print(turns[7])
          Start scores = (63, 61).
          Player 1 rolls 2 dice and gets outcomes [2, 3].
          End scores = (63, 66)
          >>> print(turns[8])
          Start scores = (63, 66).
          Player 0 rolls 2 dice and gets outcomes [3, 4].
          End scores = (66, 70)
          >>> print(turns[9])
          Start scores = (66, 70).
          Player 1 rolls 0 dice and gets outcomes [].
          End scores = (80, 66)
          >>> print(turns[10])
          Start scores = (80, 66).
          Player 0 rolls 8 dice and gets outcomes [1, 3, 1, 2, 2, 5, 3, 2].
          End scores = (81, 66)
          >>> print(turns[11])
          Start scores = (81, 66).
          Player 1 rolls 10 dice and gets outcomes [4, 5, 4, 6, 6, 3, 5, 4, 3, 1].
          End scores = (81, 67)
          >>> print(turns[12])
          Start scores = (81, 67).
          Player 0 rolls 10 dice and gets outcomes [5, 2, 2, 6, 4, 2, 6, 5, 6, 4].
          End scores = (123, 67)
          >>> print(turns[13])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=49015, score0=12, score1=5, goal=82, feral_hogs=False)
          >>> print(turns[0])
          Start scores = (12, 5).
          Player 0 rolls 8 dice and gets outcomes [1, 3, 2, 1, 5, 1, 4, 1].
          End scores = (13, 5)
          >>> print(turns[1])
          Start scores = (13, 5).
          Player 1 rolls 10 dice and gets outcomes [1, 6, 2, 5, 5, 6, 5, 4, 1, 2].
          End scores = (13, 6)
          >>> print(turns[2])
          Start scores = (13, 6).
          Player 0 rolls 6 dice and gets outcomes [2, 4, 2, 4, 2, 5].
          End scores = (32, 6)
          >>> print(turns[3])
          Start scores = (32, 6).
          Player 1 rolls 4 dice and gets outcomes [3, 5, 6, 6].
          End scores = (32, 26)
          >>> print(turns[4])
          Start scores = (32, 26).
          Player 0 rolls 7 dice and gets outcomes [3, 5, 4, 5, 3, 2, 1].
          End scores = (33, 26)
          >>> print(turns[5])
          Start scores = (33, 26).
          Player 1 rolls 5 dice and gets outcomes [6, 3, 1, 4, 1].
          End scores = (33, 27)
          >>> print(turns[6])
          Start scores = (33, 27).
          Player 0 rolls 6 dice and gets outcomes [6, 4, 6, 2, 2, 4].
          End scores = (57, 27)
          >>> print(turns[7])
          Start scores = (57, 27).
          Player 1 rolls 5 dice and gets outcomes [6, 3, 4, 6, 2].
          End scores = (57, 48)
          >>> print(turns[8])
          Start scores = (57, 48).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (63, 48)
          >>> print(turns[9])
          Start scores = (63, 48).
          Player 1 rolls 6 dice and gets outcomes [6, 2, 5, 4, 4, 3].
          End scores = (63, 72)
          >>> print(turns[10])
          Start scores = (63, 72).
          Player 0 rolls 3 dice and gets outcomes [3, 3, 5].
          End scores = (74, 72)
          >>> print(turns[11])
          Start scores = (74, 72).
          Player 1 rolls 0 dice and gets outcomes [].
          End scores = (74, 85)
          >>> print(turns[12])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=50497, score0=46, score1=5, goal=51, feral_hogs=True)
          >>> print(turns[0])
          Start scores = (46, 5).
          Player 0 rolls 6 dice and gets outcomes [3, 3, 1, 2, 5, 2].
          End scores = (47, 5)
          >>> print(turns[1])
          Start scores = (47, 5).
          Player 1 rolls 3 dice and gets outcomes [4, 5, 6].
          End scores = (47, 20)
          >>> print(turns[2])
          Start scores = (47, 20).
          Player 0 rolls 8 dice and gets outcomes [6, 2, 3, 3, 3, 4, 2, 6].
          End scores = (76, 20)
          >>> print(turns[3])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=42297, score0=6, score1=22, goal=25, feral_hogs=False)
          >>> print(turns[0])
          Start scores = (6, 22).
          Player 0 rolls 2 dice and gets outcomes [6, 1].
          End scores = (7, 22)
          >>> print(turns[1])
          Start scores = (7, 22).
          Player 1 rolls 8 dice and gets outcomes [1, 2, 5, 1, 2, 2, 3, 4].
          End scores = (7, 23)
          >>> print(turns[2])
          Start scores = (7, 23).
          Player 0 rolls 10 dice and gets outcomes [3, 6, 4, 2, 1, 5, 2, 1, 2, 1].
          End scores = (8, 23)
          >>> print(turns[3])
          Start scores = (8, 23).
          Player 1 rolls 10 dice and gets outcomes [1, 1, 2, 5, 6, 5, 6, 4, 6, 4].
          End scores = (8, 24)
          >>> print(turns[4])
          Start scores = (8, 24).
          Player 0 rolls 8 dice and gets outcomes [3, 1, 6, 2, 5, 4, 1, 2].
          End scores = (9, 24)
          >>> print(turns[5])
          Start scores = (9, 24).
          Player 1 rolls 4 dice and gets outcomes [1, 1, 4, 3].
          End scores = (9, 25)
          >>> print(turns[6])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=1726, score0=19, score1=5, goal=52, feral_hogs=True)
          >>> print(turns[0])
          Start scores = (19, 5).
          Player 0 rolls 10 dice and gets outcomes [5, 1, 3, 4, 3, 1, 5, 1, 5, 3].
          End scores = (20, 5)
          >>> print(turns[1])
          Start scores = (20, 5).
          Player 1 rolls 1 dice and gets outcomes [2].
          End scores = (20, 7)
          >>> print(turns[2])
          Start scores = (20, 7).
          Player 0 rolls 10 dice and gets outcomes [2, 3, 3, 5, 6, 2, 6, 4, 6, 6].
          End scores = (63, 7)
          >>> print(turns[3])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=17218, score0=19, score1=10, goal=50, feral_hogs=False)
          >>> print(turns[0])
          Start scores = (19, 10).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (30, 10)
          >>> print(turns[1])
          Start scores = (30, 10).
          Player 1 rolls 1 dice and gets outcomes [3].
          End scores = (13, 30)
          >>> print(turns[2])
          Start scores = (13, 30).
          Player 0 rolls 4 dice and gets outcomes [1, 5, 2, 3].
          End scores = (14, 30)
          >>> print(turns[3])
          Start scores = (14, 30).
          Player 1 rolls 5 dice and gets outcomes [3, 5, 1, 1, 4].
          End scores = (14, 31)
          >>> print(turns[4])
          Start scores = (14, 31).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (26, 31)
          >>> print(turns[5])
          Start scores = (26, 31).
          Player 1 rolls 7 dice and gets outcomes [6, 3, 2, 6, 2, 2, 5].
          End scores = (26, 57)
          >>> print(turns[6])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=88988, score0=15, score1=95, goal=100, feral_hogs=False)
          >>> print(turns[0])
          Start scores = (15, 95).
          Player 0 rolls 9 dice and gets outcomes [5, 3, 2, 4, 2, 1, 3, 2, 5].
          End scores = (16, 95)
          >>> print(turns[1])
          Start scores = (16, 95).
          Player 1 rolls 10 dice and gets outcomes [6, 4, 3, 2, 6, 4, 6, 1, 2, 1].
          End scores = (16, 96)
          >>> print(turns[2])
          Start scores = (16, 96).
          Player 0 rolls 1 dice and gets outcomes [6].
          End scores = (22, 96)
          >>> print(turns[3])
          Start scores = (22, 96).
          Player 1 rolls 7 dice and gets outcomes [5, 1, 3, 1, 5, 6, 2].
          End scores = (22, 97)
          >>> print(turns[4])
          Start scores = (22, 97).
          Player 0 rolls 6 dice and gets outcomes [4, 2, 2, 3, 6, 1].
          End scores = (23, 97)
          >>> print(turns[5])
          Start scores = (23, 97).
          Player 1 rolls 4 dice and gets outcomes [4, 4, 1, 2].
          End scores = (23, 98)
          >>> print(turns[6])
          Start scores = (23, 98).
          Player 0 rolls 4 dice and gets outcomes [3, 1, 4, 5].
          End scores = (24, 98)
          >>> print(turns[7])
          Start scores = (24, 98).
          Player 1 rolls 7 dice and gets outcomes [6, 1, 1, 1, 6, 1, 5].
          End scores = (24, 99)
          >>> print(turns[8])
          Start scores = (24, 99).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (34, 99)
          >>> print(turns[9])
          Start scores = (34, 99).
          Player 1 rolls 6 dice and gets outcomes [6, 1, 3, 2, 4, 5].
          End scores = (34, 100)
          >>> print(turns[10])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=8964, score0=79, score1=56, goal=83, feral_hogs=False)
          >>> print(turns[0])
          Start scores = (79, 56).
          Player 0 rolls 7 dice and gets outcomes [5, 2, 3, 6, 6, 1, 6].
          End scores = (80, 56)
          >>> print(turns[1])
          Start scores = (80, 56).
          Player 1 rolls 4 dice and gets outcomes [1, 2, 5, 1].
          End scores = (80, 57)
          >>> print(turns[2])
          Start scores = (80, 57).
          Player 0 rolls 9 dice and gets outcomes [2, 5, 6, 3, 5, 6, 6, 1, 4].
          End scores = (81, 57)
          >>> print(turns[3])
          Start scores = (81, 57).
          Player 1 rolls 8 dice and gets outcomes [6, 3, 3, 3, 3, 2, 6, 3].
          End scores = (81, 86)
          >>> print(turns[4])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=24932, score0=12, score1=0, goal=14, feral_hogs=False)
          >>> print(turns[0])
          Start scores = (12, 0).
          Player 0 rolls 6 dice and gets outcomes [1, 1, 1, 3, 3, 2].
          End scores = (13, 0)
          >>> print(turns[1])
          Start scores = (13, 0).
          Player 1 rolls 8 dice and gets outcomes [4, 1, 5, 4, 3, 3, 5, 1].
          End scores = (13, 1)
          >>> print(turns[2])
          Start scores = (13, 1).
          Player 0 rolls 4 dice and gets outcomes [5, 3, 2, 3].
          End scores = (26, 1)
          >>> print(turns[3])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=76726, score0=40, score1=73, goal=93, feral_hogs=False)
          >>> print(turns[0])
          Start scores = (40, 73).
          Player 0 rolls 5 dice and gets outcomes [6, 6, 1, 2, 5].
          End scores = (41, 73)
          >>> print(turns[1])
          Start scores = (41, 73).
          Player 1 rolls 3 dice and gets outcomes [6, 1, 4].
          End scores = (41, 74)
          >>> print(turns[2])
          Start scores = (41, 74).
          Player 0 rolls 8 dice and gets outcomes [2, 1, 6, 1, 6, 4, 2, 5].
          End scores = (42, 74)
          >>> print(turns[3])
          Start scores = (42, 74).
          Player 1 rolls 10 dice and gets outcomes [4, 1, 6, 2, 5, 5, 3, 6, 1, 2].
          End scores = (42, 75)
          >>> print(turns[4])
          Start scores = (42, 75).
          Player 0 rolls 9 dice and gets outcomes [2, 5, 2, 4, 5, 6, 2, 5, 4].
          End scores = (77, 75)
          >>> print(turns[5])
          Start scores = (77, 75).
          Player 1 rolls 4 dice and gets outcomes [2, 3, 3, 6].
          End scores = (77, 89)
          >>> print(turns[6])
          Start scores = (77, 89).
          Player 0 rolls 8 dice and gets outcomes [3, 1, 2, 3, 3, 3, 1, 5].
          End scores = (78, 89)
          >>> print(turns[7])
          Start scores = (78, 89).
          Player 1 rolls 10 dice and gets outcomes [1, 1, 1, 5, 1, 4, 1, 2, 5, 3].
          End scores = (78, 90)
          >>> print(turns[8])
          Start scores = (78, 90).
          Player 0 rolls 3 dice and gets outcomes [1, 3, 4].
          End scores = (90, 79)
          >>> print(turns[9])
          Start scores = (90, 79).
          Player 1 rolls 10 dice and gets outcomes [4, 6, 1, 5, 6, 3, 3, 2, 3, 3].
          End scores = (90, 80)
          >>> print(turns[10])
          Start scores = (90, 80).
          Player 0 rolls 1 dice and gets outcomes [1].
          End scores = (91, 80)
          >>> print(turns[11])
          Start scores = (91, 80).
          Player 1 rolls 6 dice and gets outcomes [5, 4, 1, 6, 1, 4].
          End scores = (91, 81)
          >>> print(turns[12])
          Start scores = (91, 81).
          Player 0 rolls 2 dice and gets outcomes [2, 2].
          End scores = (95, 81)
          >>> print(turns[13])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=85393, score0=3, score1=0, goal=44, feral_hogs=True)
          >>> print(turns[0])
          Start scores = (3, 0).
          Player 0 rolls 3 dice and gets outcomes [3, 2, 5].
          End scores = (13, 0)
          >>> print(turns[1])
          Start scores = (13, 0).
          Player 1 rolls 6 dice and gets outcomes [1, 6, 3, 2, 6, 5].
          End scores = (13, 1)
          >>> print(turns[2])
          Start scores = (13, 1).
          Player 0 rolls 1 dice and gets outcomes [3].
          End scores = (16, 1)
          >>> print(turns[3])
          Start scores = (16, 1).
          Player 1 rolls 10 dice and gets outcomes [4, 2, 4, 6, 3, 2, 1, 1, 2, 3].
          End scores = (16, 2)
          >>> print(turns[4])
          Start scores = (16, 2).
          Player 0 rolls 2 dice and gets outcomes [4, 3].
          End scores = (23, 2)
          >>> print(turns[5])
          Start scores = (23, 2).
          Player 1 rolls 0 dice and gets outcomes [].
          End scores = (11, 23)
          >>> print(turns[6])
          Start scores = (11, 23).
          Player 0 rolls 10 dice and gets outcomes [2, 5, 1, 6, 1, 1, 1, 1, 6, 4].
          End scores = (12, 23)
          >>> print(turns[7])
          Start scores = (12, 23).
          Player 1 rolls 10 dice and gets outcomes [4, 3, 4, 4, 1, 6, 2, 3, 5, 1].
          End scores = (12, 24)
          >>> print(turns[8])
          Start scores = (12, 24).
          Player 0 rolls 7 dice and gets outcomes [1, 4, 6, 1, 3, 4, 6].
          End scores = (13, 24)
          >>> print(turns[9])
          Start scores = (13, 24).
          Player 1 rolls 0 dice and gets outcomes [].
          End scores = (32, 13)
          >>> print(turns[10])
          Start scores = (32, 13).
          Player 0 rolls 4 dice and gets outcomes [5, 3, 1, 1].
          End scores = (33, 13)
          >>> print(turns[11])
          Start scores = (33, 13).
          Player 1 rolls 5 dice and gets outcomes [2, 6, 3, 2, 4].
          End scores = (30, 33)
          >>> print(turns[12])
          Start scores = (30, 33).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (33, 40)
          >>> print(turns[13])
          Start scores = (33, 40).
          Player 1 rolls 4 dice and gets outcomes [1, 5, 4, 2].
          End scores = (33, 41)
          >>> print(turns[14])
          Start scores = (33, 41).
          Player 0 rolls 5 dice and gets outcomes [1, 1, 1, 4, 6].
          End scores = (34, 41)
          >>> print(turns[15])
          Start scores = (34, 41).
          Player 1 rolls 2 dice and gets outcomes [2, 5].
          End scores = (34, 48)
          >>> print(turns[16])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=35702, score0=10, score1=13, goal=14, feral_hogs=True)
          >>> print(turns[0])
          Start scores = (10, 13).
          Player 0 rolls 4 dice and gets outcomes [5, 4, 6, 2].
          End scores = (27, 13)
          >>> print(turns[1])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=75713, score0=62, score1=6, goal=63, feral_hogs=False)
          >>> print(turns[0])
          Start scores = (62, 6).
          Player 0 rolls 7 dice and gets outcomes [1, 6, 2, 6, 4, 4, 6].
          End scores = (63, 6)
          >>> print(turns[1])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=14879, score0=24, score1=8, goal=29, feral_hogs=False)
          >>> print(turns[0])
          Start scores = (24, 8).
          Player 0 rolls 4 dice and gets outcomes [1, 1, 6, 6].
          End scores = (25, 8)
          >>> print(turns[1])
          Start scores = (25, 8).
          Player 1 rolls 8 dice and gets outcomes [2, 6, 5, 1, 4, 6, 3, 4].
          End scores = (25, 9)
          >>> print(turns[2])
          Start scores = (25, 9).
          Player 0 rolls 3 dice and gets outcomes [6, 3, 3].
          End scores = (37, 9)
          >>> print(turns[3])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=62742, score0=9, score1=5, goal=11, feral_hogs=False)
          >>> print(turns[0])
          Start scores = (9, 5).
          Player 0 rolls 3 dice and gets outcomes [3, 2, 4].
          End scores = (18, 5)
          >>> print(turns[1])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=99168, score0=34, score1=40, goal=95, feral_hogs=True)
          >>> print(turns[0])
          Start scores = (34, 40).
          Player 0 rolls 1 dice and gets outcomes [1].
          End scores = (35, 40)
          >>> print(turns[1])
          Start scores = (35, 40).
          Player 1 rolls 3 dice and gets outcomes [5, 2, 5].
          End scores = (52, 35)
          >>> print(turns[2])
          Start scores = (52, 35).
          Player 0 rolls 7 dice and gets outcomes [1, 5, 5, 2, 6, 4, 4].
          End scores = (53, 35)
          >>> print(turns[3])
          Start scores = (53, 35).
          Player 1 rolls 7 dice and gets outcomes [3, 1, 4, 1, 5, 4, 4].
          End scores = (53, 36)
          >>> print(turns[4])
          Start scores = (53, 36).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (60, 36)
          >>> print(turns[5])
          Start scores = (60, 36).
          Player 1 rolls 5 dice and gets outcomes [6, 1, 3, 5, 5].
          End scores = (60, 37)
          >>> print(turns[6])
          Start scores = (60, 37).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (66, 37)
          >>> print(turns[7])
          Start scores = (66, 37).
          Player 1 rolls 4 dice and gets outcomes [2, 1, 5, 1].
          End scores = (66, 38)
          >>> print(turns[8])
          Start scores = (66, 38).
          Player 0 rolls 6 dice and gets outcomes [2, 2, 4, 5, 2, 1].
          End scores = (67, 38)
          >>> print(turns[9])
          Start scores = (67, 38).
          Player 1 rolls 3 dice and gets outcomes [5, 2, 6].
          End scores = (67, 54)
          >>> print(turns[10])
          Start scores = (67, 54).
          Player 0 rolls 1 dice and gets outcomes [1].
          End scores = (68, 54)
          >>> print(turns[11])
          Start scores = (68, 54).
          Player 1 rolls 5 dice and gets outcomes [6, 1, 1, 5, 1].
          End scores = (68, 55)
          >>> print(turns[12])
          Start scores = (68, 55).
          Player 0 rolls 5 dice and gets outcomes [1, 5, 3, 6, 3].
          End scores = (69, 55)
          >>> print(turns[13])
          Start scores = (69, 55).
          Player 1 rolls 4 dice and gets outcomes [6, 1, 3, 2].
          End scores = (69, 56)
          >>> print(turns[14])
          Start scores = (69, 56).
          Player 0 rolls 8 dice and gets outcomes [2, 3, 2, 4, 6, 2, 4, 1].
          End scores = (70, 56)
          >>> print(turns[15])
          Start scores = (70, 56).
          Player 1 rolls 0 dice and gets outcomes [].
          End scores = (70, 73)
          >>> print(turns[16])
          Start scores = (70, 73).
          Player 0 rolls 7 dice and gets outcomes [3, 2, 3, 3, 3, 5, 2].
          End scores = (91, 73)
          >>> print(turns[17])
          Start scores = (91, 73).
          Player 1 rolls 5 dice and gets outcomes [3, 1, 3, 1, 1].
          End scores = (91, 74)
          >>> print(turns[18])
          Start scores = (91, 74).
          Player 0 rolls 6 dice and gets outcomes [1, 6, 5, 3, 2, 1].
          End scores = (92, 74)
          >>> print(turns[19])
          Start scores = (92, 74).
          Player 1 rolls 4 dice and gets outcomes [1, 1, 2, 4].
          End scores = (92, 75)
          >>> print(turns[20])
          Start scores = (92, 75).
          Player 0 rolls 7 dice and gets outcomes [1, 5, 1, 6, 1, 5, 6].
          End scores = (93, 75)
          >>> print(turns[21])
          Start scores = (93, 75).
          Player 1 rolls 5 dice and gets outcomes [5, 2, 2, 4, 3].
          End scores = (93, 91)
          >>> print(turns[22])
          Start scores = (93, 91).
          Player 0 rolls 3 dice and gets outcomes [6, 5, 1].
          End scores = (97, 91)
          >>> print(turns[23])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=98804, score0=37, score1=45, goal=47, feral_hogs=False)
          >>> print(turns[0])
          Start scores = (37, 45).
          Player 0 rolls 4 dice and gets outcomes [1, 3, 3, 2].
          End scores = (38, 45)
          >>> print(turns[1])
          Start scores = (38, 45).
          Player 1 rolls 8 dice and gets outcomes [6, 5, 5, 3, 5, 5, 4, 3].
          End scores = (38, 81)
          >>> print(turns[2])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=27518, score0=87, score1=16, goal=92, feral_hogs=False)
          >>> print(turns[0])
          Start scores = (87, 16).
          Player 0 rolls 7 dice and gets outcomes [6, 1, 6, 6, 1, 5, 2].
          End scores = (88, 16)
          >>> print(turns[1])
          Start scores = (88, 16).
          Player 1 rolls 2 dice and gets outcomes [6, 1].
          End scores = (88, 17)
          >>> print(turns[2])
          Start scores = (88, 17).
          Player 0 rolls 10 dice and gets outcomes [6, 5, 4, 2, 4, 5, 5, 4, 2, 1].
          End scores = (89, 17)
          >>> print(turns[3])
          Start scores = (89, 17).
          Player 1 rolls 10 dice and gets outcomes [1, 1, 6, 2, 2, 2, 2, 3, 2, 2].
          End scores = (89, 18)
          >>> print(turns[4])
          Start scores = (89, 18).
          Player 0 rolls 4 dice and gets outcomes [6, 5, 1, 2].
          End scores = (90, 18)
          >>> print(turns[5])
          Start scores = (90, 18).
          Player 1 rolls 7 dice and gets outcomes [5, 1, 2, 2, 1, 3, 1].
          End scores = (19, 90)
          >>> print(turns[6])
          Start scores = (19, 90).
          Player 0 rolls 2 dice and gets outcomes [3, 5].
          End scores = (27, 90)
          >>> print(turns[7])
          Start scores = (27, 90).
          Player 1 rolls 8 dice and gets outcomes [4, 2, 6, 1, 6, 4, 1, 4].
          End scores = (27, 91)
          >>> print(turns[8])
          Start scores = (27, 91).
          Player 0 rolls 3 dice and gets outcomes [5, 6, 6].
          End scores = (44, 91)
          >>> print(turns[9])
          Start scores = (44, 91).
          Player 1 rolls 7 dice and gets outcomes [3, 5, 5, 5, 5, 6, 1].
          End scores = (44, 92)
          >>> print(turns[10])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=75062, score0=43, score1=5, goal=97, feral_hogs=False)
          >>> print(turns[0])
          Start scores = (43, 5).
          Player 0 rolls 8 dice and gets outcomes [6, 1, 4, 5, 6, 6, 5, 3].
          End scores = (44, 5)
          >>> print(turns[1])
          Start scores = (44, 5).
          Player 1 rolls 4 dice and gets outcomes [5, 5, 2, 4].
          End scores = (44, 21)
          >>> print(turns[2])
          Start scores = (44, 21).
          Player 0 rolls 3 dice and gets outcomes [6, 2, 1].
          End scores = (45, 21)
          >>> print(turns[3])
          Start scores = (45, 21).
          Player 1 rolls 9 dice and gets outcomes [1, 5, 3, 3, 4, 5, 5, 4, 6].
          End scores = (45, 22)
          >>> print(turns[4])
          Start scores = (45, 22).
          Player 0 rolls 6 dice and gets outcomes [1, 6, 6, 6, 5, 3].
          End scores = (46, 22)
          >>> print(turns[5])
          Start scores = (46, 22).
          Player 1 rolls 3 dice and gets outcomes [2, 5, 2].
          End scores = (46, 31)
          >>> print(turns[6])
          Start scores = (46, 31).
          Player 0 rolls 6 dice and gets outcomes [5, 3, 2, 6, 1, 1].
          End scores = (47, 31)
          >>> print(turns[7])
          Start scores = (47, 31).
          Player 1 rolls 9 dice and gets outcomes [5, 1, 4, 6, 5, 5, 1, 1, 4].
          End scores = (47, 32)
          >>> print(turns[8])
          Start scores = (47, 32).
          Player 0 rolls 9 dice and gets outcomes [1, 2, 5, 6, 6, 3, 6, 2, 2].
          End scores = (48, 32)
          >>> print(turns[9])
          Start scores = (48, 32).
          Player 1 rolls 9 dice and gets outcomes [5, 1, 4, 5, 4, 5, 5, 2, 1].
          End scores = (48, 33)
          >>> print(turns[10])
          Start scores = (48, 33).
          Player 0 rolls 4 dice and gets outcomes [6, 5, 1, 4].
          End scores = (49, 33)
          >>> print(turns[11])
          Start scores = (49, 33).
          Player 1 rolls 0 dice and gets outcomes [].
          End scores = (49, 38)
          >>> print(turns[12])
          Start scores = (49, 38).
          Player 0 rolls 9 dice and gets outcomes [2, 4, 5, 6, 2, 2, 5, 3, 6].
          End scores = (84, 38)
          >>> print(turns[13])
          Start scores = (84, 38).
          Player 1 rolls 7 dice and gets outcomes [5, 1, 3, 1, 3, 2, 3].
          End scores = (84, 39)
          >>> print(turns[14])
          Start scores = (84, 39).
          Player 0 rolls 8 dice and gets outcomes [6, 1, 6, 3, 1, 2, 3, 1].
          End scores = (85, 39)
          >>> print(turns[15])
          Start scores = (85, 39).
          Player 1 rolls 1 dice and gets outcomes [1].
          End scores = (85, 40)
          >>> print(turns[16])
          Start scores = (85, 40).
          Player 0 rolls 7 dice and gets outcomes [5, 2, 3, 5, 5, 5, 2].
          End scores = (112, 40)
          >>> print(turns[17])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=578, score0=7, score1=24, goal=30, feral_hogs=False)
          >>> print(turns[0])
          Start scores = (7, 24).
          Player 0 rolls 10 dice and gets outcomes [1, 1, 3, 2, 5, 2, 5, 6, 6, 2].
          End scores = (8, 24)
          >>> print(turns[1])
          Start scores = (8, 24).
          Player 1 rolls 2 dice and gets outcomes [6, 3].
          End scores = (8, 33)
          >>> print(turns[2])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=93942, score0=42, score1=41, goal=43, feral_hogs=True)
          >>> print(turns[0])
          Start scores = (42, 41).
          Player 0 rolls 7 dice and gets outcomes [3, 6, 3, 3, 2, 6, 1].
          End scores = (43, 41)
          >>> print(turns[1])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=48161, score0=15, score1=55, goal=83, feral_hogs=False)
          >>> print(turns[0])
          Start scores = (15, 55).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (25, 55)
          >>> print(turns[1])
          Start scores = (25, 55).
          Player 1 rolls 6 dice and gets outcomes [1, 4, 5, 6, 3, 6].
          End scores = (25, 56)
          >>> print(turns[2])
          Start scores = (25, 56).
          Player 0 rolls 5 dice and gets outcomes [5, 4, 2, 5, 3].
          End scores = (44, 56)
          >>> print(turns[3])
          Start scores = (44, 56).
          Player 1 rolls 1 dice and gets outcomes [1].
          End scores = (44, 57)
          >>> print(turns[4])
          Start scores = (44, 57).
          Player 0 rolls 1 dice and gets outcomes [3].
          End scores = (47, 57)
          >>> print(turns[5])
          Start scores = (47, 57).
          Player 1 rolls 6 dice and gets outcomes [4, 3, 1, 6, 6, 1].
          End scores = (47, 58)
          >>> print(turns[6])
          Start scores = (47, 58).
          Player 0 rolls 2 dice and gets outcomes [3, 2].
          End scores = (52, 58)
          >>> print(turns[7])
          Start scores = (52, 58).
          Player 1 rolls 0 dice and gets outcomes [].
          End scores = (52, 71)
          >>> print(turns[8])
          Start scores = (52, 71).
          Player 0 rolls 8 dice and gets outcomes [2, 5, 3, 6, 1, 3, 1, 2].
          End scores = (53, 71)
          >>> print(turns[9])
          Start scores = (53, 71).
          Player 1 rolls 7 dice and gets outcomes [5, 4, 5, 4, 5, 4, 4].
          End scores = (53, 102)
          >>> print(turns[10])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=52136, score0=2, score1=14, goal=15, feral_hogs=True)
          >>> print(turns[0])
          Start scores = (2, 14).
          Player 0 rolls 4 dice and gets outcomes [3, 3, 1, 5].
          End scores = (14, 3)
          >>> print(turns[1])
          Start scores = (14, 3).
          Player 1 rolls 7 dice and gets outcomes [1, 5, 2, 4, 6, 6, 1].
          End scores = (14, 4)
          >>> print(turns[2])
          Start scores = (14, 4).
          Player 0 rolls 7 dice and gets outcomes [6, 5, 4, 4, 3, 4, 6].
          End scores = (46, 4)
          >>> print(turns[3])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=30971, score0=11, score1=12, goal=25, feral_hogs=False)
          >>> print(turns[0])
          Start scores = (11, 12).
          Player 0 rolls 9 dice and gets outcomes [2, 2, 1, 2, 6, 5, 4, 6, 3].
          End scores = (12, 12)
          >>> print(turns[1])
          Start scores = (12, 12).
          Player 1 rolls 4 dice and gets outcomes [3, 6, 4, 1].
          End scores = (13, 12)
          >>> print(turns[2])
          Start scores = (13, 12).
          Player 0 rolls 1 dice and gets outcomes [3].
          End scores = (16, 12)
          >>> print(turns[3])
          Start scores = (16, 12).
          Player 1 rolls 5 dice and gets outcomes [3, 6, 5, 3, 5].
          End scores = (16, 34)
          >>> print(turns[4])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=69948, score0=11, score1=19, goal=43, feral_hogs=False)
          >>> print(turns[0])
          Start scores = (11, 19).
          Player 0 rolls 9 dice and gets outcomes [1, 5, 6, 6, 2, 6, 1, 6, 4].
          End scores = (12, 19)
          >>> print(turns[1])
          Start scores = (12, 19).
          Player 1 rolls 6 dice and gets outcomes [2, 3, 5, 6, 1, 3].
          End scores = (12, 20)
          >>> print(turns[2])
          Start scores = (12, 20).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (24, 20)
          >>> print(turns[3])
          Start scores = (24, 20).
          Player 1 rolls 6 dice and gets outcomes [1, 6, 4, 5, 6, 6].
          End scores = (24, 21)
          >>> print(turns[4])
          Start scores = (24, 21).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (35, 21)
          >>> print(turns[5])
          Start scores = (35, 21).
          Player 1 rolls 9 dice and gets outcomes [5, 6, 2, 3, 5, 4, 6, 5, 5].
          End scores = (62, 35)
          >>> print(turns[6])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=33856, score0=9, score1=9, goal=19, feral_hogs=False)
          >>> print(turns[0])
          Start scores = (9, 9).
          Player 0 rolls 1 dice and gets outcomes [3].
          End scores = (12, 9)
          >>> print(turns[1])
          Start scores = (12, 9).
          Player 1 rolls 3 dice and gets outcomes [5, 5, 6].
          End scores = (12, 25)
          >>> print(turns[2])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=93176, score0=7, score1=37, goal=80, feral_hogs=False)
          >>> print(turns[0])
          Start scores = (7, 37).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (13, 37)
          >>> print(turns[1])
          Start scores = (13, 37).
          Player 1 rolls 9 dice and gets outcomes [6, 6, 6, 6, 3, 6, 4, 6, 4].
          End scores = (84, 13)
          >>> print(turns[2])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=85986, score0=35, score1=12, goal=74, feral_hogs=False)
          >>> print(turns[0])
          Start scores = (35, 12).
          Player 0 rolls 10 dice and gets outcomes [6, 2, 3, 4, 3, 3, 6, 5, 1, 2].
          End scores = (36, 12)
          >>> print(turns[1])
          Start scores = (36, 12).
          Player 1 rolls 4 dice and gets outcomes [5, 3, 6, 1].
          End scores = (13, 36)
          >>> print(turns[2])
          Start scores = (13, 36).
          Player 0 rolls 5 dice and gets outcomes [2, 3, 3, 6, 4].
          End scores = (31, 36)
          >>> print(turns[3])
          Start scores = (31, 36).
          Player 1 rolls 7 dice and gets outcomes [2, 5, 1, 6, 3, 6, 4].
          End scores = (31, 37)
          >>> print(turns[4])
          Start scores = (31, 37).
          Player 0 rolls 6 dice and gets outcomes [3, 3, 5, 2, 2, 3].
          End scores = (49, 37)
          >>> print(turns[5])
          Start scores = (49, 37).
          Player 1 rolls 3 dice and gets outcomes [4, 5, 6].
          End scores = (49, 52)
          >>> print(turns[6])
          Start scores = (49, 52).
          Player 0 rolls 10 dice and gets outcomes [3, 6, 5, 5, 5, 3, 5, 5, 2, 4].
          End scores = (92, 52)
          >>> print(turns[7])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=76820, score0=28, score1=14, goal=61, feral_hogs=False)
          >>> print(turns[0])
          Start scores = (28, 14).
          Player 0 rolls 4 dice and gets outcomes [2, 6, 4, 1].
          End scores = (29, 14)
          >>> print(turns[1])
          Start scores = (29, 14).
          Player 1 rolls 0 dice and gets outcomes [].
          End scores = (17, 29)
          >>> print(turns[2])
          Start scores = (17, 29).
          Player 0 rolls 6 dice and gets outcomes [1, 1, 1, 3, 3, 6].
          End scores = (18, 29)
          >>> print(turns[3])
          Start scores = (18, 29).
          Player 1 rolls 5 dice and gets outcomes [6, 6, 4, 2, 5].
          End scores = (18, 52)
          >>> print(turns[4])
          Start scores = (18, 52).
          Player 0 rolls 3 dice and gets outcomes [4, 1, 5].
          End scores = (19, 52)
          >>> print(turns[5])
          Start scores = (19, 52).
          Player 1 rolls 7 dice and gets outcomes [5, 3, 6, 5, 4, 4, 5].
          End scores = (19, 84)
          >>> print(turns[6])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=83984, score0=64, score1=49, goal=78, feral_hogs=True)
          >>> print(turns[0])
          Start scores = (64, 49).
          Player 0 rolls 7 dice and gets outcomes [3, 5, 3, 5, 6, 3, 4].
          End scores = (93, 49)
          >>> print(turns[1])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=25773, score0=3, score1=17, goal=30, feral_hogs=True)
          >>> print(turns[0])
          Start scores = (3, 17).
          Player 0 rolls 5 dice and gets outcomes [3, 4, 5, 4, 6].
          End scores = (25, 17)
          >>> print(turns[1])
          Start scores = (25, 17).
          Player 1 rolls 3 dice and gets outcomes [2, 1, 4].
          End scores = (25, 18)
          >>> print(turns[2])
          Start scores = (25, 18).
          Player 0 rolls 4 dice and gets outcomes [5, 1, 5, 3].
          End scores = (26, 18)
          >>> print(turns[3])
          Start scores = (26, 18).
          Player 1 rolls 8 dice and gets outcomes [1, 4, 3, 2, 1, 5, 6, 2].
          End scores = (26, 19)
          >>> print(turns[4])
          Start scores = (26, 19).
          Player 0 rolls 9 dice and gets outcomes [6, 5, 6, 2, 1, 5, 2, 1, 1].
          End scores = (27, 19)
          >>> print(turns[5])
          Start scores = (27, 19).
          Player 1 rolls 10 dice and gets outcomes [5, 6, 6, 4, 2, 5, 3, 3, 2, 4].
          End scores = (59, 27)
          >>> print(turns[6])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=6012, score0=30, score1=3, goal=85, feral_hogs=False)
          >>> print(turns[0])
          Start scores = (30, 3).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (37, 3)
          >>> print(turns[1])
          Start scores = (37, 3).
          Player 1 rolls 1 dice and gets outcomes [1].
          End scores = (4, 37)
          >>> print(turns[2])
          Start scores = (4, 37).
          Player 0 rolls 5 dice and gets outcomes [4, 6, 2, 4, 2].
          End scores = (22, 37)
          >>> print(turns[3])
          Start scores = (22, 37).
          Player 1 rolls 7 dice and gets outcomes [4, 2, 4, 3, 3, 4, 6].
          End scores = (22, 63)
          >>> print(turns[4])
          Start scores = (22, 63).
          Player 0 rolls 5 dice and gets outcomes [4, 4, 6, 6, 6].
          End scores = (48, 63)
          >>> print(turns[5])
          Start scores = (48, 63).
          Player 1 rolls 7 dice and gets outcomes [5, 5, 1, 1, 4, 2, 4].
          End scores = (64, 48)
          >>> print(turns[6])
          Start scores = (64, 48).
          Player 0 rolls 8 dice and gets outcomes [5, 3, 3, 4, 1, 1, 5, 6].
          End scores = (65, 48)
          >>> print(turns[7])
          Start scores = (65, 48).
          Player 1 rolls 0 dice and gets outcomes [].
          End scores = (65, 59)
          >>> print(turns[8])
          Start scores = (65, 59).
          Player 0 rolls 3 dice and gets outcomes [1, 1, 6].
          End scores = (66, 59)
          >>> print(turns[9])
          Start scores = (66, 59).
          Player 1 rolls 9 dice and gets outcomes [1, 6, 1, 6, 1, 1, 3, 2, 2].
          End scores = (60, 66)
          >>> print(turns[10])
          Start scores = (60, 66).
          Player 0 rolls 2 dice and gets outcomes [6, 3].
          End scores = (69, 66)
          >>> print(turns[11])
          Start scores = (69, 66).
          Player 1 rolls 0 dice and gets outcomes [].
          End scores = (73, 69)
          >>> print(turns[12])
          Start scores = (73, 69).
          Player 0 rolls 1 dice and gets outcomes [6].
          End scores = (79, 69)
          >>> print(turns[13])
          Start scores = (79, 69).
          Player 1 rolls 8 dice and gets outcomes [5, 1, 4, 4, 1, 4, 6, 4].
          End scores = (79, 70)
          >>> print(turns[14])
          Start scores = (79, 70).
          Player 0 rolls 2 dice and gets outcomes [4, 2].
          End scores = (85, 70)
          >>> print(turns[15])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=56692, score0=69, score1=40, goal=71, feral_hogs=False)
          >>> print(turns[0])
          Start scores = (69, 40).
          Player 0 rolls 6 dice and gets outcomes [6, 4, 6, 4, 4, 1].
          End scores = (70, 40)
          >>> print(turns[1])
          Start scores = (70, 40).
          Player 1 rolls 3 dice and gets outcomes [3, 3, 4].
          End scores = (70, 50)
          >>> print(turns[2])
          Start scores = (70, 50).
          Player 0 rolls 4 dice and gets outcomes [5, 5, 6, 2].
          End scores = (88, 50)
          >>> print(turns[3])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=11528, score0=6, score1=7, goal=17, feral_hogs=False)
          >>> print(turns[0])
          Start scores = (6, 7).
          Player 0 rolls 3 dice and gets outcomes [2, 6, 2].
          End scores = (16, 7)
          >>> print(turns[1])
          Start scores = (16, 7).
          Player 1 rolls 8 dice and gets outcomes [6, 3, 1, 5, 2, 6, 5, 5].
          End scores = (16, 8)
          >>> print(turns[2])
          Start scores = (16, 8).
          Player 0 rolls 4 dice and gets outcomes [5, 2, 2, 1].
          End scores = (17, 8)
          >>> print(turns[3])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=95684, score0=3, score1=1, goal=10, feral_hogs=True)
          >>> print(turns[0])
          Start scores = (3, 1).
          Player 0 rolls 1 dice and gets outcomes [3].
          End scores = (6, 1)
          >>> print(turns[1])
          Start scores = (6, 1).
          Player 1 rolls 8 dice and gets outcomes [4, 1, 3, 5, 1, 6, 2, 6].
          End scores = (6, 2)
          >>> print(turns[2])
          Start scores = (6, 2).
          Player 0 rolls 5 dice and gets outcomes [1, 4, 5, 5, 4].
          End scores = (10, 2)
          >>> print(turns[3])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=81397, score0=45, score1=40, goal=52, feral_hogs=False)
          >>> print(turns[0])
          Start scores = (45, 40).
          Player 0 rolls 3 dice and gets outcomes [6, 5, 3].
          End scores = (59, 40)
          >>> print(turns[1])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=22637, score0=32, score1=11, goal=58, feral_hogs=True)
          >>> print(turns[0])
          Start scores = (32, 11).
          Player 0 rolls 5 dice and gets outcomes [6, 6, 5, 5, 5].
          End scores = (59, 11)
          >>> print(turns[1])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=11998, score0=16, score1=21, goal=67, feral_hogs=False)
          >>> print(turns[0])
          Start scores = (16, 21).
          Player 0 rolls 1 dice and gets outcomes [4].
          End scores = (20, 21)
          >>> print(turns[1])
          Start scores = (20, 21).
          Player 1 rolls 0 dice and gets outcomes [].
          End scores = (20, 33)
          >>> print(turns[2])
          Start scores = (20, 33).
          Player 0 rolls 2 dice and gets outcomes [2, 3].
          End scores = (25, 33)
          >>> print(turns[3])
          Start scores = (25, 33).
          Player 1 rolls 7 dice and gets outcomes [5, 6, 3, 3, 6, 2, 1].
          End scores = (25, 34)
          >>> print(turns[4])
          Start scores = (25, 34).
          Player 0 rolls 2 dice and gets outcomes [6, 4].
          End scores = (35, 34)
          >>> print(turns[5])
          Start scores = (35, 34).
          Player 1 rolls 8 dice and gets outcomes [5, 3, 4, 6, 2, 3, 4, 2].
          End scores = (35, 63)
          >>> print(turns[6])
          Start scores = (35, 63).
          Player 0 rolls 3 dice and gets outcomes [3, 4, 3].
          End scores = (45, 63)
          >>> print(turns[7])
          Start scores = (45, 63).
          Player 1 rolls 8 dice and gets outcomes [6, 2, 5, 6, 4, 6, 2, 6].
          End scores = (45, 100)
          >>> print(turns[8])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=69783, score0=11, score1=13, goal=38, feral_hogs=False)
          >>> print(turns[0])
          Start scores = (11, 13).
          Player 0 rolls 2 dice and gets outcomes [4, 6].
          End scores = (21, 13)
          >>> print(turns[1])
          Start scores = (21, 13).
          Player 1 rolls 1 dice and gets outcomes [6].
          End scores = (21, 19)
          >>> print(turns[2])
          Start scores = (21, 19).
          Player 0 rolls 8 dice and gets outcomes [4, 4, 5, 6, 4, 3, 5, 1].
          End scores = (22, 19)
          >>> print(turns[3])
          Start scores = (22, 19).
          Player 1 rolls 7 dice and gets outcomes [1, 1, 6, 6, 3, 6, 5].
          End scores = (20, 22)
          >>> print(turns[4])
          Start scores = (20, 22).
          Player 0 rolls 10 dice and gets outcomes [5, 4, 3, 6, 5, 3, 1, 2, 2, 4].
          End scores = (21, 22)
          >>> print(turns[5])
          Start scores = (21, 22).
          Player 1 rolls 8 dice and gets outcomes [5, 2, 4, 1, 4, 5, 1, 5].
          End scores = (23, 21)
          >>> print(turns[6])
          Start scores = (23, 21).
          Player 0 rolls 7 dice and gets outcomes [4, 1, 3, 4, 3, 3, 5].
          End scores = (24, 21)
          >>> print(turns[7])
          Start scores = (24, 21).
          Player 1 rolls 7 dice and gets outcomes [2, 6, 2, 1, 3, 3, 1].
          End scores = (22, 24)
          >>> print(turns[8])
          Start scores = (22, 24).
          Player 0 rolls 9 dice and gets outcomes [2, 6, 5, 3, 5, 3, 5, 5, 3].
          End scores = (59, 24)
          >>> print(turns[9])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=37364, score0=29, score1=22, goal=35, feral_hogs=True)
          >>> print(turns[0])
          Start scores = (29, 22).
          Player 0 rolls 4 dice and gets outcomes [1, 6, 1, 6].
          End scores = (22, 30)
          >>> print(turns[1])
          Start scores = (22, 30).
          Player 1 rolls 0 dice and gets outcomes [].
          End scores = (40, 22)
          >>> print(turns[2])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=5143, score0=2, score1=15, goal=79, feral_hogs=True)
          >>> print(turns[0])
          Start scores = (2, 15).
          Player 0 rolls 5 dice and gets outcomes [4, 6, 6, 6, 4].
          End scores = (28, 15)
          >>> print(turns[1])
          Start scores = (28, 15).
          Player 1 rolls 1 dice and gets outcomes [4].
          End scores = (28, 19)
          >>> print(turns[2])
          Start scores = (28, 19).
          Player 0 rolls 5 dice and gets outcomes [3, 3, 2, 3, 4].
          End scores = (43, 19)
          >>> print(turns[3])
          Start scores = (43, 19).
          Player 1 rolls 6 dice and gets outcomes [6, 2, 2, 2, 4, 3].
          End scores = (43, 41)
          >>> print(turns[4])
          Start scores = (43, 41).
          Player 0 rolls 8 dice and gets outcomes [3, 3, 6, 1, 4, 5, 1, 5].
          End scores = (44, 41)
          >>> print(turns[5])
          Start scores = (44, 41).
          Player 1 rolls 4 dice and gets outcomes [5, 3, 2, 1].
          End scores = (44, 42)
          >>> print(turns[6])
          Start scores = (44, 42).
          Player 0 rolls 9 dice and gets outcomes [2, 6, 2, 1, 5, 2, 5, 3, 3].
          End scores = (45, 42)
          >>> print(turns[7])
          Start scores = (45, 42).
          Player 1 rolls 10 dice and gets outcomes [2, 4, 4, 4, 2, 4, 6, 2, 5, 6].
          End scores = (81, 45)
          >>> print(turns[8])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=82888, score0=26, score1=39, goal=87, feral_hogs=True)
          >>> print(turns[0])
          Start scores = (26, 39).
          Player 0 rolls 9 dice and gets outcomes [4, 4, 3, 4, 3, 6, 5, 2, 6].
          End scores = (63, 39)
          >>> print(turns[1])
          Start scores = (63, 39).
          Player 1 rolls 2 dice and gets outcomes [6, 6].
          End scores = (63, 54)
          >>> print(turns[2])
          Start scores = (63, 54).
          Player 0 rolls 4 dice and gets outcomes [3, 1, 2, 4].
          End scores = (64, 54)
          >>> print(turns[3])
          Start scores = (64, 54).
          Player 1 rolls 4 dice and gets outcomes [4, 5, 5, 4].
          End scores = (64, 72)
          >>> print(turns[4])
          Start scores = (64, 72).
          Player 0 rolls 3 dice and gets outcomes [4, 2, 2].
          End scores = (75, 72)
          >>> print(turns[5])
          Start scores = (75, 72).
          Player 1 rolls 5 dice and gets outcomes [5, 3, 3, 4, 1].
          End scores = (75, 73)
          >>> print(turns[6])
          Start scores = (75, 73).
          Player 0 rolls 8 dice and gets outcomes [2, 6, 1, 6, 2, 1, 4, 3].
          End scores = (76, 73)
          >>> print(turns[7])
          Start scores = (76, 73).
          Player 1 rolls 3 dice and gets outcomes [1, 4, 1].
          End scores = (76, 77)
          >>> print(turns[8])
          Start scores = (76, 77).
          Player 0 rolls 7 dice and gets outcomes [1, 6, 3, 2, 5, 5, 2].
          End scores = (77, 77)
          >>> print(turns[9])
          Start scores = (77, 77).
          Player 1 rolls 2 dice and gets outcomes [1, 2].
          End scores = (77, 78)
          >>> print(turns[10])
          Start scores = (77, 78).
          Player 0 rolls 3 dice and gets outcomes [4, 2, 3].
          End scores = (89, 78)
          >>> print(turns[11])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=25835, score0=15, score1=64, goal=95, feral_hogs=False)
          >>> print(turns[0])
          Start scores = (15, 64).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (27, 64)
          >>> print(turns[1])
          Start scores = (27, 64).
          Player 1 rolls 2 dice and gets outcomes [3, 2].
          End scores = (69, 27)
          >>> print(turns[2])
          Start scores = (69, 27).
          Player 0 rolls 6 dice and gets outcomes [3, 4, 3, 1, 2, 1].
          End scores = (70, 27)
          >>> print(turns[3])
          Start scores = (70, 27).
          Player 1 rolls 5 dice and gets outcomes [3, 1, 6, 6, 4].
          End scores = (70, 28)
          >>> print(turns[4])
          Start scores = (70, 28).
          Player 0 rolls 1 dice and gets outcomes [4].
          End scores = (74, 28)
          >>> print(turns[5])
          Start scores = (74, 28).
          Player 1 rolls 0 dice and gets outcomes [].
          End scores = (74, 41)
          >>> print(turns[6])
          Start scores = (74, 41).
          Player 0 rolls 6 dice and gets outcomes [2, 3, 4, 2, 5, 3].
          End scores = (93, 41)
          >>> print(turns[7])
          Start scores = (93, 41).
          Player 1 rolls 5 dice and gets outcomes [1, 6, 6, 4, 5].
          End scores = (93, 42)
          >>> print(turns[8])
          Start scores = (93, 42).
          Player 0 rolls 6 dice and gets outcomes [5, 4, 2, 2, 1, 3].
          End scores = (94, 42)
          >>> print(turns[9])
          Start scores = (94, 42).
          Player 1 rolls 8 dice and gets outcomes [5, 2, 1, 6, 3, 5, 2, 2].
          End scores = (94, 43)
          >>> print(turns[10])
          Start scores = (94, 43).
          Player 0 rolls 3 dice and gets outcomes [4, 1, 3].
          End scores = (95, 43)
          >>> print(turns[11])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=85071, score0=86, score1=5, goal=89, feral_hogs=False)
          >>> print(turns[0])
          Start scores = (86, 5).
          Player 0 rolls 7 dice and gets outcomes [1, 3, 2, 6, 4, 5, 6].
          End scores = (87, 5)
          >>> print(turns[1])
          Start scores = (87, 5).
          Player 1 rolls 0 dice and gets outcomes [].
          End scores = (87, 16)
          >>> print(turns[2])
          Start scores = (87, 16).
          Player 0 rolls 8 dice and gets outcomes [6, 6, 1, 3, 5, 6, 6, 5].
          End scores = (88, 16)
          >>> print(turns[3])
          Start scores = (88, 16).
          Player 1 rolls 2 dice and gets outcomes [5, 3].
          End scores = (88, 24)
          >>> print(turns[4])
          Start scores = (88, 24).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (24, 96)
          >>> print(turns[5])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=23577, score0=32, score1=23, goal=45, feral_hogs=False)
          >>> print(turns[0])
          Start scores = (32, 23).
          Player 0 rolls 7 dice and gets outcomes [1, 4, 6, 5, 3, 6, 4].
          End scores = (33, 23)
          >>> print(turns[1])
          Start scores = (33, 23).
          Player 1 rolls 8 dice and gets outcomes [2, 1, 3, 5, 3, 6, 6, 5].
          End scores = (33, 24)
          >>> print(turns[2])
          Start scores = (33, 24).
          Player 0 rolls 1 dice and gets outcomes [1].
          End scores = (34, 24)
          >>> print(turns[3])
          Start scores = (34, 24).
          Player 1 rolls 7 dice and gets outcomes [4, 4, 5, 2, 6, 4, 2].
          End scores = (51, 34)
          >>> print(turns[4])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=663, score0=44, score1=13, goal=59, feral_hogs=True)
          >>> print(turns[0])
          Start scores = (44, 13).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (13, 52)
          >>> print(turns[1])
          Start scores = (13, 52).
          Player 1 rolls 1 dice and gets outcomes [5].
          End scores = (13, 57)
          >>> print(turns[2])
          Start scores = (13, 57).
          Player 0 rolls 1 dice and gets outcomes [6].
          End scores = (19, 57)
          >>> print(turns[3])
          Start scores = (19, 57).
          Player 1 rolls 7 dice and gets outcomes [6, 4, 5, 3, 5, 5, 6].
          End scores = (19, 94)
          >>> print(turns[4])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=6543, score0=65, score1=70, goal=87, feral_hogs=True)
          >>> print(turns[0])
          Start scores = (65, 70).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (82, 70)
          >>> print(turns[1])
          Start scores = (82, 70).
          Player 1 rolls 6 dice and gets outcomes [5, 3, 3, 3, 2, 3].
          End scores = (82, 89)
          >>> print(turns[2])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=31919, score0=2, score1=16, goal=28, feral_hogs=False)
          >>> print(turns[0])
          Start scores = (2, 16).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (16, 7)
          >>> print(turns[1])
          Start scores = (16, 7).
          Player 1 rolls 2 dice and gets outcomes [5, 6].
          End scores = (16, 18)
          >>> print(turns[2])
          Start scores = (16, 18).
          Player 0 rolls 5 dice and gets outcomes [2, 2, 3, 2, 5].
          End scores = (30, 18)
          >>> print(turns[3])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=67699, score0=24, score1=17, goal=28, feral_hogs=True)
          >>> print(turns[0])
          Start scores = (24, 17).
          Player 0 rolls 5 dice and gets outcomes [2, 1, 3, 6, 6].
          End scores = (25, 17)
          >>> print(turns[1])
          Start scores = (25, 17).
          Player 1 rolls 2 dice and gets outcomes [4, 3].
          End scores = (27, 25)
          >>> print(turns[2])
          Start scores = (27, 25).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (34, 25)
          >>> print(turns[3])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=25815, score0=52, score1=11, goal=54, feral_hogs=False)
          >>> print(turns[0])
          Start scores = (52, 11).
          Player 0 rolls 9 dice and gets outcomes [5, 5, 5, 4, 2, 4, 3, 1, 5].
          End scores = (53, 11)
          >>> print(turns[1])
          Start scores = (53, 11).
          Player 1 rolls 5 dice and gets outcomes [1, 2, 1, 2, 6].
          End scores = (53, 12)
          >>> print(turns[2])
          Start scores = (53, 12).
          Player 0 rolls 6 dice and gets outcomes [4, 5, 6, 3, 1, 4].
          End scores = (54, 12)
          >>> print(turns[3])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=41969, score0=38, score1=54, goal=78, feral_hogs=False)
          >>> print(turns[0])
          Start scores = (38, 54).
          Player 0 rolls 1 dice and gets outcomes [1].
          End scores = (54, 39)
          >>> print(turns[1])
          Start scores = (54, 39).
          Player 1 rolls 9 dice and gets outcomes [1, 2, 5, 6, 2, 4, 1, 4, 5].
          End scores = (54, 40)
          >>> print(turns[2])
          Start scores = (54, 40).
          Player 0 rolls 7 dice and gets outcomes [6, 4, 2, 2, 5, 2, 3].
          End scores = (78, 40)
          >>> print(turns[3])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=68309, score0=53, score1=40, goal=56, feral_hogs=True)
          >>> print(turns[0])
          Start scores = (53, 40).
          Player 0 rolls 7 dice and gets outcomes [2, 4, 3, 5, 6, 2, 2].
          End scores = (77, 40)
          >>> print(turns[1])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=8243, score0=28, score1=23, goal=30, feral_hogs=False)
          >>> print(turns[0])
          Start scores = (28, 23).
          Player 0 rolls 6 dice and gets outcomes [4, 2, 5, 2, 6, 5].
          End scores = (52, 23)
          >>> print(turns[1])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=43015, score0=53, score1=74, goal=77, feral_hogs=True)
          >>> print(turns[0])
          Start scores = (53, 74).
          Player 0 rolls 10 dice and gets outcomes [5, 6, 6, 6, 1, 4, 3, 5, 3, 2].
          End scores = (54, 74)
          >>> print(turns[1])
          Start scores = (54, 74).
          Player 1 rolls 5 dice and gets outcomes [1, 6, 5, 4, 6].
          End scores = (54, 75)
          >>> print(turns[2])
          Start scores = (54, 75).
          Player 0 rolls 9 dice and gets outcomes [2, 3, 2, 4, 4, 6, 4, 5, 3].
          End scores = (87, 75)
          >>> print(turns[3])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=76012, score0=39, score1=36, goal=73, feral_hogs=False)
          >>> print(turns[0])
          Start scores = (39, 36).
          Player 0 rolls 2 dice and gets outcomes [1, 4].
          End scores = (40, 36)
          >>> print(turns[1])
          Start scores = (40, 36).
          Player 1 rolls 2 dice and gets outcomes [6, 6].
          End scores = (40, 48)
          >>> print(turns[2])
          Start scores = (40, 48).
          Player 0 rolls 4 dice and gets outcomes [6, 6, 6, 2].
          End scores = (60, 48)
          >>> print(turns[3])
          Start scores = (60, 48).
          Player 1 rolls 8 dice and gets outcomes [1, 3, 3, 2, 3, 5, 3, 6].
          End scores = (60, 49)
          >>> print(turns[4])
          Start scores = (60, 49).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (49, 65)
          >>> print(turns[5])
          Start scores = (49, 65).
          Player 1 rolls 2 dice and gets outcomes [2, 6].
          End scores = (49, 73)
          >>> print(turns[6])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=9818, score0=11, score1=9, goal=64, feral_hogs=True)
          >>> print(turns[0])
          Start scores = (11, 9).
          Player 0 rolls 10 dice and gets outcomes [2, 5, 3, 3, 6, 6, 4, 1, 1, 2].
          End scores = (12, 9)
          >>> print(turns[1])
          Start scores = (12, 9).
          Player 1 rolls 4 dice and gets outcomes [4, 1, 2, 6].
          End scores = (12, 10)
          >>> print(turns[2])
          Start scores = (12, 10).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (23, 10)
          >>> print(turns[3])
          Start scores = (23, 10).
          Player 1 rolls 4 dice and gets outcomes [3, 4, 2, 6].
          End scores = (25, 23)
          >>> print(turns[4])
          Start scores = (25, 23).
          Player 0 rolls 9 dice and gets outcomes [5, 5, 4, 2, 3, 3, 6, 6, 3].
          End scores = (23, 65)
          >>> print(turns[5])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=25916, score0=86, score1=24, goal=88, feral_hogs=True)
          >>> print(turns[0])
          Start scores = (86, 24).
          Player 0 rolls 5 dice and gets outcomes [4, 1, 5, 5, 1].
          End scores = (87, 24)
          >>> print(turns[1])
          Start scores = (87, 24).
          Player 1 rolls 8 dice and gets outcomes [5, 4, 4, 2, 5, 2, 2, 2].
          End scores = (87, 50)
          >>> print(turns[2])
          Start scores = (87, 50).
          Player 0 rolls 7 dice and gets outcomes [1, 2, 4, 1, 6, 4, 2].
          End scores = (88, 50)
          >>> print(turns[3])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=15583, score0=11, score1=40, goal=55, feral_hogs=True)
          >>> print(turns[0])
          Start scores = (11, 40).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (25, 40)
          >>> print(turns[1])
          Start scores = (25, 40).
          Player 1 rolls 6 dice and gets outcomes [1, 2, 3, 5, 4, 4].
          End scores = (25, 41)
          >>> print(turns[2])
          Start scores = (25, 41).
          Player 0 rolls 6 dice and gets outcomes [2, 5, 1, 2, 1, 2].
          End scores = (26, 41)
          >>> print(turns[3])
          Start scores = (26, 41).
          Player 1 rolls 1 dice and gets outcomes [1].
          End scores = (26, 42)
          >>> print(turns[4])
          Start scores = (26, 42).
          Player 0 rolls 3 dice and gets outcomes [4, 6, 4].
          End scores = (43, 42)
          >>> print(turns[5])
          Start scores = (43, 42).
          Player 1 rolls 8 dice and gets outcomes [2, 1, 3, 3, 5, 4, 3, 4].
          End scores = (43, 43)
          >>> print(turns[6])
          Start scores = (43, 43).
          Player 0 rolls 6 dice and gets outcomes [1, 3, 5, 2, 2, 2].
          End scores = (44, 43)
          >>> print(turns[7])
          Start scores = (44, 43).
          Player 1 rolls 10 dice and gets outcomes [5, 4, 1, 4, 4, 4, 3, 5, 1, 3].
          End scores = (44, 44)
          >>> print(turns[8])
          Start scores = (44, 44).
          Player 0 rolls 10 dice and gets outcomes [5, 2, 4, 1, 6, 5, 3, 6, 3, 6].
          End scores = (45, 44)
          >>> print(turns[9])
          Start scores = (45, 44).
          Player 1 rolls 7 dice and gets outcomes [1, 4, 5, 6, 2, 2, 5].
          End scores = (45, 45)
          >>> print(turns[10])
          Start scores = (45, 45).
          Player 0 rolls 1 dice and gets outcomes [3].
          End scores = (48, 45)
          >>> print(turns[11])
          Start scores = (48, 45).
          Player 1 rolls 1 dice and gets outcomes [4].
          End scores = (48, 49)
          >>> print(turns[12])
          Start scores = (48, 49).
          Player 0 rolls 8 dice and gets outcomes [4, 5, 3, 4, 2, 6, 2, 4].
          End scores = (78, 49)
          >>> print(turns[13])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=7242, score0=19, score1=46, goal=98, feral_hogs=True)
          >>> print(turns[0])
          Start scores = (19, 46).
          Player 0 rolls 8 dice and gets outcomes [2, 2, 3, 5, 4, 1, 1, 3].
          End scores = (20, 46)
          >>> print(turns[1])
          Start scores = (20, 46).
          Player 1 rolls 8 dice and gets outcomes [1, 1, 6, 6, 5, 3, 1, 4].
          End scores = (20, 47)
          >>> print(turns[2])
          Start scores = (20, 47).
          Player 0 rolls 10 dice and gets outcomes [4, 5, 4, 6, 1, 1, 6, 2, 3, 1].
          End scores = (21, 47)
          >>> print(turns[3])
          Start scores = (21, 47).
          Player 1 rolls 7 dice and gets outcomes [1, 5, 4, 4, 5, 3, 2].
          End scores = (21, 48)
          >>> print(turns[4])
          Start scores = (21, 48).
          Player 0 rolls 4 dice and gets outcomes [2, 1, 1, 1].
          End scores = (22, 48)
          >>> print(turns[5])
          Start scores = (22, 48).
          Player 1 rolls 5 dice and gets outcomes [1, 1, 6, 6, 3].
          End scores = (22, 49)
          >>> print(turns[6])
          Start scores = (22, 49).
          Player 0 rolls 6 dice and gets outcomes [5, 3, 2, 2, 3, 4].
          End scores = (41, 49)
          >>> print(turns[7])
          Start scores = (41, 49).
          Player 1 rolls 6 dice and gets outcomes [5, 3, 1, 6, 1, 6].
          End scores = (41, 50)
          >>> print(turns[8])
          Start scores = (41, 50).
          Player 0 rolls 5 dice and gets outcomes [6, 3, 2, 1, 1].
          End scores = (42, 50)
          >>> print(turns[9])
          Start scores = (42, 50).
          Player 1 rolls 4 dice and gets outcomes [3, 6, 3, 1].
          End scores = (42, 51)
          >>> print(turns[10])
          Start scores = (42, 51).
          Player 0 rolls 10 dice and gets outcomes [6, 3, 2, 2, 5, 6, 2, 6, 3, 3].
          End scores = (80, 51)
          >>> print(turns[11])
          Start scores = (80, 51).
          Player 1 rolls 2 dice and gets outcomes [6, 4].
          End scores = (80, 61)
          >>> print(turns[12])
          Start scores = (80, 61).
          Player 0 rolls 1 dice and gets outcomes [4].
          End scores = (84, 61)
          >>> print(turns[13])
          Start scores = (84, 61).
          Player 1 rolls 4 dice and gets outcomes [4, 1, 4, 2].
          End scores = (84, 62)
          >>> print(turns[14])
          Start scores = (84, 62).
          Player 0 rolls 4 dice and gets outcomes [5, 5, 1, 3].
          End scores = (85, 62)
          >>> print(turns[15])
          Start scores = (85, 62).
          Player 1 rolls 0 dice and gets outcomes [].
          End scores = (85, 75)
          >>> print(turns[16])
          Start scores = (85, 75).
          Player 0 rolls 3 dice and gets outcomes [4, 1, 2].
          End scores = (89, 75)
          >>> print(turns[17])
          Start scores = (89, 75).
          Player 1 rolls 3 dice and gets outcomes [1, 5, 3].
          End scores = (89, 76)
          >>> print(turns[18])
          Start scores = (89, 76).
          Player 0 rolls 2 dice and gets outcomes [1, 2].
          End scores = (90, 76)
          >>> print(turns[19])
          Start scores = (90, 76).
          Player 1 rolls 8 dice and gets outcomes [3, 3, 1, 5, 4, 3, 2, 1].
          End scores = (90, 77)
          >>> print(turns[20])
          Start scores = (90, 77).
          Player 0 rolls 2 dice and gets outcomes [6, 3].
          End scores = (99, 77)
          >>> print(turns[21])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=74122, score0=18, score1=14, goal=32, feral_hogs=False)
          >>> print(turns[0])
          Start scores = (18, 14).
          Player 0 rolls 7 dice and gets outcomes [3, 2, 5, 2, 2, 6, 1].
          End scores = (19, 14)
          >>> print(turns[1])
          Start scores = (19, 14).
          Player 1 rolls 3 dice and gets outcomes [1, 3, 3].
          End scores = (19, 15)
          >>> print(turns[2])
          Start scores = (19, 15).
          Player 0 rolls 9 dice and gets outcomes [5, 3, 4, 3, 6, 3, 2, 5, 6].
          End scores = (15, 56)
          >>> print(turns[3])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=59593, score0=27, score1=9, goal=40, feral_hogs=False)
          >>> print(turns[0])
          Start scores = (27, 9).
          Player 0 rolls 1 dice and gets outcomes [5].
          End scores = (32, 9)
          >>> print(turns[1])
          Start scores = (32, 9).
          Player 1 rolls 4 dice and gets outcomes [4, 4, 2, 2].
          End scores = (32, 21)
          >>> print(turns[2])
          Start scores = (32, 21).
          Player 0 rolls 1 dice and gets outcomes [5].
          End scores = (37, 21)
          >>> print(turns[3])
          Start scores = (37, 21).
          Player 1 rolls 6 dice and gets outcomes [4, 6, 2, 2, 4, 4].
          End scores = (37, 43)
          >>> print(turns[4])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=8128, score0=17, score1=8, goal=29, feral_hogs=False)
          >>> print(turns[0])
          Start scores = (17, 8).
          Player 0 rolls 4 dice and gets outcomes [4, 2, 4, 5].
          End scores = (32, 8)
          >>> print(turns[1])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=22810, score0=7, score1=0, goal=43, feral_hogs=False)
          >>> print(turns[0])
          Start scores = (7, 0).
          Player 0 rolls 2 dice and gets outcomes [5, 3].
          End scores = (15, 0)
          >>> print(turns[1])
          Start scores = (15, 0).
          Player 1 rolls 2 dice and gets outcomes [2, 1].
          End scores = (15, 1)
          >>> print(turns[2])
          Start scores = (15, 1).
          Player 0 rolls 8 dice and gets outcomes [4, 1, 1, 3, 1, 4, 3, 5].
          End scores = (16, 1)
          >>> print(turns[3])
          Start scores = (16, 1).
          Player 1 rolls 1 dice and gets outcomes [3].
          End scores = (16, 4)
          >>> print(turns[4])
          Start scores = (16, 4).
          Player 0 rolls 10 dice and gets outcomes [5, 1, 6, 3, 1, 5, 4, 3, 1, 2].
          End scores = (17, 4)
          >>> print(turns[5])
          Start scores = (17, 4).
          Player 1 rolls 2 dice and gets outcomes [6, 5].
          End scores = (17, 15)
          >>> print(turns[6])
          Start scores = (17, 15).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (23, 15)
          >>> print(turns[7])
          Start scores = (23, 15).
          Player 1 rolls 10 dice and gets outcomes [5, 4, 6, 6, 6, 2, 1, 5, 2, 4].
          End scores = (23, 16)
          >>> print(turns[8])
          Start scores = (23, 16).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (28, 16)
          >>> print(turns[9])
          Start scores = (28, 16).
          Player 1 rolls 6 dice and gets outcomes [4, 5, 5, 6, 6, 3].
          End scores = (28, 45)
          >>> print(turns[10])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=59348, score0=95, score1=84, goal=97, feral_hogs=True)
          >>> print(turns[0])
          Start scores = (95, 84).
          Player 0 rolls 1 dice and gets outcomes [2].
          End scores = (97, 84)
          >>> print(turns[1])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=88169, score0=23, score1=40, goal=79, feral_hogs=False)
          >>> print(turns[0])
          Start scores = (23, 40).
          Player 0 rolls 3 dice and gets outcomes [1, 5, 6].
          End scores = (40, 24)
          >>> print(turns[1])
          Start scores = (40, 24).
          Player 1 rolls 1 dice and gets outcomes [2].
          End scores = (40, 26)
          >>> print(turns[2])
          Start scores = (40, 26).
          Player 0 rolls 4 dice and gets outcomes [6, 6, 6, 2].
          End scores = (60, 26)
          >>> print(turns[3])
          Start scores = (60, 26).
          Player 1 rolls 0 dice and gets outcomes [].
          End scores = (60, 42)
          >>> print(turns[4])
          Start scores = (60, 42).
          Player 0 rolls 9 dice and gets outcomes [3, 3, 6, 5, 4, 2, 3, 5, 1].
          End scores = (61, 42)
          >>> print(turns[5])
          Start scores = (61, 42).
          Player 1 rolls 1 dice and gets outcomes [6].
          End scores = (61, 48)
          >>> print(turns[6])
          Start scores = (61, 48).
          Player 0 rolls 3 dice and gets outcomes [3, 2, 5].
          End scores = (71, 48)
          >>> print(turns[7])
          Start scores = (71, 48).
          Player 1 rolls 2 dice and gets outcomes [6, 6].
          End scores = (71, 60)
          >>> print(turns[8])
          Start scores = (71, 60).
          Player 0 rolls 5 dice and gets outcomes [4, 5, 3, 3, 4].
          End scores = (90, 60)
          >>> print(turns[9])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=70467, score0=61, score1=74, goal=97, feral_hogs=False)
          >>> print(turns[0])
          Start scores = (61, 74).
          Player 0 rolls 2 dice and gets outcomes [4, 4].
          End scores = (69, 74)
          >>> print(turns[1])
          Start scores = (69, 74).
          Player 1 rolls 8 dice and gets outcomes [6, 4, 3, 1, 5, 1, 5, 6].
          End scores = (69, 75)
          >>> print(turns[2])
          Start scores = (69, 75).
          Player 0 rolls 6 dice and gets outcomes [5, 3, 4, 1, 5, 6].
          End scores = (70, 75)
          >>> print(turns[3])
          Start scores = (70, 75).
          Player 1 rolls 6 dice and gets outcomes [6, 4, 6, 1, 5, 3].
          End scores = (70, 76)
          >>> print(turns[4])
          Start scores = (70, 76).
          Player 0 rolls 7 dice and gets outcomes [2, 2, 1, 3, 3, 6, 1].
          End scores = (71, 76)
          >>> print(turns[5])
          Start scores = (71, 76).
          Player 1 rolls 7 dice and gets outcomes [6, 3, 6, 4, 5, 3, 1].
          End scores = (71, 77)
          >>> print(turns[6])
          Start scores = (71, 77).
          Player 0 rolls 4 dice and gets outcomes [2, 6, 4, 4].
          End scores = (87, 77)
          >>> print(turns[7])
          Start scores = (87, 77).
          Player 1 rolls 5 dice and gets outcomes [2, 6, 3, 3, 4].
          End scores = (87, 95)
          >>> print(turns[8])
          Start scores = (87, 95).
          Player 0 rolls 1 dice and gets outcomes [1].
          End scores = (88, 95)
          >>> print(turns[9])
          Start scores = (88, 95).
          Player 1 rolls 6 dice and gets outcomes [2, 4, 2, 2, 6, 4].
          End scores = (88, 115)
          >>> print(turns[10])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=8714, score0=38, score1=19, goal=57, feral_hogs=False)
          >>> print(turns[0])
          Start scores = (38, 19).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (40, 19)
          >>> print(turns[1])
          Start scores = (40, 19).
          Player 1 rolls 4 dice and gets outcomes [5, 1, 1, 1].
          End scores = (40, 20)
          >>> print(turns[2])
          Start scores = (40, 20).
          Player 0 rolls 2 dice and gets outcomes [4, 5].
          End scores = (49, 20)
          >>> print(turns[3])
          Start scores = (49, 20).
          Player 1 rolls 9 dice and gets outcomes [5, 4, 6, 5, 6, 3, 4, 3, 5].
          End scores = (49, 61)
          >>> print(turns[4])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=13230, score0=65, score1=56, goal=77, feral_hogs=True)
          >>> print(turns[0])
          Start scores = (65, 56).
          Player 0 rolls 6 dice and gets outcomes [2, 5, 2, 1, 3, 4].
          End scores = (66, 56)
          >>> print(turns[1])
          Start scores = (66, 56).
          Player 1 rolls 2 dice and gets outcomes [2, 5].
          End scores = (66, 66)
          >>> print(turns[2])
          Start scores = (66, 66).
          Player 0 rolls 9 dice and gets outcomes [4, 1, 1, 5, 3, 6, 1, 3, 5].
          End scores = (67, 66)
          >>> print(turns[3])
          Start scores = (67, 66).
          Player 1 rolls 7 dice and gets outcomes [2, 4, 6, 6, 3, 6, 1].
          End scores = (67, 67)
          >>> print(turns[4])
          Start scores = (67, 67).
          Player 0 rolls 9 dice and gets outcomes [6, 4, 1, 4, 3, 4, 1, 3, 2].
          End scores = (68, 67)
          >>> print(turns[5])
          Start scores = (68, 67).
          Player 1 rolls 3 dice and gets outcomes [2, 3, 6].
          End scores = (68, 81)
          >>> print(turns[6])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=96667, score0=2, score1=3, goal=13, feral_hogs=True)
          >>> print(turns[0])
          Start scores = (2, 3).
          Player 0 rolls 9 dice and gets outcomes [1, 1, 3, 5, 3, 6, 6, 4, 1].
          End scores = (3, 3)
          >>> print(turns[1])
          Start scores = (3, 3).
          Player 1 rolls 3 dice and gets outcomes [2, 3, 5].
          End scores = (13, 3)
          >>> print(turns[2])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=27904, score0=23, score1=39, goal=92, feral_hogs=False)
          >>> print(turns[0])
          Start scores = (23, 39).
          Player 0 rolls 9 dice and gets outcomes [6, 6, 2, 6, 1, 4, 3, 4, 3].
          End scores = (24, 39)
          >>> print(turns[1])
          Start scores = (24, 39).
          Player 1 rolls 1 dice and gets outcomes [4].
          End scores = (24, 43)
          >>> print(turns[2])
          Start scores = (24, 43).
          Player 0 rolls 2 dice and gets outcomes [3, 3].
          End scores = (30, 43)
          >>> print(turns[3])
          Start scores = (30, 43).
          Player 1 rolls 9 dice and gets outcomes [4, 5, 5, 6, 2, 4, 1, 3, 5].
          End scores = (30, 44)
          >>> print(turns[4])
          Start scores = (30, 44).
          Player 0 rolls 7 dice and gets outcomes [4, 5, 2, 2, 4, 1, 1].
          End scores = (31, 44)
          >>> print(turns[5])
          Start scores = (31, 44).
          Player 1 rolls 7 dice and gets outcomes [5, 5, 6, 1, 6, 1, 1].
          End scores = (31, 45)
          >>> print(turns[6])
          Start scores = (31, 45).
          Player 0 rolls 1 dice and gets outcomes [2].
          End scores = (33, 45)
          >>> print(turns[7])
          Start scores = (33, 45).
          Player 1 rolls 9 dice and gets outcomes [5, 2, 2, 5, 2, 6, 6, 2, 3].
          End scores = (33, 78)
          >>> print(turns[8])
          Start scores = (33, 78).
          Player 0 rolls 10 dice and gets outcomes [5, 3, 4, 5, 2, 1, 5, 5, 3, 6].
          End scores = (34, 78)
          >>> print(turns[9])
          Start scores = (34, 78).
          Player 1 rolls 9 dice and gets outcomes [6, 2, 2, 6, 1, 1, 6, 5, 2].
          End scores = (34, 79)
          >>> print(turns[10])
          Start scores = (34, 79).
          Player 0 rolls 7 dice and gets outcomes [3, 2, 2, 2, 4, 4, 6].
          End scores = (57, 79)
          >>> print(turns[11])
          Start scores = (57, 79).
          Player 1 rolls 1 dice and gets outcomes [1].
          End scores = (57, 80)
          >>> print(turns[12])
          Start scores = (57, 80).
          Player 0 rolls 9 dice and gets outcomes [5, 4, 6, 5, 5, 4, 6, 5, 2].
          End scores = (99, 80)
          >>> print(turns[13])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=36152, score0=49, score1=25, goal=52, feral_hogs=True)
          >>> print(turns[0])
          Start scores = (49, 25).
          Player 0 rolls 5 dice and gets outcomes [1, 5, 6, 1, 3].
          End scores = (50, 25)
          >>> print(turns[1])
          Start scores = (50, 25).
          Player 1 rolls 5 dice and gets outcomes [3, 1, 2, 2, 2].
          End scores = (50, 26)
          >>> print(turns[2])
          Start scores = (50, 26).
          Player 0 rolls 6 dice and gets outcomes [2, 3, 1, 5, 5, 3].
          End scores = (51, 26)
          >>> print(turns[3])
          Start scores = (51, 26).
          Player 1 rolls 8 dice and gets outcomes [2, 2, 3, 1, 5, 3, 2, 2].
          End scores = (51, 27)
          >>> print(turns[4])
          Start scores = (51, 27).
          Player 0 rolls 9 dice and gets outcomes [4, 3, 5, 6, 4, 2, 3, 2, 1].
          End scores = (52, 27)
          >>> print(turns[5])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=97165, score0=13, score1=4, goal=42, feral_hogs=False)
          >>> print(turns[0])
          Start scores = (13, 4).
          Player 0 rolls 4 dice and gets outcomes [1, 3, 1, 4].
          End scores = (4, 14)
          >>> print(turns[1])
          Start scores = (4, 14).
          Player 1 rolls 1 dice and gets outcomes [5].
          End scores = (4, 19)
          >>> print(turns[2])
          Start scores = (4, 19).
          Player 0 rolls 10 dice and gets outcomes [4, 5, 3, 3, 5, 4, 6, 1, 2, 4].
          End scores = (5, 19)
          >>> print(turns[3])
          Start scores = (5, 19).
          Player 1 rolls 4 dice and gets outcomes [1, 5, 5, 6].
          End scores = (5, 20)
          >>> print(turns[4])
          Start scores = (5, 20).
          Player 0 rolls 3 dice and gets outcomes [1, 1, 3].
          End scores = (6, 20)
          >>> print(turns[5])
          Start scores = (6, 20).
          Player 1 rolls 6 dice and gets outcomes [3, 3, 6, 3, 4, 4].
          End scores = (6, 43)
          >>> print(turns[6])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=7964, score0=0, score1=12, goal=30, feral_hogs=True)
          >>> print(turns[0])
          Start scores = (0, 12).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (9, 12)
          >>> print(turns[1])
          Start scores = (9, 12).
          Player 1 rolls 2 dice and gets outcomes [2, 5].
          End scores = (9, 22)
          >>> print(turns[2])
          Start scores = (9, 22).
          Player 0 rolls 10 dice and gets outcomes [5, 4, 6, 3, 3, 2, 4, 2, 2, 1].
          End scores = (22, 10)
          >>> print(turns[3])
          Start scores = (22, 10).
          Player 1 rolls 2 dice and gets outcomes [1, 2].
          End scores = (22, 11)
          >>> print(turns[4])
          Start scores = (22, 11).
          Player 0 rolls 5 dice and gets outcomes [4, 1, 2, 5, 5].
          End scores = (23, 11)
          >>> print(turns[5])
          Start scores = (23, 11).
          Player 1 rolls 5 dice and gets outcomes [5, 5, 3, 5, 3].
          End scores = (23, 32)
          >>> print(turns[6])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=87291, score0=59, score1=15, goal=87, feral_hogs=False)
          >>> print(turns[0])
          Start scores = (59, 15).
          Player 0 rolls 3 dice and gets outcomes [2, 2, 1].
          End scores = (60, 15)
          >>> print(turns[1])
          Start scores = (60, 15).
          Player 1 rolls 9 dice and gets outcomes [6, 2, 4, 4, 4, 3, 5, 2, 3].
          End scores = (60, 48)
          >>> print(turns[2])
          Start scores = (60, 48).
          Player 0 rolls 8 dice and gets outcomes [3, 5, 1, 6, 6, 2, 3, 4].
          End scores = (61, 48)
          >>> print(turns[3])
          Start scores = (61, 48).
          Player 1 rolls 5 dice and gets outcomes [6, 2, 5, 6, 3].
          End scores = (61, 70)
          >>> print(turns[4])
          Start scores = (61, 70).
          Player 0 rolls 4 dice and gets outcomes [2, 5, 4, 4].
          End scores = (76, 70)
          >>> print(turns[5])
          Start scores = (76, 70).
          Player 1 rolls 8 dice and gets outcomes [2, 6, 4, 1, 6, 1, 2, 4].
          End scores = (76, 71)
          >>> print(turns[6])
          Start scores = (76, 71).
          Player 0 rolls 4 dice and gets outcomes [4, 2, 2, 1].
          End scores = (77, 71)
          >>> print(turns[7])
          Start scores = (77, 71).
          Player 1 rolls 4 dice and gets outcomes [1, 3, 3, 6].
          End scores = (77, 72)
          >>> print(turns[8])
          Start scores = (77, 72).
          Player 0 rolls 4 dice and gets outcomes [6, 2, 6, 2].
          End scores = (93, 72)
          >>> print(turns[9])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=2481, score0=32, score1=79, goal=98, feral_hogs=False)
          >>> print(turns[0])
          Start scores = (32, 79).
          Player 0 rolls 10 dice and gets outcomes [2, 4, 4, 5, 2, 5, 3, 1, 2, 5].
          End scores = (33, 79)
          >>> print(turns[1])
          Start scores = (33, 79).
          Player 1 rolls 6 dice and gets outcomes [2, 2, 5, 5, 1, 6].
          End scores = (80, 33)
          >>> print(turns[2])
          Start scores = (80, 33).
          Player 0 rolls 9 dice and gets outcomes [3, 1, 2, 4, 6, 2, 2, 3, 6].
          End scores = (81, 33)
          >>> print(turns[3])
          Start scores = (81, 33).
          Player 1 rolls 3 dice and gets outcomes [1, 3, 6].
          End scores = (81, 34)
          >>> print(turns[4])
          Start scores = (81, 34).
          Player 0 rolls 10 dice and gets outcomes [4, 2, 3, 6, 1, 4, 2, 2, 3, 2].
          End scores = (82, 34)
          >>> print(turns[5])
          Start scores = (82, 34).
          Player 1 rolls 9 dice and gets outcomes [1, 1, 4, 6, 3, 1, 6, 5, 4].
          End scores = (82, 35)
          >>> print(turns[6])
          Start scores = (82, 35).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (90, 35)
          >>> print(turns[7])
          Start scores = (90, 35).
          Player 1 rolls 9 dice and gets outcomes [3, 6, 2, 5, 2, 1, 5, 3, 6].
          End scores = (90, 36)
          >>> print(turns[8])
          Start scores = (90, 36).
          Player 0 rolls 7 dice and gets outcomes [1, 2, 4, 2, 6, 2, 1].
          End scores = (91, 36)
          >>> print(turns[9])
          Start scores = (91, 36).
          Player 1 rolls 9 dice and gets outcomes [4, 1, 3, 1, 3, 4, 4, 5, 3].
          End scores = (91, 37)
          >>> print(turns[10])
          Start scores = (91, 37).
          Player 0 rolls 4 dice and gets outcomes [6, 5, 4, 2].
          End scores = (108, 37)
          >>> print(turns[11])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=57878, score0=4, score1=13, goal=29, feral_hogs=True)
          >>> print(turns[0])
          Start scores = (4, 13).
          Player 0 rolls 5 dice and gets outcomes [2, 3, 1, 6, 3].
          End scores = (5, 13)
          >>> print(turns[1])
          Start scores = (5, 13).
          Player 1 rolls 9 dice and gets outcomes [3, 4, 2, 3, 3, 4, 1, 4, 3].
          End scores = (5, 14)
          >>> print(turns[2])
          Start scores = (5, 14).
          Player 0 rolls 5 dice and gets outcomes [1, 5, 2, 3, 1].
          End scores = (6, 14)
          >>> print(turns[3])
          Start scores = (6, 14).
          Player 1 rolls 0 dice and gets outcomes [].
          End scores = (6, 18)
          >>> print(turns[4])
          Start scores = (6, 18).
          Player 0 rolls 2 dice and gets outcomes [5, 1].
          End scores = (18, 7)
          >>> print(turns[5])
          Start scores = (18, 7).
          Player 1 rolls 5 dice and gets outcomes [3, 6, 6, 1, 1].
          End scores = (18, 8)
          >>> print(turns[6])
          Start scores = (18, 8).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (20, 8)
          >>> print(turns[7])
          Start scores = (20, 8).
          Player 1 rolls 2 dice and gets outcomes [6, 4].
          End scores = (20, 18)
          >>> print(turns[8])
          Start scores = (20, 18).
          Player 0 rolls 8 dice and gets outcomes [5, 3, 4, 4, 2, 2, 3, 2].
          End scores = (45, 18)
          >>> print(turns[9])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=27303, score0=31, score1=3, goal=39, feral_hogs=False)
          >>> print(turns[0])
          Start scores = (31, 3).
          Player 0 rolls 9 dice and gets outcomes [6, 5, 6, 1, 6, 2, 2, 2, 6].
          End scores = (32, 3)
          >>> print(turns[1])
          Start scores = (32, 3).
          Player 1 rolls 9 dice and gets outcomes [1, 6, 1, 1, 5, 5, 2, 1, 6].
          End scores = (32, 4)
          >>> print(turns[2])
          Start scores = (32, 4).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (38, 4)
          >>> print(turns[3])
          Start scores = (38, 4).
          Player 1 rolls 6 dice and gets outcomes [3, 6, 6, 6, 6, 3].
          End scores = (38, 34)
          >>> print(turns[4])
          Start scores = (38, 34).
          Player 0 rolls 3 dice and gets outcomes [3, 5, 5].
          End scores = (34, 51)
          >>> print(turns[5])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=98514, score0=46, score1=42, goal=60, feral_hogs=True)
          >>> print(turns[0])
          Start scores = (46, 42).
          Player 0 rolls 5 dice and gets outcomes [5, 1, 3, 3, 5].
          End scores = (47, 42)
          >>> print(turns[1])
          Start scores = (47, 42).
          Player 1 rolls 0 dice and gets outcomes [].
          End scores = (47, 49)
          >>> print(turns[2])
          Start scores = (47, 49).
          Player 0 rolls 8 dice and gets outcomes [6, 3, 4, 4, 5, 1, 4, 6].
          End scores = (48, 49)
          >>> print(turns[3])
          Start scores = (48, 49).
          Player 1 rolls 3 dice and gets outcomes [4, 5, 6].
          End scores = (64, 48)
          >>> print(turns[4])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=64395, score0=3, score1=18, goal=52, feral_hogs=False)
          >>> print(turns[0])
          Start scores = (3, 18).
          Player 0 rolls 9 dice and gets outcomes [4, 4, 6, 3, 2, 6, 3, 3, 2].
          End scores = (36, 18)
          >>> print(turns[1])
          Start scores = (36, 18).
          Player 1 rolls 3 dice and gets outcomes [2, 1, 2].
          End scores = (19, 36)
          >>> print(turns[2])
          Start scores = (19, 36).
          Player 0 rolls 2 dice and gets outcomes [6, 5].
          End scores = (30, 36)
          >>> print(turns[3])
          Start scores = (30, 36).
          Player 1 rolls 9 dice and gets outcomes [6, 3, 3, 2, 6, 4, 1, 4, 5].
          End scores = (30, 37)
          >>> print(turns[4])
          Start scores = (30, 37).
          Player 0 rolls 8 dice and gets outcomes [2, 1, 3, 4, 4, 5, 3, 1].
          End scores = (31, 37)
          >>> print(turns[5])
          Start scores = (31, 37).
          Player 1 rolls 3 dice and gets outcomes [1, 4, 3].
          End scores = (31, 38)
          >>> print(turns[6])
          Start scores = (31, 38).
          Player 0 rolls 1 dice and gets outcomes [6].
          End scores = (37, 38)
          >>> print(turns[7])
          Start scores = (37, 38).
          Player 1 rolls 1 dice and gets outcomes [2].
          End scores = (37, 40)
          >>> print(turns[8])
          Start scores = (37, 40).
          Player 0 rolls 6 dice and gets outcomes [4, 3, 2, 2, 6, 1].
          End scores = (38, 40)
          >>> print(turns[9])
          Start scores = (38, 40).
          Player 1 rolls 0 dice and gets outcomes [].
          End scores = (45, 38)
          >>> print(turns[10])
          Start scores = (45, 38).
          Player 0 rolls 10 dice and gets outcomes [1, 2, 5, 5, 6, 6, 6, 2, 1, 5].
          End scores = (46, 38)
          >>> print(turns[11])
          Start scores = (46, 38).
          Player 1 rolls 9 dice and gets outcomes [6, 5, 4, 2, 2, 4, 4, 6, 4].
          End scores = (46, 75)
          >>> print(turns[12])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=13464, score0=27, score1=4, goal=47, feral_hogs=True)
          >>> print(turns[0])
          Start scores = (27, 4).
          Player 0 rolls 4 dice and gets outcomes [3, 1, 5, 4].
          End scores = (28, 4)
          >>> print(turns[1])
          Start scores = (28, 4).
          Player 1 rolls 7 dice and gets outcomes [5, 3, 2, 5, 4, 5, 3].
          End scores = (28, 31)
          >>> print(turns[2])
          Start scores = (28, 31).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (40, 31)
          >>> print(turns[3])
          Start scores = (40, 31).
          Player 1 rolls 2 dice and gets outcomes [6, 4].
          End scores = (40, 41)
          >>> print(turns[4])
          Start scores = (40, 41).
          Player 0 rolls 1 dice and gets outcomes [1].
          End scores = (41, 41)
          >>> print(turns[5])
          Start scores = (41, 41).
          Player 1 rolls 0 dice and gets outcomes [].
          End scores = (41, 54)
          >>> print(turns[6])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=92338, score0=64, score1=67, goal=69, feral_hogs=False)
          >>> print(turns[0])
          Start scores = (64, 67).
          Player 0 rolls 10 dice and gets outcomes [6, 2, 4, 4, 6, 4, 4, 6, 3, 4].
          End scores = (107, 67)
          >>> print(turns[1])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=55414, score0=9, score1=19, goal=32, feral_hogs=False)
          >>> print(turns[0])
          Start scores = (9, 19).
          Player 0 rolls 8 dice and gets outcomes [1, 3, 2, 6, 1, 2, 5, 3].
          End scores = (10, 19)
          >>> print(turns[1])
          Start scores = (10, 19).
          Player 1 rolls 10 dice and gets outcomes [4, 2, 4, 6, 1, 5, 1, 3, 2, 1].
          End scores = (10, 20)
          >>> print(turns[2])
          Start scores = (10, 20).
          Player 0 rolls 3 dice and gets outcomes [3, 4, 2].
          End scores = (19, 20)
          >>> print(turns[3])
          Start scores = (19, 20).
          Player 1 rolls 4 dice and gets outcomes [6, 6, 6, 2].
          End scores = (19, 40)
          >>> print(turns[4])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=2412, score0=90, score1=38, goal=94, feral_hogs=False)
          >>> print(turns[0])
          Start scores = (90, 38).
          Player 0 rolls 7 dice and gets outcomes [5, 3, 2, 6, 4, 1, 5].
          End scores = (91, 38)
          >>> print(turns[1])
          Start scores = (91, 38).
          Player 1 rolls 6 dice and gets outcomes [2, 3, 3, 5, 1, 6].
          End scores = (91, 39)
          >>> print(turns[2])
          Start scores = (91, 39).
          Player 0 rolls 3 dice and gets outcomes [1, 1, 5].
          End scores = (92, 39)
          >>> print(turns[3])
          Start scores = (92, 39).
          Player 1 rolls 8 dice and gets outcomes [1, 2, 6, 3, 1, 6, 5, 6].
          End scores = (92, 40)
          >>> print(turns[4])
          Start scores = (92, 40).
          Player 0 rolls 5 dice and gets outcomes [1, 3, 1, 5, 6].
          End scores = (93, 40)
          >>> print(turns[5])
          Start scores = (93, 40).
          Player 1 rolls 3 dice and gets outcomes [5, 4, 6].
          End scores = (93, 55)
          >>> print(turns[6])
          Start scores = (93, 55).
          Player 0 rolls 10 dice and gets outcomes [3, 1, 5, 6, 5, 3, 5, 2, 4, 3].
          End scores = (94, 55)
          >>> print(turns[7])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=43957, score0=35, score1=51, goal=100, feral_hogs=True)
          >>> print(turns[0])
          Start scores = (35, 51).
          Player 0 rolls 6 dice and gets outcomes [2, 3, 4, 6, 3, 2].
          End scores = (55, 51)
          >>> print(turns[1])
          Start scores = (55, 51).
          Player 1 rolls 4 dice and gets outcomes [5, 3, 1, 1].
          End scores = (55, 52)
          >>> print(turns[2])
          Start scores = (55, 52).
          Player 0 rolls 1 dice and gets outcomes [3].
          End scores = (58, 52)
          >>> print(turns[3])
          Start scores = (58, 52).
          Player 1 rolls 4 dice and gets outcomes [5, 1, 1, 4].
          End scores = (53, 58)
          >>> print(turns[4])
          Start scores = (53, 58).
          Player 0 rolls 8 dice and gets outcomes [2, 5, 3, 3, 4, 5, 5, 3].
          End scores = (58, 83)
          >>> print(turns[5])
          Start scores = (58, 83).
          Player 1 rolls 8 dice and gets outcomes [6, 6, 5, 2, 6, 5, 1, 3].
          End scores = (58, 84)
          >>> print(turns[6])
          Start scores = (58, 84).
          Player 0 rolls 10 dice and gets outcomes [1, 2, 6, 1, 1, 3, 2, 3, 1, 3].
          End scores = (59, 84)
          >>> print(turns[7])
          Start scores = (59, 84).
          Player 1 rolls 10 dice and gets outcomes [4, 4, 4, 4, 1, 5, 4, 5, 3, 2].
          End scores = (59, 85)
          >>> print(turns[8])
          Start scores = (59, 85).
          Player 0 rolls 1 dice and gets outcomes [1].
          End scores = (60, 85)
          >>> print(turns[9])
          Start scores = (60, 85).
          Player 1 rolls 8 dice and gets outcomes [3, 3, 3, 1, 3, 6, 6, 2].
          End scores = (86, 60)
          >>> print(turns[10])
          Start scores = (86, 60).
          Player 0 rolls 7 dice and gets outcomes [1, 3, 5, 1, 6, 4, 3].
          End scores = (87, 60)
          >>> print(turns[11])
          Start scores = (87, 60).
          Player 1 rolls 0 dice and gets outcomes [].
          End scores = (87, 71)
          >>> print(turns[12])
          Start scores = (87, 71).
          Player 0 rolls 3 dice and gets outcomes [6, 4, 5].
          End scores = (105, 71)
          >>> print(turns[13])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=36287, score0=42, score1=52, goal=100, feral_hogs=True)
          >>> print(turns[0])
          Start scores = (42, 52).
          Player 0 rolls 10 dice and gets outcomes [5, 4, 1, 5, 6, 4, 2, 3, 4, 4].
          End scores = (43, 52)
          >>> print(turns[1])
          Start scores = (43, 52).
          Player 1 rolls 10 dice and gets outcomes [3, 4, 6, 2, 4, 2, 4, 6, 4, 3].
          End scores = (43, 90)
          >>> print(turns[2])
          Start scores = (43, 90).
          Player 0 rolls 7 dice and gets outcomes [6, 4, 4, 6, 6, 4, 4].
          End scores = (77, 90)
          >>> print(turns[3])
          Start scores = (77, 90).
          Player 1 rolls 5 dice and gets outcomes [4, 4, 1, 6, 1].
          End scores = (77, 91)
          >>> print(turns[4])
          Start scores = (77, 91).
          Player 0 rolls 7 dice and gets outcomes [6, 2, 6, 5, 4, 1, 3].
          End scores = (78, 91)
          >>> print(turns[5])
          Start scores = (78, 91).
          Player 1 rolls 6 dice and gets outcomes [1, 3, 1, 1, 2, 2].
          End scores = (78, 92)
          >>> print(turns[6])
          Start scores = (78, 92).
          Player 0 rolls 3 dice and gets outcomes [2, 2, 2].
          End scores = (87, 92)
          >>> print(turns[7])
          Start scores = (87, 92).
          Player 1 rolls 10 dice and gets outcomes [1, 5, 4, 5, 2, 3, 4, 1, 5, 4].
          End scores = (87, 93)
          >>> print(turns[8])
          Start scores = (87, 93).
          Player 0 rolls 1 dice and gets outcomes [6].
          End scores = (93, 93)
          >>> print(turns[9])
          Start scores = (93, 93).
          Player 1 rolls 10 dice and gets outcomes [6, 5, 3, 5, 1, 3, 2, 5, 1, 2].
          End scores = (93, 94)
          >>> print(turns[10])
          Start scores = (93, 94).
          Player 0 rolls 3 dice and gets outcomes [3, 1, 4].
          End scores = (94, 94)
          >>> print(turns[11])
          Start scores = (94, 94).
          Player 1 rolls 6 dice and gets outcomes [4, 1, 4, 1, 3, 2].
          End scores = (94, 95)
          >>> print(turns[12])
          Start scores = (94, 95).
          Player 0 rolls 2 dice and gets outcomes [6, 2].
          End scores = (102, 95)
          >>> print(turns[13])
          Game Over
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, hog_gui, test_number=36008, score0=3, score1=9, goal=11, feral_hogs=True)
          >>> print(turns[0])
          Start scores = (3, 9).
          Player 0 rolls 10 dice and gets outcomes [3, 3, 4, 3, 2, 1, 6, 5, 6, 5].
          End scores = (4, 9)
          >>> print(turns[1])
          Start scores = (4, 9).
          Player 1 rolls 10 dice and gets outcomes [1, 3, 5, 1, 3, 1, 3, 5, 6, 6].
          End scores = (4, 10)
          >>> print(turns[2])
          Start scores = (4, 10).
          Player 0 rolls 2 dice and gets outcomes [1, 4].
          End scores = (5, 10)
          >>> print(turns[3])
          Start scores = (5, 10).
          Player 1 rolls 8 dice and gets outcomes [6, 2, 3, 1, 6, 4, 4, 5].
          End scores = (5, 11)
          >>> print(turns[4])
          Game Over
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> # Fuzz Testing
      >>> # Plays a lot of random games, and calculates a secret value.
      >>> # Failing this test means something is wrong, but you should
      >>> # look at other tests to see where the problem might be.
      >>> # Hint: make sure you're only calling take_turn once per turn!
      >>> #
      >>> import hog, importlib, hog_gui
      >>> # importlib.reload(hog)
      >>> import tests.play_utils
      """,
      'teardown': r"""
      
      """,
      'type': 'doctest'
    }
  ]
}
