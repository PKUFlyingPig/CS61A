test = {
  'name': 'derive-sum',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (make-sum 1 3)
          8b30509d9e68cd1a783d9d64827ae5c8
          # locked
          scm> (make-sum 'x 0)
          af70c7541c654d94823e8ec85df4bd8b
          # locked
          scm> (make-sum 0 'x)
          af70c7541c654d94823e8ec85df4bd8b
          # locked
          scm> (make-sum 'a 'x)
          95b13491f71edf29ea7ad071ac68e761
          # locked
          scm> (make-sum 'a (make-sum 'x 1))
          a8313c5befb504c8242674b600920158
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
    },
    {
      'cases': [
        {
          'code': r"""
          scm> (derive '(+ x 3) 'x)
          c246989ba42191bcf781a5b9bc9b80ea
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
