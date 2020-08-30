test = {
  'name': 'q4',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> isinstance("abc", str)
          True
          
          >>> isinstance("abc", list)
          False
          
          >>> x = [200, 300]
          
          >>> x.append(x)
          
          >>> y = [x, x]              # this is the `y` from the doctests
          
          >>> lemon_y = lemon(y)      # this is the `lemon_y` from the doctests
          
          >>> len(lemon_y)
          2
          
          >>> lemon_y[0] is lemon_y[1]
          True
          
          >>> len(lemon_y[0])
          3
          
          >>> lemon_y[0][0]
          200
          
          >>> lemon_y[0][1]
          300
          
          >>> lemon_y[0][2] is lemon_y[0]
          True
          
          >>> lemon_y is y
          False
          
          >>> lemon_y[0] is y[0]
          False
          """,
          'hidden': False
        }
      ],
      'scored': True,
      'setup': 'from q4 import *',
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> a = []
          
          >>> lemon_a = lemon(a)
          
          >>> lemon_a
          []
          
          >>> lemon_a is a
          False
          """,
          'hidden': False
        }
      ],
      'scored': True,
      'setup': 'from q4 import *',
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> b = []
          
          >>> b.append(b)
          
          >>> lemon_b = lemon(b)
          
          >>> len(lemon_b)
          1
          
          >>> lemon_b is lemon_b[0]
          True
          
          >>> lemon_b is b
          False
          """,
          'hidden': False
        }
      ],
      'scored': True,
      'setup': 'from q4 import *',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
