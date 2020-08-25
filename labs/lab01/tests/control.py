test = {
  'name': 'Control',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> def xk(c, d):
          ...     if c == 4:
          ...         return 6
          ...     elif d >= 4:
          ...         return 6 + 7 + c
          ...     else:
          ...         return 25
          >>> xk(10, 10)
          23
          >>> xk(10, 6)
          23
          >>> xk(4, 6)
          6
          >>> xk(0, 0)
          25
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> def how_big(x):
          ...     if x > 10:
          ...         print('huge')
          ...     elif x > 5:
          ...         return 'big'
          ...     elif x > 0:
          ...         print('small')
          ...     else:
          ...         print("nothin'")
          >>> how_big(7)
          'big'
          >>> how_big(12)
          huge
          >>> how_big(1)
          small
          >>> how_big(-1)
          nothin'
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': False,
      'type': 'wwpp'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> n = 3
          >>> while n >= 0:  # If this loops forever, just type Infinite Loop
          ...     n -= 1
          ...     print(n)
          2
          1
          0
          -1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> positive = 28
          >>> while positive: # If this loops forever, just type Infinite Loop
          ...    print("positive?")
          ...    positive -= 3
          Infinite Loop
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> positive = -9
          >>> negative = -12
          >>> while negative: # If this loops forever, just type Infinite Loop
          ...    if positive:
          ...        print(negative)
          ...    positive += 3
          ...    negative += 3
          -12
          -9
          -6
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
