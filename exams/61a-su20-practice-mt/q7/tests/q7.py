test = {
  'name': 'q7',
  'points': 8,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> t = Tree (1 , [ Tree (2) , Tree (1 , [ Tree (2 , [ Tree (3 , [ Tree (0)])])])])
          
          >>> longest_seq( t) # 1 -> 2 -> 3
          3
          
          >>> t = Tree (1)
          
          >>> longest_seq( t)
          1
          """,
          'hidden': False
        }
      ],
      'scored': True,
      'setup': 'from q7 import *',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
