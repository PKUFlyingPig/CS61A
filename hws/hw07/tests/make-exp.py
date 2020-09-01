test = {
  'name': 'make-exp',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (make-exp 2 4)
          9029a38cf7547348db1b791f8759ff61
          # locked
          scm> (make-exp 'x 1)
          af70c7541c654d94823e8ec85df4bd8b
          # locked
          scm> (make-exp 'x 0)
          c246989ba42191bcf781a5b9bc9b80ea
          # locked
          scm> x^2
          35d27ca42e0dea1373023371dc518fcd
          # locked
          scm> (first-operand x^2)
          af70c7541c654d94823e8ec85df4bd8b
          # locked
          scm> (second-operand x^2)
          9e912e512c4a5bd85d3693205c7f635c
          # locked
          scm> (exp? x^2) ; #t or #f
          dd1c8dcce7b8598825d7b6b7d237639d
          # locked
          scm> (exp? 1)
          9e1a295fed6e9113292585fe7acb7556
          # locked
          scm> (exp? 'x)
          9e1a295fed6e9113292585fe7acb7556
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': True,
      'setup': r"""
      scm> (load-all ".")
      scm> (define x^2 (make-exp 'x 2))
      scm> (define x^3 (make-exp 'x 3))
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
