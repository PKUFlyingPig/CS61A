test = {
  'name': 'split-at',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (car (split-at '(1 2 3 4 5) 3))
          (1 2 3)
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (cdr (split-at '(1 2 3 4 5) 3))
          (4 5)
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (car (split-at '(1 2 3 4 5) 10))
          (1 2 3 4 5)
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (cdr (split-at '(1 2 3 4 5) 10))
          ()
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (car (split-at '(0 1 1 2 3) 0))
          ()
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (cdr (split-at '(0 1 1 2 3) 0))
          (0 1 1 2 3)
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
