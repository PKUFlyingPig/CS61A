"""The buffer module assists in iterating through lines and tokens."""

import math

class Buffer(object):
    """A Buffer provides a way of accessing a sequence of tokens across lines.

    Its constructor takes an iterator, called "the source", that returns the
    next line of tokens as a list each time it is queried, or None to indicate
    the end of data.

    The Buffer in effect concatenates the sequences returned from its source
    and then supplies the items from them one at a time through its pop()
    method, calling the source for more sequences of items only when needed.

    In addition, Buffer provides a current method to look at the
    next item to be supplied, without sequencing past it.

    The __str__ method prints all tokens read so far, up to the end of the
    current line, and marks the current token with >>.

    >>> buf = Buffer(iter([['(', '+'], [15], [12, ')']]))
    >>> buf.pop()
    '('
    >>> buf.pop()
    '+'
    >>> buf.current()
    15
    >>> print(buf)
    1: ( +
    2:  >> 15
    >>> buf.pop()
    15
    >>> buf.current()
    12
    >>> buf.pop()
    12
    >>> print(buf)
    1: ( +
    2: 15
    3: 12 >> )
    >>> buf.pop()
    ')'
    >>> print(buf)
    1: ( +
    2: 15
    3: 12 ) >>
    >>> buf.pop()  # returns None
    """
    def __init__(self, source):
        self.index = 0
        self.lines = []
        self.source = source
        self.current_line = ()
        self.current()

    def pop(self):
        """Remove the next item from self and return it. If self has
        exhausted its source, returns None."""
        current = self.current()
        self.index += 1
        return current

    @property
    def more_on_line(self):
        return self.index < len(self.current_line)

    def current(self):
        """Return the current element, or None if none exists."""
        while not self.more_on_line:
            self.index = 0
            try:
                self.current_line = next(self.source)
                self.lines.append(self.current_line)
            except StopIteration:
                self.current_line = ()
                return None
        return self.current_line[self.index]

    def __str__(self):
        """Return recently read contents; current element marked with >>."""
        # Format string for right-justified line numbers
        n = len(self.lines)
        msg = '{0:>' + str(math.floor(math.log10(n))+1) + "}: "

        # Up to three previous lines and current line are included in output
        s = ''
        for i in range(max(0, n-4), n-1):
            s += msg.format(i+1) + ' '.join(map(str, self.lines[i])) + '\n'
        s += msg.format(n)
        s += ' '.join(map(str, self.current_line[:self.index]))
        s += ' >> '
        s += ' '.join(map(str, self.current_line[self.index:]))
        return s.strip()

# Try to import readline for interactive history
try:
    import readline
except:
    pass

class InputReader(object):
    """An InputReader is an iterable that prompts the user for input."""
    def __init__(self, prompt):
        self.prompt = prompt

    def __iter__(self):
        while True:
            yield input(self.prompt)
            self.prompt = ' ' * len(self.prompt)
