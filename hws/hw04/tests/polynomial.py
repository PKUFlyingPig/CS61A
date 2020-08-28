test = {
  'name': 'polynomial',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> str_interval(polynomial(interval(0, 2), [-1, 3, -2]))
          '-3 to 0.125'
          >>> str_interval(polynomial(interval(1, 3), [1, -3, 2]))
          '0 to 10'
          >>> str_interval(polynomial(interval(0.5, 2.25), [10, 24, -6, -8, 3]))
          '18.0 to 23.0'
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> import hw04
      >>> from hw04 import *
      """,
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> # Testing for abstraction violations
          >>> # Your code should not check for which implementation is used
          >>> str_interval(polynomial(interval(0, 2), [-1, 3, -2]))
          '-3 to 0.125'
          >>> str_interval(polynomial(interval(1, 3), [1, -3, 2]))
          '0 to 10'
          >>> str_interval(polynomial(interval(0.5, 2.25), [10, 24, -6, -8, 3]))
          '18.0 to 23.0'
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> import hw04
      >>> old_abstraction = hw04.interval, hw04.lower_bound, hw04.upper_bound
      >>> hw04.interval = lambda a, b: lambda x: a if x == 0 else b
      >>> hw04.lower_bound = lambda s: s(0)
      >>> hw04.upper_bound = lambda s: s(1)
      >>> from hw04 import *
      """,
      'teardown': r"""
      >>> hw04.interval, hw04.lower_bound, hw04.upper_bound = old_abstraction
      """,
      'type': 'doctest'
    }
  ]
}
