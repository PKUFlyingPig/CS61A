test = {
  'name': 'replicate',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (replicate 1 5)
          (1 1 1 1 1)
          scm> (replicate 'a 7)
          (a a a a a a a)
          scm> (replicate 5 0)
          ()
          scm> (replicate 4 1)
          (4)
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (define a (replicate 'a 1000))
          a
          scm> (length a)
          1000
          scm> (define b (replicate 3 2000))
          b
          scm> (length b)
          2000
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
