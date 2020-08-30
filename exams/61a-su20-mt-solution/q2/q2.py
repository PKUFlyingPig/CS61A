email = 'example_key'

def schedule(galaxy, sum_to, max_digit):
    """
    A 'galaxy' is a string which contains either digits or '?'s.

    A 'completion' of a galaxy is a string that is the same as galaxy, except
    with digits replacing each of the '?'s.

    Your task in this question is to find all completions of the given `galaxy`
    that use digits up to `max_digit`, and whose digits sum to `sum_to`.

    Note 1: the function int can be used to convert a string to an integer and str
        can be used to convert an integer to a string as such:

        >>> int("5")
        5
        >>> str(5)
        '5'

    Note 2: Indexing and slicing can be used on strings as well as on lists.

        >>> 'evocative'[3]
        'c'
        >>> 'evocative'[3:]
        'cative'
        >>> 'evocative'[:6]
        'evocat'
        >>> 'evocative'[3:6]
        'cat'


    >>> schedule('?????', 25, 5)
    ['55555']
    >>> schedule('???', 5, 2)
    ['122', '212', '221']
    >>> schedule('?2??11?', 5, 3)
    ['0200111', '0201110', '0210110', '1200110']
    """
    def schedule_helper(galaxy, sum_sofar, index):
        if index >= len(galaxy) and sum_sofar == sum_to:
            return [galaxy]
        elif sum_sofar > sum_to or index >= len(galaxy):
            return []
        elif galaxy[index] != '?':
            return schedule_helper(galaxy, sum_sofar + int(galaxy[index]), index + 1)
        ans = []
        for x in range(max_digit + 1):
            modified_galaxy = galaxy[:index] + str(x) + galaxy[index + 1:]
            ans += schedule_helper(modified_galaxy, sum_sofar + x, index + 1)
        return ans

    return schedule_helper(galaxy, 0, 0)

# ORIGINAL SKELETON FOLLOWS

# def schedule(galaxy, sum_to, max_digit):
#     """
#     A 'galaxy' is a string which contains either digits or '?'s.

#     A 'completion' of a galaxy is a string that is the same as galaxy, except
#     with digits replacing each of the '?'s.

#     Your task in this question is to find all completions of the given `galaxy`
#     that use digits up to `max_digit`, and whose digits sum to `sum_to`.

#     Note 1: the function int can be used to convert a string to an integer and str
#         can be used to convert an integer to a string as such:

#         >>> int("5")
#         5
#         >>> str(5)
#         '5'

#     Note 2: Indexing and slicing can be used on strings as well as on lists.

#         >>> 'evocative'[3]
#         'c'
#         >>> 'evocative'[3:]
#         'cative'
#         >>> 'evocative'[:6]
#         'evocat'
#         >>> 'evocative'[3:6]
#         'cat'


#     >>> schedule('?????', 25, 5)
#     ['55555']
#     >>> schedule('???', 5, 2)
#     ['122', '212', '221']
#     >>> schedule('?2??11?', 5, 3)
#     ['0200111', '0201110', '0210110', '1200110']
#     """
#     def schedule_helper(galaxy, sum_sofar, index):
#         if index >= len(galaxy) and sum_sofar == sum_to:
#             return [galaxy]
#         elif sum_sofar > sum_to or index >= len(galaxy):
#             return []
#         elif galaxy[index] != '?':
#             return schedule_helper(galaxy, sum_sofar + int(galaxy[index]), index + 1)
#         ans = []
#         for x in range(max_digit + 1):
#             modified_galaxy = galaxy[:index] + str(x) + galaxy[index + 1:]
#             ans += schedule_helper(modified_galaxy, sum_sofar + x, index + 1)
#         return ans

#     return schedule_helper(galaxy, 0, 0)
