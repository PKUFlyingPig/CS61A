test = {
  'name': 'q1',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> hacker = cat([1,2], 2)
          
          >>> hacker(1)
          
          >>> hacker(2)
          'Successfully unlocked!'
          
          >>> hacker = cat([1,2], 1)
          
          >>> hacker(1)
          
          >>> hacker(3) # used up attempts to gain access
          
          >>> hacker(2) # correct attempt to gain access, but already locked
          'The safe is now inaccessible!'
          
          >>> hacker = cat([1,2], 2)
          
          >>> hacker(1)
          
          >>> hacker(3) # 1 attempt left to gain access
          
          >>> hacker(2) # correct attempt to gain access
          'Successfully unlocked!'
          """,
          'hidden': False
        }
      ],
      'scored': True,
      'setup': 'from q1 import *',
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> hacker = cat([1], 4)
          
          >>> hacker(3)
          
          >>> hacker(3)
          
          >>> hacker(3)
          
          >>> hacker(3)
          
          >>> hacker(3)
          'The safe is now inaccessible!'
          
          >>> hacker = cat([1], 4)
          
          >>> hacker(3)
          
          >>> hacker(3)
          
          >>> hacker(3)
          
          >>> hacker(3)
          
          >>> hacker(1)
          'The safe is now inaccessible!'
          
          >>> hacker = cat([1], 4)
          
          >>> hacker(1)
          'Successfully unlocked!'
          
          >>> hacker = cat([1, 2, 3, 4, 5, 6], 4)
          
          >>> hacker(1)
          
          >>> hacker(2)
          
          >>> hacker(3)
          
          >>> hacker(4)
          
          >>> hacker(5)
          
          >>> hacker(6)
          'Successfully unlocked!'
          
          >>> hacker = cat([1,2,3,4], 2)
          
          >>> hacker(1)
          
          >>> hacker(2)
          
          >>> hacker(3)
          
          >>> hacker(3)
          
          >>> hacker(4)
          'Successfully unlocked!'
          """,
          'hidden': False
        }
      ],
      'scored': True,
      'setup': 'from q1 import *',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
