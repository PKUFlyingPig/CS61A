test = {
  'name': 'What Would Scheme Print?',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (cons 1 (cons 2 nil))
          (1 2)
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (car (cons 1 (cons 2 nil)))
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (cdr (cons 1 (cons 2 nil)))
          (2)
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (list 1 2 3)
          (1 2 3)
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> '(1 2 3)
          (1 2 3)
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (cons 1 '(list 2 3))  ; Recall quoting
          (1 list 2 3)
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (cons 1 `(list 2 3))  ; Quasiquotes also work as quotes!
          (1 list 2 3)
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> '(cons 4 (cons (cons 6 8) ()))
          (cons 4 (cons (cons 6 8) ()))
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (cons 1 (list (cons 3 nil) 4 5))
          (1 (3) 4 5)
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
