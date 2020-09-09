test = {
  'name': 'Problem 1',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> scheme_read(Buffer(tokenize_lines(['nil'])))
          nil
          >>> scheme_read(Buffer(tokenize_lines(['1'])))
          1
          >>> scheme_read(Buffer(tokenize_lines(['true'])))
          True
          >>> read_tail(Buffer(tokenize_lines(['2)'])))
          Pair(2, nil)
          >>> read_tail(Buffer(tokenize_lines(['(2)'])))
          SyntaxError
          >>> read_line('3')
          3
          >>> read_line('-123')
          -123
          >>> read_line('1.25')
          1.25
          >>> read_line('true')
          True
          >>> read_line('(a)')
          Pair('a', nil)
          >>> read_line(')')
          SyntaxError
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> tokens = tokenize_lines(["(+ 1 ", "(23 4)) ("])
          >>> src = Buffer(tokens)
          >>> src.current()
          '('
          >>> src.pop_first()
          '('
          >>> src.current()
          '+'
          >>> src.pop_first()
          '+'
          >>> src.pop_first()
          1
          >>> scheme_read(src)  # Returns and removes the next complete expression in src
          Pair(23, Pair(4, nil))
          >>> src.current()
          ')'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> scheme_read(Buffer(tokenize_lines(['(18 6)']))) # Type SyntaxError if you think this errors
          Pair(18, Pair(6, nil))
          >>> read_line('(18 6)')  # Shorter version of above!
          Pair(18, Pair(6, nil))
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> read_tail(Buffer(tokenize_lines([')'])))
          nil
          >>> read_tail(Buffer(tokenize_lines(['1 2 3)'])))
          Pair(1, Pair(2, Pair(3, nil)))
          >>> read_tail(Buffer(tokenize_lines(['2 (3 4))'])))
          Pair(2, Pair(Pair(3, Pair(4, nil)), nil))
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> read_tail(Buffer(tokenize_lines(['(1 2 3)']))) # Type SyntaxError if you think this errors
          SyntaxError
          >>> read_line('((1 2 3)')
          SyntaxError
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> src = Buffer(tokenize_lines(["(+ 1 2)"]))
          >>> scheme_read(src)
          Pair('+', Pair(1, Pair(2, nil)))
          >>> src.current() # Don't forget to remove the closing parenthesis!
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> read_line("(+ (- 2 3) 1)")
          Pair('+', Pair(Pair('-', Pair(2, Pair(3, nil))), Pair(1, nil)))
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> read_line("()")
          nil
          >>> read_line("((a))")
          Pair(Pair('a', nil), nil)
          >>> read_line("(+ 1 (- 2 3) 8)")
          Pair('+', Pair(1, Pair(Pair('-', Pair(2, Pair(3, nil))), Pair(8, nil))))
          # choice: Pair('+', Pair(1, Pair('-', Pair(2, 3), Pair(8, nil))))
          # choice: Pair('+', Pair(1, Pair(Pair('-', Pair(2, 3)), Pair(8, nil))))
          # choice: Pair('+', Pair(1, Pair('-', Pair(2, Pair(3, nil)), Pair(8, nil))))
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
    }
  ]
}
