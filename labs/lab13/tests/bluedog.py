test = {
  'name': 'bluedog',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          sqlite> SELECT * FROM bluedog;
          blue|dog
          blue|dog
          blue|dog
          blue|dog
          blue|dog
          blue|dog
          blue|dog
          blue|dog
          blue|dog
          blue|dog
          blue|dog
          sqlite> SELECT * FROM bluedog_songs;
          blue|dog|Clair De Lune
          blue|dog|Formation
          blue|dog|Dancing Queen
          blue|dog|Dancing Queen
          blue|dog|Dancing Queen
          blue|dog|Dancing Queen
          blue|dog|Clair De Lune
          blue|dog|Formation
          blue|dog|Never Be Like You
          blue|dog|Formation
          blue|dog|Never Be Like You
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'ordered': False,
      'scored': True,
      'setup': r"""
      sqlite> .read lab13.sql
      """,
      'teardown': '',
      'type': 'sqlite'
    }
  ]
}
