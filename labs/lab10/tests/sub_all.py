test = {
  'name': 'sub_all',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (sub-all '(go ((bears))) '(go bears) '(big game))
          a3d5571f329133205125536142e7ed9b
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (sub-all '((4 calling birds) (3 french hens) (2 turtle doves))
          ....     '(1 2 3 4)
          ....     '(one two three four))
          ((four calling birds) (three french hens) (two turtle doves))
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
