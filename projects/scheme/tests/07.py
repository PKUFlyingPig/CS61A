test = {
  'name': 'Problem 7',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> eval_all(Pair(2, nil), env)
          2
          >>> eval_all(Pair(4, Pair(5, nil)), env)
          5
          >>> eval_all(nil, env) # return None (meaning undefined)
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> lst = Pair(1, Pair(2, Pair(3, nil)))
          >>> eval_all(lst, env)
          3
          >>> lst     # The list should not be mutated!
          Pair(1, Pair(2, Pair(3, nil)))
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from scheme import *
      >>> env = create_global_frame()
      """,
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          scm> (begin (+ 2 3) (+ 5 6))
          11
          scm> (begin (define x 3) x)
          3
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (begin 30 '(+ 2 2))
          (+ 2 2)
          scm> (define x 0)
          x
          scm> (begin (define x (+ x 1)) 42 (define y (+ x 1)))
          y
          scm> x
          1
          scm> y
          2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (begin 30 'hello)
          hello
          scm> (begin (define x 3) (cons x '(y z)))
          (3 y z)
          scm> (begin (define x 3) (cons x '(x z)))
          (3 x z)
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (define x 0)
          x
          scm> (begin (define x (+ x 1))
          ....        (define x (+ x 10))
          ....        (define x (+ x 100))
          ....        (define x (+ x 1000)))
          x
          scm> x
          1111
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
