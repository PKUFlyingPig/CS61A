test = {
  'name': 'Problem 18',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (let-to-lambda 1)
          eb892a26497f936d1f6cae54aacc5f51
          # locked
          scm> (let-to-lambda 'a)
          1bafa4c4e8a0f079ce3e2b9f42f660e8
          # locked
          scm> (let-to-lambda '(+ 1 2))
          60bce2a18c88a72aea48f8aa277c4f35
          # locked
          scm> (let-to-lambda '(let ((a 1)
          ....                 (b 2))
          ....                (+ a b)))
          5954848e6ef93fe629e44367fa62ef91
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> '(quoted expressions remain the same)
          (quoted expressions remain the same)
          scm> (let-to-lambda '(quote (let ((a 1) (b 2)) (+ a b))))
          (quote (let ((a 1) (b 2)) (+ a b)))
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      scm> (load 'questions)
      """,
      'teardown': '',
      'type': 'scheme'
    },
    {
      'cases': [
        {
          'code': r"""
          scm> '(lambda parameters not affected but body affected)
          (lambda parameters not affected but body affected)
          scm> (let-to-lambda '(lambda (let a b) (+ let a b)))
          (lambda (let a b) (+ let a b))
          scm> (let-to-lambda '(lambda (x) a (let ((a x)) a)))
          (lambda (x) a ((lambda (a) a) x))
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (let-to-lambda '(let ((a (let ((a 2)) a))
          ....                 (b 2))
          ....                (+ a b)))
          ((lambda (a b) (+ a b)) ((lambda (a) a) 2) 2)
          scm> (let-to-lambda '(let ((a 1))
          ....                (let ((b a))
          ....                     b)))
          ((lambda (a) ((lambda (b) b) a)) 1)
          scm> (let-to-lambda '(+ 1 (let ((a 1)) a)))
          (+ 1 ((lambda (a) a) 1))
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      scm> (load 'questions)
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
