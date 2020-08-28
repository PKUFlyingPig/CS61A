test = {
  'name': 'Problem EC2',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> key_distance_diff.call_count = 0
          >>> key_distance_diff("wird", "word", 4)
          0.6834861261734088
          >>> key_distance_diff.call_count <= 106 #see if you removed redundant recursive calls
          True
          >>> key_distance_diff.call_count = 0 #reset the counter
          >>> key_distance_diff("aird", "word", 4)
          1.650081475501692
          >>> key_distance_diff.call_count <= 60
          True
          >>> key_distance_diff.call_count = 0
          >>> key_distance_diff("bord", "word", 4)
          2
          >>> key_distance_diff.call_count <= 34
          True
          >>> key_distance_diff.call_count = 0
          >>> key_distance_diff("speling","spelling", 8)
          1
          >>> key_distance_diff.call_count <= 712
          True
          >>> key_distance_diff.call_count = 0
          >>> key_distance_diff("speliing","spelling", 10)
          0.9665953493282832
          >>> key_distance_diff.call_count <= 568
          True
          >>> key_distance_diff.call_count = 0
          >>> key_distance_diff("spelosng","spelling", 10)
          2.683486126173409
          >>> key_distance_diff.call_count <= 622
          True
          >>> key_distance_diff.call_count = 0
          >>> key_distance_diff("spelosn","spelling", 10)
          3.683486126173409
          >>> key_distance_diff.call_count <= 775
          True
          >>> key_distance_diff.call_count = 0
          >>> key_distance_diff("wird", "word", 4)
          0.6834861261734088
          >>> key_distance_diff.call_count
          1
          >>> key_distance_diff.call_count = 0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Check that you're only using the key_distance_diff func
          >>> import trace, io
          >>> from contextlib import redirect_stdout
          >>> with io.StringIO() as buf, redirect_stdout(buf):
          ...     trace.Trace(trace=True).runfunc(key_distance_diff, "abc", "def", 3)
          ...     output = buf.getvalue()
          >>> lines = [line for line in output.split('\n') if 'funcname' in line]
          >>> func_names = set([l.split(",")[1].split(":")[1].strip() for l in lines])
          >>> func_names == {'counted', 'key_distance_diff', 'memoized'}
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> autocorrect("woll", common_words, key_distance_diff, 4)
          'will'
          >>> key_distance_diff.call_count <= 98924
          True
          >>> key_distance_diff.call_count = 0
          >>> faster_autocorrect("woll", common_words, meowstake_matches, 4)
          'well'
          >>> key_distance_diff.call_count
          0
          >>> key_distance_diff.call_count = 0
          >>> faster_autocorrect("woll", common_words, key_distance_diff, 4)
          'will'
          >>> key_distance_diff.call_count <= 2000 #key_distance_diffs should be memoized, this is the first call to faster_autocorrect
          True
          >>> key_distance_diff.call_count = 0
          >>> faster_autocorrect("woll", common_words, key_distance_diff, 4)
          'will'
          >>> key_distance_diff.call_count #faster_autocorrect should be memoized and this is the second call
          0
          >>> autocorrect("woll", common_words, key_distance_diff, 4)
          'will'
          >>> key_distance_diff.call_count <= 2000 #key_distance_diffs should still be memoized but autocorrect should not be
          True
          >>> key_distance_diff.call_count = 0
          >>> faster_autocorrect("woll", common_words, key_distance_diff, 3)
          'will'
          >>> key_distance_diff.call_count <= 41546 #different limit so it should have to recompute many calls
          True
          >>> key_distance_diff.call_count = 0
          >>> faster_autocorrect("woll", all_words, key_distance_diff, 2)
          'will'
          >>> key_distance_diff.call_count <= 6173942
          True
          >>> key_distance_diff.call_count = 0
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> try:
      ...    from cats import key_distance_diff, meowstake_matches, autocorrect, lines_from_file, faster_autocorrect, shifty_shifts
      ...    all_words = lines_from_file("data/words.txt")
      ...    common_words = lines_from_file("data/common_words.txt")
      ... except ImportError:
      ...    raise ImportError("You probably didn't define faster_autocorrect in typing_test.py yet!")
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
