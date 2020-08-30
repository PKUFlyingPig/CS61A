test = {
  'name': 'q3',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> painting_a = microscope()
          
          >>> painting_b, x = painting_a(2)
          
          >>> x                                   # 2
          2
          
          >>> painting_c, x = painting_b(8)
          
          >>> x                                   # 2 - 8
          -6
          
          >>> painting_d, x = painting_c(12)
          
          >>> x                                   # 2 - 8 + 12
          6
          
          >>> painting_e, x = painting_d(30)
          
          >>> x                                   # 2 - 8 + 12 - 30
          -24
          
          >>> painting_b_again, x = painting_a(100)
          
          >>> x                                   # 100 [note that we are using painting_a not painting_d here]
          100
          
          >>> plush(microscope(), [1, 2, 3, 4, 5])
          3
          
          >>> plush(microscope(), [4000])
          4000
          
          >>> plush(microscope(), [2, 90])
          -88
          
          >>> plush(identity_painting, [2, 90])
          90
          """,
          'hidden': False
        }
      ],
      'scored': True,
      'setup': 'from q3 import *',
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': '',
          'hidden': False
        }
      ],
      'scored': True,
      'setup': 'from q3 import *',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
