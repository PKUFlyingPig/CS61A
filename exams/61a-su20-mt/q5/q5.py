email = 'example_key'

def subsaltshaker(disk):
    """
    A 'saltshaker' is a sequence of digits of length `d` composed entirely of the digit `d`. Examples include
        1
        4444
        7777777

    Note that `1 <= d <= 9`; there are no 0-length saltshakers.

    Your task is to implement the `subsaltshaker` function, which takes in an integer `disk` and returns
        whether `disk` contains a saltshaker as a consecutive subinteger of its digits.

    >>> subsaltshaker(2233) # 22 counts
    True
    >>> subsaltshaker(2444423) # 4444 counts
    True
    >>> subsaltshaker(82223) # 22 counts even if it appears as part of 222
    True
    >>> subsaltshaker(234562) # 2...2 does not count if the 2s are not consecutive
    False
    >>> subsaltshaker(1) # 1 counts
    True
    >>> subsaltshaker(498729879871) # 1 counts
    True
    >>> subsaltshaker(149872987987) # 1 counts
    True
    >>> subsaltshaker(4445555) # no saltshakers in this number
    False
    >>> subsaltshaker(20) # no saltshakers in this number
    False
    """
    current_digit = disk%10
    count = 0
    while disk:
        last = disk%10
        if last == current_digit:
            count += 1
        else:
            count = 1
            current_digit = last
        if current_digit == count:
            return True
        disk = disk//10
    return False

# ORIGINAL SKELETON FOLLOWS

# def subsaltshaker(disk):
#     """
#     A 'saltshaker' is a sequence of digits of length `d` composed entirely of the digit `d`. Examples include
#         1
#         4444
#         7777777

#     Note that `1 <= d <= 9`; there are no 0-length saltshakers.

#     Your task is to implement the `subsaltshaker` function, which takes in an integer `disk` and returns
#         whether `disk` contains a saltshaker as a consecutive subinteger of its digits.

#     >>> subsaltshaker(2233) # 22 counts
#     True
#     >>> subsaltshaker(2444423) # 4444 counts
#     True
#     >>> subsaltshaker(82223) # 22 counts even if it appears as part of 222
#     True
#     >>> subsaltshaker(234562) # 2...2 does not count if the 2s are not consecutive
#     False
#     >>> subsaltshaker(1) # 1 counts
#     True
#     >>> subsaltshaker(498729879871) # 1 counts
#     True
#     >>> subsaltshaker(149872987987) # 1 counts
#     True
#     >>> subsaltshaker(4445555) # no saltshakers in this number
#     False
#     >>> subsaltshaker(20) # no saltshakers in this number
#     False
#     """
#     current_digit = ______
#     count = ______
#     while ______:
#         last = ______
#         if ______:
#             count += 1
#         else:
#             count = ______
#             ______
#         if ______:
#             ______
#         disk = ______
#     return ______
