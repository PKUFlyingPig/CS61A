test = {
  'name': 'lets-count',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          sqlite> SELECT * from favpets;
          dog|20
          cat|9
          turtle|4
          penguin|4
          dragon|4
          wolf|3
          tiger|3
          panda|3
          fox|3
          elephant|3
          sqlite> SELECT * from dog;
          dog|20
          sqlite> SELECT * from bluedog_agg;
          Dancing Queen|4
          Formation|3
          Never Be Like You|2
          Clair De Lune|2
          sqlite> SELECT * from instructor_obedience;
          7|Image 1|6
          7|Image 2|10
          7|Image 3|12
          7|Image 4|12
          7|Image 5|10
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
