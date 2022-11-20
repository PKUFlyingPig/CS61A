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
          >>> 7 % 2  # 7 modulo 2, the remainder when dividing 7 by 2.
          1
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
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
          >>> y = y + 3
          >>> y * 2
          16
          >>> y = y // 4
          >>> y + x # think carefully about what x is equal to!
          22
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': False,
      'type': 'wwpp'
    }
  ]
}
