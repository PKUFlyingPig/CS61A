test = {
  'name': 'q4',
  'points': 6,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> sums(2, 2)
          [[1, 1]]
          
          >>> sums(2, 3)
          []
          
          >>> sums(4, 2)
          [[3, 1], [2, 2], [1, 3]]
          
          >>> sums(5, 3)
          [[3, 1, 1], [2, 2, 1], [1, 3, 1], [2, 1, 2], [1, 2, 2], [1, 1, 3]]
          """,
          'hidden': False
        }
      ],
      'scored': True,
      'setup': 'from q4 import *',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
