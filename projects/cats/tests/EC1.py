test = {
  'name': 'Problem EC1',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> key_distance_diff("wird", "word", 4)
          0.6834861261734088
          >>> key_distance_diff("aird", "word", 4)
          1.650081475501692
          >>> key_distance_diff("bord", "word", 4)
          2
          >>> key_distance_diff("word", "word", 0)
          0
          >>> key_distance_diff("word", "bord", 0)
          inf
          >>> key_distance_diff("w", "word", 4)
          3
          >>> key_distance_diff("speling","spelling", 8)
          1
          >>> key_distance_diff("speliing","spelling", 10)
          0.9665953493282832
          >>> key_distance_diff("spelosng","spelling", 10)
          2.683486126173409
          >>> key_distance_diff("spelosn","spelling", 10)
          3.683486126173409
          >>> key_distance_diff("word", "swoed", 3)
          1.6834861261734089
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect("woll", common_words, key_distance_diff, 4)
          'will'
          >>> autocorrect("woll", common_words, meowstake_matches, 4)
          'well'
          >>> autocorrect("nird", all_words, key_distance_diff, 2)
          'bird'
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> try:
      ...    from cats import key_distance_diff, meowstake_matches, autocorrect, lines_from_file
      ...    all_words = lines_from_file("data/words.txt")
      ...    common_words = lines_from_file("data/common_words.txt")
      ... except ImportError:
      ...    raise ImportError("You probably didn't define key_distance_diff in typing_test.py yet!")
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
