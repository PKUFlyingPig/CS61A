test = {
  'name': 'composed',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> ((composed add-one add-one) 2)
          4
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> ((composed multiply-by-two multiply-by-two) 2)
          8
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> ((composed add-one multiply-by-two) 2)
          5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> ((composed multiply-by-two add-one) 2)
          6
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> ((composed (composed add-one add-one) add-one) 2)
          5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> ((composed (composed add-one add-one) multiply-by-two) 2)
          6
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> ((composed multiply-by-two (composed add-one add-one)) 2)
          8
          """,
          'hidden': False,
          'locked': False
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
