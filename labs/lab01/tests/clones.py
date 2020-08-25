test = {
  'name': 'Higher Order Functions, Part 2',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> def cloning(x):
          ...     def machine(y):
          ...          y += 3
          ...          return x(y)
          ...     return machine
          >>> def increment(x):
          ...     return x + 1
          >>> dolly = cloning(increment)
          >>> a = 3
          >>> dolly(a)
          f3f0d7ed9a5f7790e7d6be65f44e207a
          # locked
          >>> a
          95e06bb41a8511e42188cb3fde2ddb68
          # locked
          >>> x23 = cloning(increment)
          >>> x23(2) == dolly(2)
          5154670fa295caf18cafa4245c1358a9
          # locked
          >>> x23 == dolly
          5dfeeb9ca37d955606d40c6553cd4956
          # locked
          >>> x23(dolly)
          d7b5fd49f83e4ee318af207fc969c9f4
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': False,
      'type': 'wwpp'
    }
  ]
}
