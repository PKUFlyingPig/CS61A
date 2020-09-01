test = {
  'name': 'derive-product',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (make-product 2 3)
          d89dec15f7ace001cf3392d60dd0343e
          # locked
          scm> (make-product 'x 0)
          2987fbac6d35b0de527489a12a63cba6
          # locked
          scm> (make-product 1 'x)
          af70c7541c654d94823e8ec85df4bd8b
          # locked
          scm> (make-product 'a 'x)
          942d355044217c0fda7147914763c11b
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
    },
    {
      'cases': [
        {
          'code': r"""
          scm> (derive '(* x y) 'x)
          y
          scm> (derive '(+ x (* x y)) 'x)
          (+ 1 y)
          scm> (derive '(* (* x y) (+ x 3)) 'x)
          (+ (* y (+ x 3)) (* x y))
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
