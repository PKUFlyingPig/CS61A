test = {
  'name': 'Problem 15',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (define y 1)
          1a9a3321b8b99a0f9291d89be986e74c
          # locked
          scm> (define f (mu (x) (+ x y)))
          715124391110b4a3beec8c9ba1ec3097
          # locked
          scm> (define g (lambda (x y) (f (+ x x))))
          4781badc0e77c1e0291e161d5c9bfa57
          # locked
          scm> (g 3 7)
          ac8f8bf5e63b01fde95f04f5c6ce2820
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'scheme'
    },
    {
      'cases': [
        {
          'code': r"""
          scm> (define h (mu () x))
          h
          scm> (define (high fn x) (fn))
          high
          scm> (high h 2)
          2
          scm> (define (f x) (mu () (lambda (y) (+ x y))))
          f
          scm> (define (g x) (((f (+ x 1))) (+ x 2)))
          g
          scm> (g 3)
          8
          scm> (mu ())
          SchemeError
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
