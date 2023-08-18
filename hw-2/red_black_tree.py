class Node:
    def __init__(self, value, color='RED', left=None, right=None):
        self.value = value
        self.color = color
        self.left = left
        self.right = right

    def __str__(self):
        color_str = 'RED' if self.color == 'RED' else 'BLACK'
        return f'Node(value={self.value}, color={color_str})'


class RedBlackTree:
    def __init__(self):
        self.root = None

    def rotate_left(self, node):
        new_root = node.right
        node.right = new_root.left
        new_root.left = node
        new_root.color, node.color = node.color, 'RED'
        return new_root

    def rotate_right(self, node):
        new_root = node.left
        node.left = new_root.right
        new_root.right = node
        new_root.color, node.color = node.color, 'RED'
        return new_root

    def flip_colors(self, node):
        node.color = 'RED'
        node.left.color = 'BLACK'
        node.right.color = 'BLACK'

    def insert(self, value):
        self.root = self._insert(self.root, value)
        self.root.color = 'BLACK'

    def _insert(self, node, value):
        if node is None:
            return Node(value)

        if value < node.value:
            node.left = self._insert(node.left, value)
        elif value > node.value:
            node.right = self._insert(node.right, value)

        if self.is_red(node.right) and not self.is_red(node.left):
            node = self.rotate_left(node)
        if self.is_red(node.left) and self.is_red(node.left.left):
            node = self.rotate_right(node)
        if self.is_red(node.left) and self.is_red(node.right):
            self.flip_colors(node)

        return node

    def is_red(self, node):
        return node is not None and node.color == 'RED'

    def print_tree(self, node, level=0):
        if node is not None:
            self.print_tree(node.right, level + 1)
            print('   ' * level + str(node))
            self.print_tree(node.left, level + 1)


# Пример использования
tree = RedBlackTree()
values = [15, 10, 20, 5, 12, 25]
for value in values:
    tree.insert(value)

tree.print_tree(tree.root)
