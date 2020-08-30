
def same_digits(a, b):
    """
    Implement same_digits, which takes two positive integers. It returns whether they both become
    the same number after replacing each sequence of a digit repeated consecutively with only one of that
    digit. For example, in 12222321, the sequence 2222 would be replaced by only 2, leaving 12321.
    Restriction: You may only write combinations of the following in the blanks:
    a, b, end, 10, %, if, while, and, or, ==, !=, True, False, and return. (No division allowed!)

    >>> same_digits(2002200, 2202000) # Ignoring repeats, both are 2020
    True
    >>> same_digits(21, 12) # Digits must appear in the same order
    False
    >>> same_digits(12, 2212) # 12 and 212 are not the same
    False
    >>> same_digits(2020, 20) # 2020 and 20 are not the same
    False
    """
    assert a > 0 and b > 0
    while a and b:
        if ______:
            end = a % 10
            while ______:
                a = a // 10
            while ______:
                b = b // 10
        else:
            ______
    ______

# ORIGINAL SKELETON FOLLOWS

# def same_digits(a, b):
#     """
#     Implement same_digits, which takes two positive integers. It returns whether they both become
#     the same number after replacing each sequence of a digit repeated consecutively with only one of that
#     digit. For example, in 12222321, the sequence 2222 would be replaced by only 2, leaving 12321.
#     Restriction: You may only write combinations of the following in the blanks:
#     a, b, end, 10, %, if, while, and, or, ==, !=, True, False, and return. (No division allowed!)

#     >>> same_digits(2002200, 2202000) # Ignoring repeats, both are 2020
#     True
#     >>> same_digits(21, 12) # Digits must appear in the same order
#     False
#     >>> same_digits(12, 2212) # 12 and 212 are not the same
#     False
#     >>> same_digits(2020, 20) # 2020 and 20 are not the same
#     False
#     """
#     assert a > 0 and b > 0
#     while a and b:
#         if ______:
#             end = a % 10
#             while ______:
#                 a = a // 10
#             while ______:
#                 b = b // 10
#         else:
#             ______
#     ______
