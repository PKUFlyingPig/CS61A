test = {
  'name': 'unique',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (unique '())
          ()
          scm> (unique '(1 2 1 3 1 4))
          (1 2 3 4)
          scm> (unique '(1 2 3 4))
          (1 2 3 4)
          scm> (unique '(1 1 1 1 1))
          (1)
          scm> (unique '(c a b c))
          (c a b)
          scm> (unique '(1 2 3 4 1 2 3 4 1 2 3 4))
          (1 2 3 4)
          scm> (unique '(a b c a a b b c e c d ))
          (a b c e d)
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
