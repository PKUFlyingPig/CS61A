test = {
  'name': 'small',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          sqlite> SELECT name FROM size_of_dogs WHERE size="toy" OR size="mini";
          abraham
          eisenhower
          fillmore
          grover
          herbert
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
