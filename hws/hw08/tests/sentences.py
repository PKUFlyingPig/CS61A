test = {
  'name': 'size',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          sqlite> SELECT * FROM sentences;
          barack and clinton are standard siblings
          abraham and grover are toy siblings
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'ordered': False,
      'scored': True,
      'setup': r"""
      sqlite> .read hw08.sql
      """,
      'teardown': '',
      'type': 'sqlite'
    }
  ]
}
