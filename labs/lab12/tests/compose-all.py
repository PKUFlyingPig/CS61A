test = {
  'name': 'compose-all',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (define identity (compose-all (list)))
          identity
          scm> (identity 42)
          42
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (define (halve x) (/ x 2))
          halve
          scm> (define (square x) (* x x))
          square
          scm> (define halve-then-square (compose-all (list halve square)))
          halve-then-square
          scm> (define square-then-halve (compose-all (list square halve)))
          square-then-halve
          scm> (halve-then-square 42)
          441
          scm> (square-then-halve 42)
          882
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (define (halve x) (/ x 2))
          halve
          scm> (define (square x) (* x x))
          square
          scm> (define halve-then-square-then-halve (compose-all (list halve square halve)))
          halve-then-square-then-halve
          scm> (halve-then-square-then-halve 12)
          18
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
