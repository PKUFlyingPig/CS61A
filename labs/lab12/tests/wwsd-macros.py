test = {
  'name': 'wwsd-macros',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> +
          #[+]
          scm> list
          #[list]
          scm> (define-macro (f x) (car x))
          f
          scm> (f (2 3 4)) ; type SchemeError for error, or Nothing for nothing
          2
          scm> (f (+ 2 3))
          #[+]
          scm> (define x 2000)
          x
          scm> (f (x y z))
          2000
          scm> (f (list 2 3 4))
          #[list]
          scm> (f (quote (2 3 4)))
          SchemeError
          scm> (define quote 7000)
          quote
          scm> (f (quote (2 3 4)))
          7000
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (define-macro (g x) (+ x 2))
          g
          scm> (g 2)
          4
          scm> (g (+ 2 3))
          SchemeError
          scm> (define-macro (h x) (list '+ x 2))
          h
          scm> (h (+ 2 3))
          7
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (define-macro (if-else-5 condition consequent) `(if ,condition ,consequent 5))
          if-else-5
          scm> (if-else-5 #t 2)
          2
          scm> (if-else-5 #f 3)
          5
          scm> (if-else-5 #t (/ 1 0))
          SchemeError
          scm> (if-else-5 #f (/ 1 0))
          5
          scm> (if-else-5 (= 1 0) 2)
          5
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': False,
      'setup': r"""
      
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
