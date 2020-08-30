email = 'example_key'

def lemon(xv):
    """
    A lemon-copy is a perfect replica of a nested list's box-and-pointer structure.
        If an environment diagram were drawn out, the two should be entirely
        separate but identical.

    A `xv` is a list that only contains ints and other lists.

    The function `lemon` generates a lemon-copy of the given list `xv`.

    Note: The `isinstance` function takes in a value and a type and determines
        whether the value is of the given type. So

        >>> isinstance("abc", str)
        True
        >>> isinstance("abc", list)
        False

    Here's an example, where lemon_y = lemon(y)


                             +-----+-----+            +-----+-----+-----+
                             |     |     |            |     |     |     |
                             |  +  |  +-------------> | 200 | 300 |  +  |
        y +----------------> |  |  |     |            |     |     |  |  |
                             +-----+-----+       +--> +-----+-----+-----+
        lemon_y +-+             |                |       ^           |
                  |             +----------------+       |           |
                  |                                      +-----------+
                  |
                  |          +-----+-----+            +-----+-----+-----+
                  |          |     |     |            |     |     |     |
                  +------->  |  +  |  +-------------> | 200 | 300 |  +  |
                             |  |  |     |            |     |     |  |  |
                             +-----+-----+       +--> +-----+-----+-----+
                                |                |       ^           |
                                +----------------+       |           |
                                                         +-----------+

    >>> x = [200, 300]
    >>> x.append(x)
    >>> y = [x, x]              # this is the `y` from the doctests
    >>> lemon_y = lemon(y)      # this is the `lemon_y` from the doctests
    >>> # check that lemon_y has the same structure as y
    >>> len(lemon_y)
    2
    >>> lemon_y[0] is lemon_y[1]
    True
    >>> len(lemon_y[0])
    3
    >>> lemon_y[0][0]
    200
    >>> lemon_y[0][1]
    300
    >>> lemon_y[0][2] is lemon_y[0]
    True
    >>> # check that lemon_y and y have no list objects in common
    >>> lemon_y is y
    False
    >>> lemon_y[0] is y[0]
    False
    """
    lemon_lookup = []
    def helper(xv):
        if isinstance(xv, int):
            return xv
        for old_new in lemon_lookup:
            if old_new[0] is xv:
                return old_new[1]
        new_xv = []
        lemon_lookup.append((xv, new_xv))
        for element in xv:
            new_xv.append(helper(element))
        return new_xv
    return helper(xv)

# ORIGINAL SKELETON FOLLOWS

# def lemon(xv):
#     """
#     A lemon-copy is a perfect replica of a nested list's box-and-pointer structure.
#         If an environment diagram were drawn out, the two should be entirely
#         separate but identical.

#     A `xv` is a list that only contains ints and other lists.

#     The function `lemon` generates a lemon-copy of the given list `xv`.

#     Note: The `isinstance` function takes in a value and a type and determines
#         whether the value is of the given type. So

#         >>> isinstance("abc", str)
#         True
#         >>> isinstance("abc", list)
#         False

#     Here's an example, where lemon_y = lemon(y)


#                              +-----+-----+            +-----+-----+-----+
#                              |     |     |            |     |     |     |
#                              |  +  |  +-------------> | 200 | 300 |  +  |
#         y +----------------> |  |  |     |            |     |     |  |  |
#                              +-----+-----+       +--> +-----+-----+-----+
#         lemon_y +-+             |                |       ^           |
#                   |             +----------------+       |           |
#                   |                                      +-----------+
#                   |
#                   |          +-----+-----+            +-----+-----+-----+
#                   |          |     |     |            |     |     |     |
#                   +------->  |  +  |  +-------------> | 200 | 300 |  +  |
#                              |  |  |     |            |     |     |  |  |
#                              +-----+-----+       +--> +-----+-----+-----+
#                                 |                |       ^           |
#                                 +----------------+       |           |
#                                                          +-----------+

#     >>> x = [200, 300]
#     >>> x.append(x)
#     >>> y = [x, x]              # this is the `y` from the doctests
#     >>> lemon_y = lemon(y)      # this is the `lemon_y` from the doctests
#     >>> # check that lemon_y has the same structure as y
#     >>> len(lemon_y)
#     2
#     >>> lemon_y[0] is lemon_y[1]
#     True
#     >>> len(lemon_y[0])
#     3
#     >>> lemon_y[0][0]
#     200
#     >>> lemon_y[0][1]
#     300
#     >>> lemon_y[0][2] is lemon_y[0]
#     True
#     >>> # check that lemon_y and y have no list objects in common
#     >>> lemon_y is y
#     False
#     >>> lemon_y[0] is y[0]
#     False
#     """
#     lemon_lookup = []
#     def helper(xv):
#         if isinstance(xv, int):
#             return xv
#         for old_new in lemon_lookup:
#             if old_new[0] is xv:
#                 return old_new[1]
#         new_xv = []
#         lemon_lookup.append((xv, new_xv))
#         for element in xv:
#             new_xv.append(helper(element))
#         return new_xv
#     return helper(xv)
