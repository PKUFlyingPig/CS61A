test = {
  'name': 'Veritasiness',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> True and 13
          13
          >>> False or 0
          0
          >>> not 10
          False
          >>> not None
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> True and 1 / 0 and False  # If this errors, just type Error.
          Error
          >>> True or 1 / 0 or False  # If this errors, just type Error.
          True
          >>> True and 0  # If this errors, just type Error.
          0
          >>> False or 1  # If this errors, just type Error.
          1
          >>> 1 and 3 and 6 and 10 and 15  # If this errors, just type Error.
          15
          >>> -1 and 1 > 0 # If this errors, just type Error.
          True
          >>> 0 or False or 2 or 1 / 0  # If this errors, just type Error.
          2
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
          >>> not 0
          True
          >>> (1 + 1) and 1  # If this errors, just type Error. If this is blank, just type Nothing.
          1
          >>> 1/0 or True  # If this errors, just type Error. If this is blank, just type Nothing.
          Error
          >>> (True or False) and False  # If this errors, just type Error. If this is blank, just type Nothing.
          False
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
