test = {
  'name': 'filter-lst',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (filter-lst even? '(1 2 3 4))
          f6d93158137814c549d98372b81a6666
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (filter-lst odd? '(1 3 5))
          2b642a9b7568a2206bdc1a3d944f1dc2
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (filter-lst odd? '(2 4 6 1))
          2c988a84918e0b2958168830ef8b7391
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (filter-lst even? '(3))
          5d4e7085bcd945f8a26f87865c684069
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (filter-lst odd? nil)
          5d4e7085bcd945f8a26f87865c684069
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': True,
      'setup': r"""
      scm> (load-all ".")
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
