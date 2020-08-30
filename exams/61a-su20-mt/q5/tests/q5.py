test = {
  'name': 'q5',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> subsaltshaker(2233) # 22 counts
          True
          
          >>> subsaltshaker(2444423) # 4444 counts
          True
          
          >>> subsaltshaker(82223) # 22 counts even if it appears as part of 222
          True
          
          >>> subsaltshaker(234562) # 2...2 does not count if the 2s are not consecutive
          False
          
          >>> subsaltshaker(1) # 1 counts
          True
          
          >>> subsaltshaker(498729879871) # 1 counts
          True
          
          >>> subsaltshaker(149872987987) # 1 counts
          True
          
          >>> subsaltshaker(4445555) # no saltshakers in this number
          False
          
          >>> subsaltshaker(20) # no saltshakers in this number
          False
          """,
          'hidden': False
        }
      ],
      'scored': True,
      'setup': 'from q5 import *',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
