test = {
  'name': 'Recursion',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> def f(a, b):
          ...     if a > b:
          ...         return f(a - 3, 2 * b)
          ...     elif a < b:
          ...         return f(b // 2, a)
          ...     else:
          ...         return b
          >>> f(2, 2)
          2
          >>> f(7, 4)
          4
          >>> f(2, 28)
          8
          >>> f(-1, -3)
          Infinite
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
