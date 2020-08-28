"Utility functions for file and string manipulation"

import string
from math import sqrt

def lines_from_file(path):
    """Return a list of strings, one for each line in a file."""
    with open(path, 'r') as f:
        return [line.strip() for line in f.readlines()]


punctuation_remover = str.maketrans('', '', string.punctuation)


def remove_punctuation(s):
    """Return a string with the same contents as s, but with punctuation removed.

    >>> remove_punctuation("It's a lovely day, don't you think?")
    'Its a lovely day dont you think'
    """
    return s.strip().translate(punctuation_remover)


def lower(s):
    """Return a lowercased version of s."""
    return s.lower()


def split(s):
    """Return a list of words contained in s, which are sequences of characters
    separated by whitespace (spaces, tabs, etc.).

    >>> split("It's a lovely day, don't you think?")
    ["It's", 'a', 'lovely', 'day,', "don't", 'you', 'think?']
    """
    return s.split()

#########################################
# Functions relating to keyboard layout #
#########################################

KEY_LAYOUT = [["1","2","3","4","5","6","7","8","9","0","-","="],
              ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p","[","]"],
			  ["a", "s", "d", "f", "g", "h", "j", "k", "l",";","'"],
			  ["z", "x", "c", "v", "b", "n", "m",",",".","/"],
              [" "]]

def distance(p1, p2):
	"""Return the Euclidean distance between two points

	The Euclidean distance between two points, (x1, y1) and (x2, y2)
	is the square root of (x1 - x2) ** 2 + (y1 - y2) ** 2

	>>> distance((0, 1), (1, 1))
	1
	>>> distance((1, 1), (1, 1))
	0
	>>> round(distance((4, 0), (0, 4)), 3)
	5.657
	"""
	return sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def get_key_distances():
	"""Return a new dictionary mapping key pairs to distances.

	Each key of the dictionary is a tuple of two
	letters as strings, and each value is the euclidean distance
	between the two letters on a standard QWERTY keyboard normalized
	such that the greatest distance is 2.0

	The scaling is constant, so a pair of keys that are twice
	as far have a distance value that is twice as great

	>>> distances = get_key_distances()
	>>> distances["a", "a"]
	0.0
	>>> distances["a", "d"] # 2.0 / 9
	2.0
	>>> distances["d", "a"]
	2.0
	"""
	key_distance = {}

	def compute_pairwise_distances(i, j, d):
		for x in range(len(KEY_LAYOUT)):
			for y in range(len(KEY_LAYOUT[x])):
				l1 = KEY_LAYOUT[i][j]
				l2 = KEY_LAYOUT[x][y]
				d[l1, l2] = distance((i, j), (x, y))

	for i in range(len(KEY_LAYOUT)):
		for j in range(len(KEY_LAYOUT[i])):
			compute_pairwise_distances(i, j, key_distance)

	max_value = max(key_distance.values())
	return {key : value * 8 / max_value for key, value in key_distance.items()}

def count(f):
    """Keeps track of the number of times a function f is called using the
    variable call_count

    >>> def factorial(n):
    ...     if n <= 1:
    ...         return 1
    ...     return n * factorial(n - 1)
    >>> factorial = count(factorial)
    >>> factorial(5)
    120
    >>> factorial.call_count
    5
    """
    def counted(*args):
        counted.call_count += 1
        return f(*args)
    counted.call_count = 0
    return counted