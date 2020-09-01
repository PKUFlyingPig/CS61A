test = {
  'name': 'remove',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (remove 3 nil)
          5d4e7085bcd945f8a26f87865c684069
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (remove 2 '(1 3 2))
          ede3b682727808ad2d2bf8535fdcebd3
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (remove 1 '(1 3 2))
          bfc251e881731057d823aeabdc42668c
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (remove 42 '(1 3 2))
          f39704cebbce57936f399d93cb42b9a0
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (remove 3 '(1 3 3 7))
          a555c23623f094eacbb9ed66ec9778b4
          # locked
          """,
          'hidden': False,
          'locked': True
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
