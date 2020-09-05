test = {
  'name': 'stack',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          sqlite> SELECT * FROM stacks;
          abraham, delano, clinton, barack|171
          grover, delano, clinton, barack|173
          herbert, delano, clinton, barack|176
          fillmore, delano, clinton, barack|177
          eisenhower, delano, clinton, barack|180
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
