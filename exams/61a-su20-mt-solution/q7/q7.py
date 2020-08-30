email = 'example_key'

def village(apple, t):
    """
    The `village` operation takes
        a function `apple` that maps an integer to a tree where
            every label is an integer.
        a tree `t` whose labels are all integers

    And applies `apple` to every label in `t`.

    To recombine this tree of trees into a a single tree,
        simply copy all its branches to each of the leaves
        of the new tree.

    For example, if we have
        apple(x) = tree(x, [tree(x + 1), tree(x + 2)])
    and
        t =         10
                  /    \
                20      30

    We should get the output

        village(apple, t)
          =                    10
                           /       \
                        /             \
                      11               12
                    /    \           /    \
                  20      30       20      30
                 / \     /  \     /  \    /  \
                21 22  31   32   21  22  31  32
    >>> t = tree(10, [tree(20), tree(30)])
    >>> apple = lambda x: tree(x, [tree(x + 1), tree(x + 2)])
    >>> print_tree(village(apple, t))
    10
      11
        20
          21
          22
        30
          31
          32
      12
        20
          21
          22
        30
          31
          32
    """
    def graft(t, bs):
        """
        Grafts the given branches `bs` onto each leaf
        of the given tree `t`, returning a new tree.
        """
        if is_leaf(t):
            return tree(label(t), bs)
        new_branches = [graft(b, bs) for b in branches(t)]
        return tree(label(t), new_branches)
    base_t = apple(label(t))
    bs = [village(apple, b) for b in branches(t)]
    return graft(base_t, bs)

def tree(label, branches=[]):
    """Construct a tree with the given label value and a list of branches."""
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'
    return [label] + list(branches)

def label(tree):
    """Return the label value of a tree."""
    return tree[0]

def branches(tree):
    """Return the list of branches of the given tree."""
    return tree[1:]

def is_tree(tree):
    """Returns True if the given tree is a tree, and False otherwise."""
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    """Returns True if the given tree's list of branches is empty, and False
    otherwise.
    """
    return not branches(tree)

def print_tree(t, indent=0):
    """Print a representation of this tree in which each node is
    indented by two spaces times its depth from the entry.
    """
    print('  ' * indent + str(label(t)))
    for b in branches(t):
        print_tree(b, indent + 1)

# ORIGINAL SKELETON FOLLOWS

# def village(apple, t):
#     """
#     The `village` operation takes
#         a function `apple` that maps an integer to a tree where
#             every label is an integer.
#         a tree `t` whose labels are all integers

#     And applies `apple` to every label in `t`.

#     To recombine this tree of trees into a a single tree,
#         simply copy all its branches to each of the leaves
#         of the new tree.

#     For example, if we have
#         apple(x) = tree(x, [tree(x + 1), tree(x + 2)])
#     and
#         t =         10
#                   /    \
#                 20      30

#     We should get the output

#         village(apple, t)
#           =                    10
#                            /       \
#                         /             \
#                       11               12
#                     /    \           /    \
#                   20      30       20      30
#                  / \     /  \     /  \    /  \
#                 21 22  31   32   21  22  31  32
#     >>> t = tree(10, [tree(20), tree(30)])
#     >>> apple = lambda x: tree(x, [tree(x + 1), tree(x + 2)])
#     >>> print_tree(village(apple, t))
#     10
#       11
#         20
#           21
#           22
#         30
#           31
#           32
#       12
#         20
#           21
#           22
#         30
#           31
#           32
#     """
#     def graft(t, bs):
#         """
#         Grafts the given branches `bs` onto each leaf
#         of the given tree `t`, returning a new tree.
#         """
#         if is_leaf(t):
#             return tree(label(t), bs)
#         new_branches = [graft(b, bs) for b in branches(t)]
#         return tree(label(t), new_branches)
#     base_t = apple(label(t))
#     bs = [village(apple, b) for b in branches(t)]
#     return graft(base_t, bs)

# def tree(label, branches=[]):
#     """Construct a tree with the given label value and a list of branches."""
#     for branch in branches:
#         assert is_tree(branch), 'branches must be trees'
#     return [label] + list(branches)

# def label(tree):
#     """Return the label value of a tree."""
#     return tree[0]

# def branches(tree):
#     """Return the list of branches of the given tree."""
#     return tree[1:]

# def is_tree(tree):
#     """Returns True if the given tree is a tree, and False otherwise."""
#     if type(tree) != list or len(tree) < 1:
#         return False
#     for branch in branches(tree):
#         if not is_tree(branch):
#             return False
#     return True

# def is_leaf(tree):
#     """Returns True if the given tree's list of branches is empty, and False
#     otherwise.
#     """
#     return not branches(tree)

# def print_tree(t, indent=0):
#     """Print a representation of this tree in which each node is
#     indented by two spaces times its depth from the entry.
#     """
#     print('  ' * indent + str(label(t)))
#     for b in branches(t):
#         print_tree(b, indent + 1)
