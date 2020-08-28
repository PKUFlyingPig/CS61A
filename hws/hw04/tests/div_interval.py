test = {
  'name': 'div_interval',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Type AssertionError if you think an AssertionError is raised
          >>> str_interval(div_interval(interval(-1, 2), interval(4, 8)))
          06f0172163ac5ae0a4c155bb75ecf6e3
          # locked
          >>> str_interval(div_interval(interval(4, 8), interval(-1, 2)))
          4060e99d27e3a37b32bf3c7106f16f59
          # locked
          """,
          'hidden': False,
          'locked': True
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
          >>> str_interval(div_interval(interval(-1, 2), interval(4, 8)))
          '-0.25 to 0.5'
          >>> str_interval(div_interval(interval(4, 8), interval(-1, 2)))
          AssertionError
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
