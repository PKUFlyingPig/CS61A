test = {
  'name': 'check_par',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> r1, r2 = check_par()
          >>> x = par1(r1, r2)
          >>> y = par2(r1, r2)
          >>> lower_bound(x) != lower_bound(y) or upper_bound(x) != upper_bound(y)
          True
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
          >>> r1, r2 = check_par()
          >>> x = par1(r1, r2)
          >>> y = par2(r1, r2)
          >>> lower_bound(x) != lower_bound(y) or upper_bound(x) != upper_bound(y)
          True
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
