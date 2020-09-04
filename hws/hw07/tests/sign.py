test = {
  'name': 'sign',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (cond ((= 1 1) 42))
          42
          scm> (cond ((= 1 1) 42) ((= 1 1) 24))
          42
          scm> (cond ((= 1 0) 42) ((= 0 1) 24) (else 999))
          999
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (sign -42)
          -1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (sign 0)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (sign 42)
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
