test = {
  'name': 'cadr-caddr',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (cddr '(1 2 3 4))
          (3 4)
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (cadr '(1 2 3 4))
          2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (caddr '(1 2 3 4))
          3
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
