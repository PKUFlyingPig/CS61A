test = {
  'name': 'pow',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (pow 2 5)
          32
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (pow 10 3)
          1000
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (pow 3 3)
          27
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (pow 1 100000000000000) ; make sure you are using the logarithmic time algorithm!
          1
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      scm> (load-all ".")
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
