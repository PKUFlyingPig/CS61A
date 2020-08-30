test = {
  'name': 'q1',
  'points': 16,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> same_digits(2002200, 2202000) # Ignoring repeats, both are 2020
          True
          
          >>> same_digits(21, 12) # Digits must appear in the same order
          False
          
          >>> same_digits(12, 2212) # 12 and 212 are not the same
          False
          
          >>> same_digits(2020, 20) # 2020 and 20 are not the same
          False
          """,
          'hidden': False
        }
      ],
      'scored': True,
      'setup': 'from q1 import *',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
