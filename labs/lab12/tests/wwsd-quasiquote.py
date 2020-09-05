test = {
  'name': 'quasiquote',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> '(1 x 3)
          (1 x 3)
          scm> (define x 2)
          x
          scm> `(1 x 3)
          (1 x 3)
          scm> `(1 ,x 3)
          (1 2 3)
          scm> '(1 ,x 3)
          (1 (unquote x) 3)
          scm> `(,1 x 3)
          (1 x 3)
          scm> `,(+ 1 x 3)
          6
          scm> `(1 (,x) 3)
          (1 (2) 3)
          scm> `(1 ,(+ x 2) 3)
          (1 4 3)
          scm> (define y 3)
          y
          scm> `(x ,(* y x) y)
          (x 6 y)
          scm> `(1 ,(cons x (list y 4)) 5)
          (1 (2 3 4) 5)
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
