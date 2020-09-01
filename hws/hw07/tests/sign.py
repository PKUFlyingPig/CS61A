test = {
  'name': 'sign',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (cond ((= 1 1) 42))
          609e0c8d7071cf8835876005653318ce
          # locked
          scm> (cond ((= 1 1) 42) ((= 1 1) 24))
          609e0c8d7071cf8835876005653318ce
          # locked
          scm> (cond ((= 1 0) 42) ((= 0 1) 24) (else 999))
          256b8b5c10cc3aeadfb6c3c9871caa8c
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (sign -42)
          e1b9cfca7d7c90645adadc2693015138
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (sign 0)
          2987fbac6d35b0de527489a12a63cba6
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (sign 42)
          c246989ba42191bcf781a5b9bc9b80ea
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
