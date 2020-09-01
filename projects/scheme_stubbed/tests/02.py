test = {
  'name': 'Problem 2',
  'points': 7,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> +
          #[+]
          scm> display
          #[display]
          scm> hello
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
    },
    {
      'cases': [
        {
          'code': r"""
          >>> env = create_global_frame()
          >>> twos = Pair(2, Pair(2, nil))
          >>> plus = BuiltinProcedure(scheme_add) # + procedure
          >>> scheme_apply(plus, twos, env) # Type SchemeError if you think this errors
          4
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> env = create_global_frame()
          >>> twos = Pair(2, Pair(2, nil))
          >>> oddp = BuiltinProcedure(scheme_oddp) # odd? procedure
          >>> scheme_apply(oddp, twos, env)
          SchemeError
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> env = create_global_frame()
          >>> two = Pair(2, nil)
          >>> eval = BuiltinProcedure(scheme_eval, True) # eval procedure
          >>> scheme_apply(eval, two, env) # be sure to check use_env
          2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> env = create_global_frame()
          >>> args = nil
          >>> def make_scheme_counter():
          ...     x = 0
          ...     def scheme_counter():
          ...         nonlocal x
          ...         x += 1
          ...         return x
          ...     return scheme_counter
          >>> counter = BuiltinProcedure(make_scheme_counter()) # counter
          >>> scheme_apply(counter, args, env) # only call procedure.fn once!
          1
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from scheme import *
      """,
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> expr = read_line('(+ 2 2)')
          >>> scheme_eval(expr, create_global_frame())
          4
          >>> expr = read_line('(+ (+ 2 2) (+ 1 3) (* 1 4))')
          >>> scheme_eval(expr, create_global_frame())
          12
          >>> expr = read_line('(yolo)')
          >>> scheme_eval(expr, create_global_frame())
          SchemeError
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
    },
    {
      'cases': [
        {
          'code': r"""
          scm> (+ 2 3)
          5
          scm> (* (+ 3 2) (+ 1 7))
          40
          scm> (1 2)
          SchemeError
          scm> (1 (print 0)) ; validate_procedure should be called before operands are evaluated
          SchemeError
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (+)
          0
          scm> (odd? 13)
          #t
          scm> (car (list 1 2 3 4))
          1
          scm> (car car)
          SchemeError
          scm> (odd? 1 2 3)
          SchemeError
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (+ (+ 1) (* 2 3) (+ 5) (+ 6 (+ 7)))
          25
          scm> (*)
          1
          scm> (-)
          SchemeError
          scm> (car (cdr (cdr (list 1 2 3 4))))
          3
          scm> (car cdr (list 1))
          SchemeError
          scm> (* (car (cdr (cdr (list 1 2 3 4)))) (car (cdr (list 1 2 3 4))))
          6
          scm> (* (car (cdr (cdr (list 1 2 3 4)))) (cdr (cdr (list 1 2 3 4))))
          SchemeError
          scm> (+ (/ 1 0))
          SchemeError
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> ((/ 1 0) (print 5)) ; operator should be evaluated before operands
          SchemeError
          scm> (null? (print 5)) ; operands should only be evaluated once
          5
          #f
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
          scm> (define size 2)
          size
          scm> size
          2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (define x (+ 2 3))
          x
          scm> x
          5
          scm> (define x (+ 2 7))
          x
          scm> x
          9
          scm> (eval (define tau 6.28))
          6.28
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (define pi 3.14159)
          pi
          scm> (define radius 10)
          radius
          scm> (define area (* pi (* radius radius)))
          area
          scm> area
          314.159
          scm> (define radius 100)
          radius
          scm> radius
          100
          scm> area
          314.159
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (define 0 1)
          SchemeError
          scm> (define error (/ 1 0))
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
    },
    {
      'cases': [
        {
          'code': r"""
          >>> read_line("(a (b 'c))")
          Pair('a', Pair(Pair('b', Pair(Pair('quote', Pair('c', nil)), nil)), nil))
          >>> read_line("(a (b '(c d)))")
          Pair('a', Pair(Pair('b', Pair(Pair('quote', Pair(Pair('c', Pair('d', nil)), nil)), nil)), nil))
          >>> read_line("')")
          SyntaxError
          >>> read_line("'()")
          Pair('quote', Pair(nil, nil))
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> read_line("'('a)")
          Pair('quote', Pair(Pair(Pair('quote', Pair('a', nil)), nil), nil))
          >>> read_line("''a")
          Pair('quote', Pair(Pair('quote', Pair('a', nil)), nil))
          >>> read_line("'('('a 'b 'c))")
          Pair('quote', Pair(Pair(Pair('quote', Pair(Pair(Pair('quote', Pair('a', nil)), Pair(Pair('quote', Pair('b', nil)), Pair(Pair('quote', Pair('c', nil)), nil))), nil)), nil), nil))
          >>> read_line("(+ '(1 2) 3)")
          Pair('+', Pair(Pair('quote', Pair(Pair(1, Pair(2, nil)), nil)), Pair(3, nil)))
          >>> read_line("'('+ '(1 2) '3)")
          Pair('quote', Pair(Pair(Pair('quote', Pair('+', nil)), Pair(Pair('quote', Pair(Pair(1, Pair(2, nil)), nil)), Pair(Pair('quote', Pair(3, nil)), nil))), nil))
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> scheme_read(Buffer(tokenize_lines(["'hello"])))
          Pair('quote', Pair('hello', nil))
          >>> read_line("(car '(1 2))")
          Pair('car', Pair(Pair('quote', Pair(Pair(1, Pair(2, nil)), nil)), nil))
          >>> print(read_line("(car '(1 2))"))
          (car (quote (1 2)))
          >>> read_line("'('a)")
          Pair('quote', Pair(Pair(Pair('quote', Pair('a', nil)), nil), nil))
          >>> read_line("''a")
          Pair('quote', Pair(Pair('quote', Pair('a', nil)), nil))
          >>> read_line("'('('a 'b 'c))")
          Pair('quote', Pair(Pair(Pair('quote', Pair(Pair(Pair('quote', Pair('a', nil)), Pair(Pair('quote', Pair('b', nil)), Pair(Pair('quote', Pair('c', nil)), nil))), nil)), nil), nil))
          >>> read_line("(+ '(1 2) 3)")
          Pair('+', Pair(Pair('quote', Pair(Pair(1, Pair(2, nil)), nil)), Pair(3, nil)))
          >>> read_line("'('+ '(1 2) '3)")
          Pair('quote', Pair(Pair(Pair('quote', Pair('+', nil)), Pair(Pair('quote', Pair(Pair(1, Pair(2, nil)), nil)), Pair(Pair('quote', Pair(3, nil)), nil))), nil))
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from scheme_reader import *
      """,
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          scm> (quote hello)
          hello
          scm> 'hello
          hello
          scm> (quote (1 2))
          (1 2)
          scm> '(1 2)
          (1 2)
          scm> (car '(1 2 3))
          1
          scm> (cdr '(1 2))
          (2)
          scm> (car (car '((1))))
          1
          scm> (quote 3)
          3
          scm> (eval (cons 'car '('(4 2))))
          4
          scm> `(1 2 3)
          (1 2 3)
          scm> (define a 2)
          a
          scm> `,a
          2
          scm> `(a b c)
          (a b c)
          scm> `(,a b c)
          (2 b c)
          scm> `(,a ,b c)
          SchemeError
          scm> `(,(+ ,a ,a) b)
          SchemeError
          scm> ``(1 2 (+ 3 4))
          (quasiquote (1 2 (+ 3 4)))
          scm> `(1 ,(cons a `(b ,(+ 1 2))))
          (1 (2 b 3))
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
