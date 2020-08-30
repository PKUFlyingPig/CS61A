test = {
  'name': 'q6',
  'points': 10,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> increment = lambda x: x + 1
          
          >>> square = lambda x: x * x
          
          >>> do_nothing = make_zipper(increment, square, 0)
          
          >>> do_nothing(2) # Don't call either f1 or f2, just return your input untouched
          2
          
          >>> incincsq = make_zipper(increment, square, 112)
          
          >>> incincsq(2) # increment(increment(square(2))), so 2 -> 4 -> 5 -> 6
          6
          
          >>> sqincsqinc = make_zipper(increment, square, 2121)
          
          >>> sqincsqinc(2) # square(increment(square(increment(2)))), so 2 -> 3 -> 9 -> 10 -> 100
          100
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
