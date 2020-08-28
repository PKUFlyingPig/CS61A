test = {
  'name': 'Trees',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> from lab06 import *
          >>> t = tree(1, tree(2))
          66901ed5775b51743d745870a1a883e3
          # locked
          >>> t = tree(1, [tree(2)])
          a4011416c969fbf2a5267fe8187bdbe9
          # locked
          >>> label(t)
          35926b8dc788659825b34f78c7f76f91
          # locked
          >>> label(branches(t)[0])
          31f02e75f8bef5a0621b68131795447b
          # locked
          >>> x = branches(t)
          >>> len(x)
          35926b8dc788659825b34f78c7f76f91
          # locked
          >>> is_leaf(x[0])
          4975a2633e94dd9ea1ce929c1df08a3b
          # locked
          >>> branch = x[0]
          >>> label(t) + label(branch)
          74689fcda5421388b764b40ec8de8ccd
          # locked
          >>> len(branches(branch))
          58e1f1fb97222d3a4c3904f2aa3cf3fa
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> from lab06 import *
          >>> b1 = tree(5, [tree(6), tree(7)])
          >>> b2 = tree(8, [tree(9, [tree(10)])])
          >>> t = tree(11, [b1, b2])
          >>> for b in branches(t):
          ...     print(label(b))
          36823867c25d95f8a792b4dde2bf0d63
          1399d9a7e3e505d23edf2a8008d52474
          # locked
          >>> for b in branches(t):
          ...     print(is_leaf(branches(b)[0]))
          4975a2633e94dd9ea1ce929c1df08a3b
          ac667055c8e3c84ad7260b0fefa2e007
          # locked
          >>> [label(b) + 100 for b in branches(t)]
          17718a31b6468a0b38c1a776bd8976cf
          # locked
          >>> [label(b) * label(branches(b)[0]) for b in branches(t)]
          9bf1abde91a898e6f38430fcf1db2978
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': False,
      'type': 'wwpp'
    }
  ]
}
