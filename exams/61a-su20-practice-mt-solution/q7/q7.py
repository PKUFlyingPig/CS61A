
def longest_seq( tr ):
    """ Given a tree, t, find the length of the longest downward sequence of node
    labels in the tree that are increasing consecutive integers. The length of the
    longest downward sequence of nodes in T whose labels are consecutive integers.
    >>> t = Tree (1 , [ Tree (2) , Tree (1 , [ Tree (2 , [ Tree (3 , [ Tree (0)])])])])
    >>> longest_seq( t) # 1 -> 2 -> 3
    3
    >>> t = Tree (1)
    >>> longest_seq( t)
    1
    """
    max_len = 1
    def longest( t ):
        """ Returns longest downward sequence of nodes starting at T whose
        labels are consecutive integers. Updates max_len to that length ,
        if greater. """
        nonlocal max_len
        n = 1
        if not t . is_leaf ():
            for b in t . branches:
                L = longest(b)
                if b. label == t. label + 1:
                    n = max (n , L + 1)
            max_len = max (n , max_len)
        return n
    longest(tr)
    return max_len

### Tree Class definition ###
class Tree:
    def __init__(self, label, branches=[]):
        self.label = label
        for branch in branches:
            assert isinstance(branch, Tree)
        self.branches = list(branches)

    def is_leaf(self):
        return not self.branches

# ORIGINAL SKELETON FOLLOWS

# def longest_seq( tr ):
#     """ Given a tree, t, find the length of the longest downward sequence of node
#     labels in the tree that are increasing consecutive integers. The length of the
#     longest downward sequence of nodes in T whose labels are consecutive integers.
#     >>> t = Tree (1 , [ Tree (2) , Tree (1 , [ Tree (2 , [ Tree (3 , [ Tree (0)])])])])
#     >>> longest_seq( t) # 1 -> 2 -> 3
#     3
#     >>> t = Tree (1)
#     >>> longest_seq( t)
#     1
#     """
#     max_len = 1
#     def longest( t ):
#         """ Returns longest downward sequence of nodes starting at T whose
#         labels are consecutive integers. Updates max_len to that length ,
#         if greater. """
#         nonlocal max_len
#         n = 1
#         if not t . is_leaf ():
#             for b in t . branches:
#                 L = longest(b)
#                 if b. label == t. label + 1:
#                     n = max (n , L + 1)
#             max_len = max (n , max_len)
#         return n
#     longest(tr)
#     return max_len

# ### Tree Class definition ###
# class Tree:
#     def __init__(self, label, branches=[]):
#         self.label = label
#         for branch in branches:
#             assert isinstance(branch, Tree)
#         self.branches = list(branches)

#     def is_leaf(self):
#         return not self.branches
