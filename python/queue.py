"""
Queue abstract data type implementation. Queues exhibit FIFO
behavior of items. This implementation will support the following
operations:

enqueue(item): insert item at back of queue.
dequeue(): remove and return first item in queue.
peek(): return item at front of queue.

"""


class Queue:
    """
    Abstract data type enforcing first-in, first-out ordering.

    Implementation stores queue items as array in reversed order, so first
    item to be removed is at last index of array, and last item to be removed
    is first index in array that isn't None. Queue can be initialized to
    specified-length array, and array resized and copied on enqueue when
    array is full -- explicitly create dynamic array over Python's built-in
    dynamic array resizing strictly for the sake of practice.

    TODO: Unit tests.
    TODO: Error handle for dequeue on empty queue, etc.
    TODO: Implement special methods such as __repr__, __str__, etc.
    TODO: Fix implementation.
    """

    def __init__(self, size=0):
        self._items = [None] * size
        self._front_index = 0
        self._size = 0

    def enqueue(self, item):
        """ Add item to back of queue (left of first element in array). """

        # Resize array if currently full.
        if self._size == len(self._items):
            self._resize()

        self._items[len(self._items) - self._size] = item
        self._size += 1

    def dequeue(self):
        """ Remove and return item at front of queue (back of array). """
        item = self._items[self._front_index]
        self._items[self._front_index] = None

        if self._front_index:
            self._front_index -= 1
        if self._size:
            self._size -= 1

        return item

    def peek(self):
        return self._items[]

    def _resize(self):
        """ Double size of queue, copy items from old to back half of new. """
        self._items = ([None] * len(self._items)) + self._items
        self._front_index = len(self._items) - 1

    def __len__(self):
        """ Return number of items currently in queue. """
        return self._size
