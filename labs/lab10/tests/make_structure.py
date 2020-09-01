test = {
  'name': 'make-list',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (define a '(1))
          e4518cbebdc0d1652a389becf2daf11b
          # locked
          scm> a
          2c988a84918e0b2958168830ef8b7391
          # locked
          scm> (define b (cons 2 a))
          ae951ee92cfd87cba4ca6bc270ede16d
          # locked
          scm> b
          92c6a338c156172c35312d2060dd02ba
          # locked
          scm> (define c (list 3 b))
          0b5443bb16d391663e72325e29dba21c
          # locked
          scm> c
          4473b526bf89266454bf0d18a3167b0b
          # locked
          scm> (car c)
          154ae95398009673bcf6847be0496a27
          # locked
          scm> (cdr c)
          4c117c29d319c285b6a835d9bb6093f7
          # locked
          scm> (car (car (cdr c)))
          8f01429f05539100445ff1214be81240
          # locked
          scm> (cdr (car (cdr c)))
          2c988a84918e0b2958168830ef8b7391
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> lst  ; type out exactly how Scheme would print the list
          d27fa7ae58e6e5c9334663d5f70ed8d8
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
