from chubb.datastructures.Nodes import TreeNode as Node


class BinarySearchTree:
    def __init__(self):
        self._root = None

    def add(self, value):
        self._root = self._add(self._root, value)

    def _add(self, node, value):
        if node is None:
            return Node(value)

        if value <= node.value:
            node.left = self._add(node.left, value)
        else:
            node.right = self._add(node.right, value)

        return node

    def _inoder(self, node):
        result = ''
        if node is None:
            return ''

        result += self._inoder(node.left)
        result += f'{node.value},'
        result += self._inoder(node.right)

        return result

    def _inorderIter(self, node):
        if node is None:
            return

        for v in self._inorderIter(node.left):
            yield v
        yield node.value

        for v in self._inorderIter(node.right):
            yield v

    def __iter__(self):
        yield from self._inorderIter(self._root)

    def __str__(self):
        return self._inoder(self._root).rstrip(',')
