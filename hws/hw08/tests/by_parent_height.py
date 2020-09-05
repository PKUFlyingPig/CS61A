test = {
  'name': 'parent',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          sqlite> SELECT * FROM by_parent_height;
          herbert
          fillmore
          abraham
          delano
          grover
          barack
          clinton
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'ordered': True,
      'scored': True,
      'setup': r"""
      sqlite> .read hw08.sql
      """,
      'teardown': '',
      'type': 'sqlite'
    }
  ]
}
