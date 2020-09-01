test = {
  'name': 'composed',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> ((composed add-one add-one) 2)
          77dc3c4c1e581a2dae92fcb6752dc48c
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> ((composed multiply-by-two multiply-by-two) 2)
          c06687c738f80a705f30e5d905972e2a
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> ((composed add-one multiply-by-two) 2)
          fc2b3643bc0ad882bd631ec7e0059563
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> ((composed multiply-by-two add-one) 2)
          ad06a9a5930cdb4717260a68b2cca9b7
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> ((composed (composed add-one add-one) add-one) 2)
          fc2b3643bc0ad882bd631ec7e0059563
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> ((composed (composed add-one add-one) multiply-by-two) 2)
          ad06a9a5930cdb4717260a68b2cca9b7
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> ((composed multiply-by-two (composed add-one add-one)) 2)
          c06687c738f80a705f30e5d905972e2a
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': False,
      'setup': r"""
      scm> (load-all ".")
      scm> (define (add-one a) (+ a 1))
      scm> (define (multiply-by-two a) (* a 2))
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
