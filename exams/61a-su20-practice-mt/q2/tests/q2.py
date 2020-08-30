test = {
  'name': 'q2',
  'points': 6,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> guesser = make_guess(10)
          
          >>> guess1 = guesser(6)
          
          >>> guess2 = guess1(7)
          
          >>> guess3 = guess2(8)
          
          >>> guess3(10)
          3
          
          >>> guess2(10)
          2
          
          >>> a = make_guess(5)(1)(2)(3)(4)(5)
          
          >>> a
          4
          """,
          'hidden': False
        }
      ],
      'scored': True,
      'setup': 'from q2 import *',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
