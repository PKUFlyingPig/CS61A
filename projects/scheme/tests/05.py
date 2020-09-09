test = {
  'name': 'Problem 5',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'answer': 'Pair(A, Pair(B, nil)), where: A is the symbol being bound, B is an expression whose value should be evaluated and bound to A',
          'choices': [
            r"""
            Pair(A, Pair(B, nil)), where:
                A is the symbol being bound,
                B is an expression whose value should be evaluated and bound to A
            """,
            r"""
            Pair(A, Pair(B, nil)), where:
                A is the symbol being bound,
                B is the value that should be bound to A
            """,
            r"""
            Pair(A, B), where:
                A is the symbol being bound,
                B is the value that should be bound to A
            """,
            r"""
            Pair(A, B), where:
                A is the symbol being bound,
                B is an expression whose value should be evaluated and bound to A
            """,
            r"""
            Pair('define', Pair(A, Pair(B, nil))), where:
                A is the symbol being bound,
                B is an expression whose value should be evaluated and bound to A
            """
          ],
          'hidden': False,
          'locked': False,
          'question': 'What is the structure of the expressions argument to do_define_form?'
        },
        {
          'answer': 'define',
          'choices': [
            'make_child_frame',
            'define',
            'lookup',
            'bindings'
          ],
          'hidden': False,
          'locked': False,
          'question': r"""
          What method of a Frame instance will bind
          a value to a symbol in that frame?
          """
        }
      ],
      'scored': False,
      'type': 'concept'
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
          scm> (eval (define tau 6.28)) ; eval takes an expression represented as a list and evaluates it
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
        },
        {
          'code': r"""
          scm> (define x 0)
          x
          scm> ((define x (+ x 1)) 2)
          SchemeError
          scm> x
          1
          scm> (define x 2 y 4)
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
