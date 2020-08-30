
def make_zipper(f1, f2, sequence):
    """
    We would like to create a function make_zipper that takes two functions f1(x) and f2(x) and a "zipper
    sequence", which is a number that contains a series of 1s and 2s. It returns a function that is the equivalent of
    f1(f2(f2(...f1(x)...))) in which the exact sequence of f1s and f2s is given by the digits of the sequence.
    As an example, if the sequence were 1211, that would mean return a function of x that is the equivalent to
    f1(f2(f1(f1(x)))). Neither recursion nor containers (lists, dictionaries, sets, etc) are allowed in your solution.

    Return a function of f1 and f2 composed based on sequence.
    >>> increment = lambda x: x + 1
    >>> square = lambda x: x * x
    >>> do_nothing = make_zipper(increment, square, 0)
    >>> do_nothing(2) # Don't call either f1 or f2, just return your input untouched
    2
    >>> incincsq = make_zipper(increment, square, 112)
    >>> incincsq(2) # increment(increment(square(2))), so 2 -> 4 -> 5 -> 6
    6
    >>> sqincsqinc = make_zipper(increment, square, 2121)
    >>> sqincsqinc(2) # square(increment(square(increment(2)))), so 2 -> 3 -> 9 -> 10 -> 100
    100
    """
    zipper = lambda x: x
    helper = lambda f, g: lambda x: f(g(x))
    while sequence != 0:
        if sequence % 10 == 1:
            zipper = helper(f1, zipper)
        else:
            zipper = helper(f2, zipper)
        sequence = sequence // 10
    return zipper

# ORIGINAL SKELETON FOLLOWS

# def make_zipper(f1, f2, sequence):
#     """
#     We would like to create a function make_zipper that takes two functions f1(x) and f2(x) and a "zipper
#     sequence", which is a number that contains a series of 1s and 2s. It returns a function that is the equivalent of
#     f1(f2(f2(...f1(x)...))) in which the exact sequence of f1s and f2s is given by the digits of the sequence.
#     As an example, if the sequence were 1211, that would mean return a function of x that is the equivalent to
#     f1(f2(f1(f1(x)))). Neither recursion nor containers (lists, dictionaries, sets, etc) are allowed in your solution.

#     Return a function of f1 and f2 composed based on sequence.
#     >>> increment = lambda x: x + 1
#     >>> square = lambda x: x * x
#     >>> do_nothing = make_zipper(increment, square, 0)
#     >>> do_nothing(2) # Don't call either f1 or f2, just return your input untouched
#     2
#     >>> incincsq = make_zipper(increment, square, 112)
#     >>> incincsq(2) # increment(increment(square(2))), so 2 -> 4 -> 5 -> 6
#     6
#     >>> sqincsqinc = make_zipper(increment, square, 2121)
#     >>> sqincsqinc(2) # square(increment(square(increment(2)))), so 2 -> 3 -> 9 -> 10 -> 100
#     100
#     """
#     zipper = lambda x: x
#     helper = lambda f, g: lambda x: f(g(x))
#     while sequence != 0:
#         if sequence % 10 == 1:
#             zipper = helper(f1, zipper)
#         else:
#             zipper = helper(f2, zipper)
#         sequence = sequence // 10
#     return zipper
