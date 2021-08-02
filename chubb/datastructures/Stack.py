class StackOverflowError(Exception):
    pass

class StackUnderflowError(Exception):
    pass

class _Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self, size=None):
        self._size = size
        self._root = None
        self._currentSize = 0
    

    def push(self, value):
        node = _Node(value)
        self._currentSize += 1

        if self._root is None:
            self._root = node
            return

        if self._size is not None and self._currentSize > self._size:
            raise StackOverflowError(f'Trying to add {self._currentSize} elements when the limit is {self._size}')

        node.next = self._root
        self._root = node
    
    def pop(self):
        if self._root is None:
            raise StackUnderflowError()
        
        result = self._root.value
        self._root = self._root.next
        self._currentSize -= 1

        return result

    def __iter__(self):
        while self._root is not None:
            yield self.pop()
    
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
      
