test = {
  'name': 'What If?',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> def ab(c, d):
          ...     if c > 5:
          ...         print(c)
          ...     elif c > 7:
          ...         print(d)
          ...     print('foo')
          >>> ab(10, 20)
          10
          foo
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> def bake(cake, make):
          ...    if cake == 0:
          ...        cake = cake + 1
          ...        print(cake)
          ...    if cake == 1:
          ...        print(make)
          ...    else:
          ...        return cake
          ...    return make
          >>> bake(0, 29)
          1
          29
          29
          >>> bake(1, "mashed potatoes")
          mashed potatoes
          'mashed potatoes'
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
