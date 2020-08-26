test = {
  'name': 'Lambda the Free',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'answer': 'A lambda expression does not automatically bind the function object that it returns to any name.',
          'choices': [
            'A lambda expression does not automatically bind the function object that it returns to any name.',
            'A lambda expression cannot have more than two parameters.',
            'A lambda expression cannot return another function.',
            'A def statement can only have one line in its body.'
          ],
          'hidden': False,
          'locked': False,
          'question': r"""
          Which of the following statements describes a difference between a def statement
          and a lambda expression?
          """
        },
        {
          'answer': 'two',
          'choices': [
            'one',
            'two',
            'three',
            'Not enough information'
          ],
          'hidden': False,
          'locked': False,
          'question': r"""
          How many parameters does the following lambda expression have?
          lambda a, b: c + d
          """
        },
        {
          'answer': 'When the function returned by the lambda expression is called.',
          'choices': [
            'When the function returned by the lambda expression is called.',
            'When you assign the lambda expression to a name.',
            'When the lambda expression is evaluated.',
            'When you pass the lambda expression into another function.'
          ],
          'hidden': False,
          'locked': False,
          'question': 'When is the return expression of a lambda expression executed?'
        }
      ],
      'scored': False,
      'type': 'concept'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> lambda x: x  # A lambda expression with one parameter x
          Function
          >>> a = lambda x: x  # Assigning a lambda function to the name a
          >>> a(5)
          5
          >>> (lambda: 3)()  # Using a lambda expression as an operator in a call exp.
          3
          >>> b = lambda x: lambda: x  # Lambdas can return other lambdas!
          >>> c = b(88)
          >>> c
          Function
          >>> c()
          88
          >>> d = lambda f: f(4)  # They can have functions as arguments as well
          >>> def square(x):
          ...     return x * x
          >>> d(square)
          16
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> x = None # remember to review the rules of WWPD given above!
          >>> x
          >>> lambda x: x
          Function
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> #
          >>> # Pay attention to the scope of variables
          >>> z = 3
          >>> e = lambda x: lambda y: lambda: x + y + z
          >>> e(0)(1)()
          4
          >>> f = lambda z: x + z
          >>> f(3)
          Error
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Try drawing an environment diagram if you get stuck!
          >>> higher_order_lambda = lambda f: lambda x: f(x)
          >>> g = lambda x: x * x
          >>> higher_order_lambda(2)(g) # Which argument belongs to which function call?
          Error
          >>> higher_order_lambda(g)(2)
          4
          >>> call_thrice = lambda f: lambda x: f(f(f(x)))
          >>> call_thrice(lambda y: y + 1)(0)
          3
          >>> print_lambda = lambda z: print(z)
          >>> print_lambda
          Function
          >>> one_thousand = print_lambda(1000)
          1000
          >>> one_thousand
          Nothing
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': False,
      'type': 'wwpp'
    }
  ]
}
