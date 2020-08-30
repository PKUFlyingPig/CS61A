test = {
  'name': 'q6',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> copycat(['a', 'b', 'c'], [1, 2, 3])
          ['a', 'b', 'b', 'c', 'c', 'c']
          
          >>> copycat(['a', 'b', 'c'], [3])
          ['a', 'a', 'a']
          
          >>> copycat(['a', 'b', 'c'], [0, 2, 0])
          ['b', 'b']
          
          >>> copycat([], [1,2,3])
          []
          
          >>> copycat(['a', 'b', 'c'], [1, -1, 3])
          ['c', 'c', 'c']
          """,
          'hidden': False
        }
      ],
      'scored': True,
      'setup': 'from q6 import *',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
