test = {
  'name': 'q5',
  'points': 6,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> sequence(6, abs) # Terms are 1, 2, 3, 4, 5, 6
          123456
          
          >>> sequence(5, lambda k: k+8) # Terms are 9, 10, 11, 12, 13
          910111213
          
          >>> sequence(4, lambda k: pow(10, k)) # Terms are 10, 100, 1000, 10000
          10100100010000
          """,
          'hidden': False
        }
      ],
      'scored': True,
      'setup': 'from q5 import *',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
