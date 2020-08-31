test = {
  'name': 'Link',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> from lab09 import *
          >>> link = Link(1000)
          >>> link.first
          1000
          >>> link.rest is Link.empty
          True
          >>> link = Link(1000, 2000)
          Error
          >>> link = Link(1000, Link())
          Error
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> from lab09 import *
          >>> link = Link(1, Link(2, Link(3)))
          >>> link.first
          1
          >>> link.rest.first
          2
          >>> link.rest.rest.rest is Link.empty
          True
          >>> link.first = 9001
          >>> link.first
          9001
          >>> link.rest = link.rest.rest
          >>> link.rest.first
          3
          >>> link = Link(1)
          >>> link.rest = link
          >>> link.rest.rest.rest.rest.first
          1
          >>> link = Link(2, Link(3, Link(4)))
          >>> link2 = Link(1, link)
          >>> link2.first
          1
          >>> link2.rest.first
          2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> from lab09 import *
          >>> link = Link(5, Link(6, Link(7)))
          >>> link                  # Look at the __repr__ method of Link
          Link(5, Link(6, Link(7)))
          >>> print(link)          # Look at the __str__ method of Link
          <5 6 7>
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': False,
      'type': 'wwpp'
    }
  ]
}
