test = {
  'name': 'matchmaker',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          sqlite> SELECT * FROM matchmaker LIMIT 10;
          turtle|Dancing Queen|blue|blue
          turtle|Dancing Queen|blue|purple
          dog|Clair De Lune|blue|red
          dog|Clair De Lune|blue|green
          dog|Clair De Lune|blue|blue
          dog|Formation|blue|blue
          dog|Formation|blue|blue
          fox|Truth Hurts|blue|black
          turtle|Dancing Queen|blue|purple
          dog|Dancing Queen|blue|blue
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
