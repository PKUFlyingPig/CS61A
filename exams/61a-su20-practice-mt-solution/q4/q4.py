
def sums(n, k):
    """
    Implement sums, which takes two positive integers n and k. It returns a list of lists containing all
    the ways that a list of k positive integers can sum to n. Results can appear in any order.

    Return the ways in which K positive integers can sum to N.
    >>> sums(2, 2)
    [[1, 1]]
    >>> sums(2, 3)
    []
    >>> sums(4, 2)
    [[3, 1], [2, 2], [1, 3]]
    >>> sums(5, 3)
    [[3, 1, 1], [2, 2, 1], [1, 3, 1], [2, 1, 2], [1, 2, 2], [1, 1, 3]]
    """
    if k == 1:
        return [[n]]
    y = []
    for x in range(1, n):
        y.extend([s + [x] for s in sums(n-x, k-1)])
    return y

# ORIGINAL SKELETON FOLLOWS

# def sums(n, k):
#     """
#     Implement sums, which takes two positive integers n and k. It returns a list of lists containing all
#     the ways that a list of k positive integers can sum to n. Results can appear in any order.

#     Return the ways in which K positive integers can sum to N.
#     >>> sums(2, 2)
#     [[1, 1]]
#     >>> sums(2, 3)
#     []
#     >>> sums(4, 2)
#     [[3, 1], [2, 2], [1, 3]]
#     >>> sums(5, 3)
#     [[3, 1, 1], [2, 2, 1], [1, 3, 1], [2, 1, 2], [1, 2, 2], [1, 1, 3]]
#     """
#     if k == 1:
#         return [[n]]
#     y = []
#     for x in range(1, n):
#         y.extend([s + [x] for s in sums(n-x, k-1)])
#     return y
