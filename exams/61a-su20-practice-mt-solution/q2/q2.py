
def make_guess(n):
    """
    Let's play a guessing game! In order to do this, we'll use higher order functions.
    Write a function, make_guess, which takes in a number that we want someone to try to guess, and returns a guessing
    function.
    A guessing function is a one-argument function which takes in a number. If the number passed in is the number we
    wanted to guess, it will return the number of incorrect guesses made prior to the correct guess. Otherwise, it returns
    another guessing function, which keeps track of the fact that we've made an incorrect guess.
    Solutions which use lists, object mutation, nonlocal, or global will receive no credit.

    >>> guesser = make_guess(10)
    >>> guess1 = guesser(6)
    >>> guess2 = guess1(7)
    >>> guess3 = guess2(8)
    >>> guess3(10)
    3
    >>> guess2(10)
    2
    >>> a = make_guess(5)(1)(2)(3)(4)(5)
    >>> a
    4
    """
    def update_guess(num_incorrect):
        def new_guess(x):
            if x == n:
                return num_incorrect
            else:
                return update_guess(num_incorrect + 1)
        return new_guess
    return update_guess(0)

# ORIGINAL SKELETON FOLLOWS

# def make_guess(n):
#     """
#     Let's play a guessing game! In order to do this, we'll use higher order functions.
#     Write a function, make_guess, which takes in a number that we want someone to try to guess, and returns a guessing
#     function.
#     A guessing function is a one-argument function which takes in a number. If the number passed in is the number we
#     wanted to guess, it will return the number of incorrect guesses made prior to the correct guess. Otherwise, it returns
#     another guessing function, which keeps track of the fact that we've made an incorrect guess.
#     Solutions which use lists, object mutation, nonlocal, or global will receive no credit.

#     >>> guesser = make_guess(10)
#     >>> guess1 = guesser(6)
#     >>> guess2 = guess1(7)
#     >>> guess3 = guess2(8)
#     >>> guess3(10)
#     3
#     >>> guess2(10)
#     2
#     >>> a = make_guess(5)(1)(2)(3)(4)(5)
#     >>> a
#     4
#     """
#     def update_guess(num_incorrect):
#         def new_guess(x):
#             if x == n:
#                 return num_incorrect
#             else:
#                 return update_guess(num_incorrect + 1)
#         return new_guess
#     return update_guess(0)
