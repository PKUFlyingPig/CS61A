test = {
  'name': 'Question 0',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> test_dice = make_test_dice(4, 1, 2)
          >>> test_dice()
          edcbd82ba98a8122be244fa325c62071
          # locked
          >>> test_dice() # Second call
          43d176e102c8d95338faf8791aa509b3
          # locked
          >>> test_dice() # Third call
          46caef5ffd6d72c8757279cbcf01b12f
          # locked
          >>> test_dice() # Fourth call
          edcbd82ba98a8122be244fa325c62071
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from hog import *
      """,
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'answer': '5c489e1123a9d0cfdd0c26a27a56d42b',
          'choices': [
            'make_test_dice(6)',
            'make_fair_dice(6)',
            'six_sided',
            'six_sided()'
          ],
          'hidden': False,
          'locked': True,
          'question': 'Which of the following is the correct way to "roll" a fair, six-sided die?'
        }
      ],
      'scored': False,
      'type': 'concept'
    }
  ]
}
