test = {
  'name': 'debugging-quiz',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'answer': 'h(x + y * 5)',
          'choices': [
            'f("hi")',
            'g(x + x, x)',
            'h(x + y * 5)'
          ],
          'hidden': False,
          'locked': False,
          'question': r"""
          In the following traceback, what is the most recent function call?
          Traceback (most recent call last):
              File "temp.py", line 10, in <module>
                f("hi")
              File "temp.py", line 2, in f
                return g(x + x, x)
              File "temp.py", line 5, in g
                return h(x + y * 5)
              File "temp.py", line 8, in h
                return x + 0
            TypeError: must be str, not int
          """
        },
        {
          'answer': 'the code attempted to add a string to an integer',
          'choices': [
            'the code attempted to add a string to an integer',
            'the code looped infinitely',
            'there was a missing return statement'
          ],
          'hidden': False,
          'locked': False,
          'question': r"""
          In the following traceback, what is the cause of this error?
          Traceback (most recent call last):
              File "temp.py", line 10, in <module>
                f("hi")
              File "temp.py", line 2, in f
                return g(x + x, x)
              File "temp.py", line 5, in g
                return h(x + y * 5)
              File "temp.py", line 8, in h
                return x + 0
            TypeError: must be str, not int
          """
        },
        {
          'answer': "def square(x): ''' >>> square(2) 4 ''' return x * x",
          'choices': [
            r"""
            def square(x):
                '''
                doctest: (2, 4)
                '''
                return x * x
            """,
            r"""
            def square(x):
                '''
                input: 2
                output: 4
                '''
                return x * x
            """,
            r"""
            def square(x):
                '''
                square(2)
                4
                '''
                return x * x
            """,
            r"""
            def square(x):
                '''
                >>> square(2)
                4
                '''
                return x * x
            """
          ],
          'hidden': False,
          'locked': False,
          'question': 'How do you write a doctest asserting that square(2) == 4?'
        },
        {
          'answer': 'To investigate the values of variables at certain points in your code',
          'choices': [
            'For permanant debugging so you can have long term confidence in your code',
            'To ensure that certain conditions are true at certain points in your code',
            'To investigate the values of variables at certain points in your code'
          ],
          'hidden': False,
          'locked': False,
          'question': 'When should you use print statements?'
        },
        {
          'answer': "Print with 'DEBUG:' at the front of the outputted line",
          'choices': [
            "You don't need to do anything, ok only looks at returned values, not printed values",
            "Print with 'DEBUG:' at the front of the outputted line",
            'Print with # at the front of the outputted line'
          ],
          'hidden': False,
          'locked': False,
          'question': 'How do you prevent the ok autograder from interpreting print statements as output?'
        },
        {
          'answer': 'python3 ok -q sum_digits -i',
          'choices': [
            'python3 ok -q sum_digits -i',
            'python3 ok -q sum_digits --trace',
            'python3 ok -q sum_digits',
            'python3 -i lab01.py'
          ],
          'hidden': False,
          'locked': False,
          'question': 'What is the best way to open an interactive terminal to investigate a failing test for question sum_digits in assignment lab01?'
        },
        {
          'answer': 'python3 ok -q sum_digits --trace',
          'choices': [
            'python3 ok -q sum_digits -i',
            'python3 ok -q sum_digits --trace',
            'python3 ok -q sum_digits',
            'python3 -i lab01.py'
          ],
          'hidden': False,
          'locked': False,
          'question': 'What is the best way to look at an environment diagram to investigate a failing test for question sum_digits in assignment lab01?'
        },
        {
          'answer': 'Code that returns a wrong answer instead of crashing is generally better as it at least works fine',
          'choices': [
            'Code that returns a wrong answer instead of crashing is generally better as it at least works fine',
            'Testing is very important to ensure robust code',
            'Debugging is not a substitute for testing',
            'It is generally bad practice to release code with debugging print statements left in',
            'It is generally good practice to release code with assertion statements left in'
          ],
          'hidden': False,
          'locked': False,
          'question': 'Which of the following is NOT true?'
        },
        {
          'answer': 'You had an unmatched parenthesis',
          'choices': [
            'You had an unmatched parenthesis',
            'Your indentation mixed tabs and spaces',
            'You forgot a return statement',
            'You typed a variable name incorrectly'
          ],
          'hidden': False,
          'locked': False,
          'question': 'You get a SyntaxError. What is most likely to have happened?'
        },
        {
          'answer': 'Your indentation mixed tabs and spaces',
          'choices': [
            'You had an unmatched parenthesis',
            'Your indentation mixed tabs and spaces',
            'You forgot a return statement',
            'You typed a variable name incorrectly'
          ],
          'hidden': False,
          'locked': False,
          'question': 'You get a IndentationError. What is most likely to have happened?'
        },
        {
          'answer': 'You forgot a return statement',
          'choices': [
            'You had an unmatched parenthesis',
            'Your indentation mixed tabs and spaces',
            'You forgot a return statement',
            'You typed a variable name incorrectly'
          ],
          'hidden': False,
          'locked': False,
          'question': 'You get a TypeError: blah blah blah NoneType blah blah blah. What is most likely to have happened?'
        },
        {
          'answer': 'You typed a variable name incorrectly',
          'choices': [
            'You had an unmatched parenthesis',
            'Your indentation mixed tabs and spaces',
            'You forgot a return statement',
            'You typed a variable name incorrectly'
          ],
          'hidden': False,
          'locked': False,
          'question': 'You get a NameError. What is most likely to have happened?'
        }
      ],
      'scored': False,
      'type': 'concept'
    }
  ]
}
