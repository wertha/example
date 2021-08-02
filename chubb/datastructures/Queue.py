from chubb.datastructures.Nodes import SimpleNode as Node
from chubb.exceptions import QueueOverflowError
from chubb.exceptions import QueueUnderflowError


class Queue:
    def __init__(self, size=None):
        self._size = size
        self._currentSize = 0
        self._root = None
        self._last = None

    def enqueue(self, value):
        node = Node(value)
        self._currentSize += 1

        if self._root is None:
            self._root = node
            self._last = node
            return

        if self._size is not None and self._currentSize > self._size:
            raise QueueOverflowError(
                f'Trying to add {self._currentSize} elements when the limit is {self._size}'
            )

        self._last.next = node
        self._last = node

    def dequeue(self):
        if self._root is None:
            raise QueueUnderflowError()

        result = self._root.value
        self._root = self._root.next
        self._currentSize -= 1

        return result

    def __iter__(self):
        while self._root is not None:
            yield self.dequeue()

    def __str__(self):
        result = ''
        tmp = self._root
        while tmp is not None:
            result += f'{tmp.value} -> '
            tmp = tmp.next

        return result

    def __repr__(self):
        result = ''
        tmp = self._root
        while tmp is not None:
            result += f'{tmp.value},'
            tmp = tmp.next

        return result.rstrip(',')