test = {
  'name': 'Python Basics',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> 10 + 2
          12
          >>> 7 / 2
          3.5
          >>> 7 // 2
          3
          >>> 7 % 2			# 7 modulo 2, equivalent to the remainder of 7 // 2
          1
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
          >>> x = 20
          >>> x + 2
          22
          >>> x
          20
          >>> y = 5
          >>> y += 3			# Equivalent to y = y + 3
          >>> y * 2
          16
          >>> y //= 4			# Equivalent to y = y // 4
          >>> y + x
          22
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
