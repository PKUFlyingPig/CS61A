
def close(n, smallest=10, d=10):
    """ A sequence is near increasing if each element but the last two is smaller than all elements
    following its subsequent element. That is, element i must be smaller than elements i + 2, i + 3, i + 4, etc.
    Implement close, which takes a non-negative integer n and returns the largest near increasing sequence
    of digits within n as an integer. The arguments smallest and d are part of the implementation; you must
    determine their purpose. The only values you may use are integers and booleans (True and False) (no lists, strings, etc.).
    Return the longest sequence of near-increasing digits in n.
    >>> close(123)
    123
    >>> close(153)
    153
    >>> close(1523)
    153
    >>> close(15123)
    1123
    >>> close(11111111)
    11
    >>> close(985357)
    557
    >>> close(14735476)
    143576
    >>> close(812348567)
    1234567
    """
    if n == 0:
      return 0
    no = close(n//10, smallest, d)
    if smallest > n % 10:
        yes = 10 * close(n//10, d, min(d, n%10)) + n%10
        return max(yes, no)
    return no

# ORIGINAL SKELETON FOLLOWS

# def close(n, smallest=10, d=10):
#     """ A sequence is near increasing if each element but the last two is smaller than all elements
#     following its subsequent element. That is, element i must be smaller than elements i + 2, i + 3, i + 4, etc.
#     Implement close, which takes a non-negative integer n and returns the largest near increasing sequence
#     of digits within n as an integer. The arguments smallest and d are part of the implementation; you must
#     determine their purpose. The only values you may use are integers and booleans (True and False) (no lists, strings, etc.).
#     Return the longest sequence of near-increasing digits in n.
#     >>> close(123)
#     123
#     >>> close(153)
#     153
#     >>> close(1523)
#     153
#     >>> close(15123)
#     1123
#     >>> close(11111111)
#     11
#     >>> close(985357)
#     557
#     >>> close(14735476)
#     143576
#     >>> close(812348567)
#     1234567
#     """
#     if n == 0:
#       return 0
#     no = close(n//10, smallest, d)
#     if smallest > n % 10:
#         yes = 10 * close(n//10, d, min(d, n%10)) + n%10
#         return max(yes, no)
#     return no
