test = {
  'name': 'q2',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> int("5")
          5
          
          >>> str(5)
          '5'
          
          >>> 'evocative'[3]
          'c'
          
          >>> 'evocative'[3:]
          'cative'
          
          >>> 'evocative'[:6]
          'evocat'
          
          >>> 'evocative'[3:6]
          'cat'
          
          >>> schedule('?????', 25, 5)
          ['55555']
          
          >>> schedule('???', 5, 2)
          ['122', '212', '221']
          
          >>> schedule('?2??11?', 5, 3)
          ['0200111', '0201110', '0210110', '1200110']
          """,
          'hidden': False
        }
      ],
      'scored': True,
      'setup': 'from q2 import *',
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> schedule('???????', 56, 3)
          []
          
          >>> schedule('0000???', 4, 2)
          ['0000022', '0000112', '0000121', '0000202', '0000211', '0000220']
          
          >>> schedule('0?000??', 4, 2)
          ['0000022', '0100012', '0100021', '0200002', '0200011', '0200020']
          """,
          'hidden': False
        }
      ],
      'scored': True,
      'setup': 'from q2 import *',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
