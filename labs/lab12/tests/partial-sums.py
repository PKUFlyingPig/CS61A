test = {
  'name': 'partial-sums',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (define twos (cons-stream 2 twos))
          twos
          scm> (define evens (partial-sums twos))
          evens
          scm> (car evens)
          2
          scm> (car (cdr-stream evens))
          4
          scm> (car (cdr-stream (cdr-stream evens)))
          6
          scm> (define quadratic (partial-sums evens))
          quadratic
          scm> (car quadratic)
          2
          scm> (car (cdr-stream quadratic))
          6
          scm> (car (cdr-stream (cdr-stream quadratic)))
          12
          scm> (define finite (cons-stream 1 (cons-stream 2 (cons-stream 3 nil))))
          finite
          scm> (define finite-sums (partial-sums finite))
          finite-sums
          scm> (car finite-sums)
          1
          scm> (car (cdr-stream finite-sums))
          3
          scm> (car (cdr-stream (cdr-stream finite-sums)))
          6
          scm> (cdr-stream (cdr-stream (cdr-stream finite-sums)))
          ()
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
