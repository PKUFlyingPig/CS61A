test = {
  'name': 'substitute',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (substitute '(c a b) 'b 'l)
          4c9459fc195a9be9473e6e88ccc7290a
          # locked
          scm> (substitute '(f e a r s) 'f 'b)
          2ee4fbd036cdbc671b4e6b41c2e0afb6
          # locked
          scm> (substitute '(g (o) o (o)) 'o 'r)
          cbcc936cd8bb7cbc04e33191a50c9349
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (substitute '((lead guitar) (bass guitar) (rhythm guitar) drums)
          ....               'guitar 'axe)
          ((lead axe) (bass axe) (rhythm axe) drums)
          scm> (substitute '(romeo romeo wherefore art thou romeo) 'romeo 'paris)
          (paris paris wherefore art thou paris)
          scm> (substitute '((to be) or not (to (be))) 'be 'eat)
          ((to eat) or not (to (eat)))
          scm> (substitute '(a b (c) d e) 'foo 'bar)
          (a b (c) d e)
          """,
          'hidden': False,
          'locked': False
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
