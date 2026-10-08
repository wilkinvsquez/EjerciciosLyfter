class Node:
    data: str
    next: "Node"

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        new_node = Node(data)

        if self.root is None:
            self.root = new_node
            return

        current= self.root
        while True:
            if data < current.data:
                if current.left is None:
                    current.left = new_node
                    return
                current = current.left
            else:
                if current.right is None:
                    current.right = new_node
                    return
                current = current.right

    def print_structure(self):
        self._print_structure(self.root, 0)

    def _print_structure(self, node, level):
        if node is None:
            return
        self._print_structure(node.right, level + 1)
        print("    " * level + str(node.data))
        self._print_structure(node.left, level + 1)


tree = BinaryTree()
for value in (10, 5, 15, 3, 7, 20):
    tree.insert(value)

tree.print_structure()