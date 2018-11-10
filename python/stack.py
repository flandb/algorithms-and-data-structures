""" Stack ADT impelementation using different data structures. """


class Stack:
    """
    Abstract data type adhering to LIFO retrieval.
    TODO: add unit tests.
    """

    def __init__(self):
        self._items = []

    def push(self, item):
        """ Adds item to back (top) of Stack. """
        self._items.append(item)

    def pop(self):
        """ Removes and returns top item from Stack. """
        return self._items.pop()

    def __repr__(self):
        """ Unambiguous str rep. of Stack for logging/debugging/repr() """
        return f'Stack({" ".join([str(item) for item in self._items])})'

    # TODO: beautify this with string formatting
    def __str__(self):
        """ Readable str rep. of Stack. """

        # Truncate items in middle if too many items in Stack
        if len(self._items) > 6:
            return (
                'Bottom => '
                f'{" ".join([str(item) for item in self._items[:3]])} '
                '. . . '
                f'{" ".join([str(item) for item in self._items[-3:]])}'
                ' <= Top'
            )

        return (
            'Bottom => '
            f'{" ".join([str(item) for item in self._items])}'
            ' <= Top'
        )

    def __len__(self):
        """ Current number of items in Stack. """
        return len(self._items)

    def __bool__(self):
        """ Truthy is stack not empty, else Falsy """
        return True if self._items else False
