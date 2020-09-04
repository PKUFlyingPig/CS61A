"""The scheme_tokens module provides functions tokenize_line and tokenize_lines
for converting (iterators producing) strings into (iterators producing) lists
of tokens.  A token may be:

  * A number (represented as an int or float)
  * A boolean (represented as a bool)
  * A symbol (represented as a string)
  * A delimiter, including parentheses, dots, and single quotes
"""

import string
import sys

_SYMBOL_STARTS = set('!$%&*/:<=>?@^_~') | set(string.ascii_lowercase)
_SYMBOL_INNERS = _SYMBOL_STARTS | set(string.digits) | set('+-.')
_NUMERAL_STARTS = set(string.digits) | set('+-.')
_WHITESPACE = set(' \t\n\r')
_SINGLE_CHAR_TOKENS = set("()'")
_TOKEN_END = _WHITESPACE | _SINGLE_CHAR_TOKENS
DELIMITERS = _SINGLE_CHAR_TOKENS | {'.'}

def valid_symbol(s):
    """Returns whether s is not a well-formed value."""
    if len(s) == 0 or s[0] not in _SYMBOL_STARTS:
        return False
    for c in s[1:]:
        if c not in _SYMBOL_INNERS:
            return False
    return True

def next_candidate_token(line, k):
    """A tuple (tok, k'), where tok is the next substring of line at or
    after position k that could be a token (assuming it passes a validity
    check), and k' is the position in line following that token.  Returns
    (None, len(line)) when there are no more tokens."""
    while k < len(line):
        c = line[k]
        if c == ';':
            return None, len(line)
        elif c in _WHITESPACE:
            k += 1
        elif c in _SINGLE_CHAR_TOKENS:
            return c, k+1
        elif c == '#':  # Boolean values #t and #f
            return line[k:k+2], min(k+2, len(line))
        else:
            j = k
            while j < len(line) and line[j] not in _TOKEN_END:
                j += 1
            return line[k:j], min(j, len(line))
    return None, len(line)

def tokenize_line(line):
    """The list of Scheme tokens on line.  Excludes comments and whitespace."""
    result = []
    text, i = next_candidate_token(line, 0)
    while text is not None:
        if text in DELIMITERS:
            result.append(text)
        elif text == '+' or text == '-':
            result.append(text)
        elif text == '#t' or text.lower() == 'true':
            result.append(True)
        elif text == '#f' or text.lower() == 'false':
            result.append(False)
        elif text == 'nil':
            result.append(text)
        elif text[0] in _NUMERAL_STARTS:
            try:
                result.append(int(text))
            except ValueError:
                try:
                    result.append(float(text))
                except ValueError:
                    raise ValueError("invalid numeral: {0}".format(text))
        elif text[0] in _SYMBOL_STARTS and valid_symbol(text):
            result.append(text)
        else:
            print("warning: invalid token: {0}".format(text), file=sys.stderr)
            print("    ", line, file=sys.stderr)
            print(" " * (i+3), "^", file=sys.stderr)
        text, i = next_candidate_token(line, i)
    return result

def tokenize_lines(input):
    """An iterator that returns lists of tokens, one for each line of the
    iterable input sequence."""
    return map(tokenize_line, input)
