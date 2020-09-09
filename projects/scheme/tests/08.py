test = {
  'name': 'Problem 8',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (lambda (x y) (+ x y))
          (lambda (x y) (+ x y))
          scm> (lambda (x))
          SchemeError
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (lambda (x) (+ x) (+ x x))
          (lambda (x) (+ x) (+ x x))
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (lambda () 2)
          (lambda () 2)
          """,
          'hidden': False,
          'locked': False
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
          >>> env = create_global_frame()
          >>> lambda_line = read_line("(lambda (a b c) (+ a (* b c)))")
          >>> lambda_proc = do_lambda_form(lambda_line.rest, env)
          >>> lambda_proc.formals
          Pair('a', Pair('b', Pair('c', nil)))
          >>> lambda_proc.body # Remember that the body is a *list* of expressions!
          Pair(Pair('+', Pair('a', Pair(Pair('*', Pair('b', Pair('c', nil))), nil))), nil)
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> env = create_global_frame()
          >>> lambda_line = read_line("(lambda (x y) x)")
          >>> lambda_proc = do_lambda_form(lambda_line.rest, env)
          >>> isinstance(lambda_proc, LambdaProcedure)
          True
          >>> lambda_proc.env is env
          True
          >>> lambda_proc
          LambdaProcedure(Pair('x', Pair('y', nil)), Pair('x', nil), <Global Frame>)
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from scheme_reader import *
      >>> from scheme import *
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
