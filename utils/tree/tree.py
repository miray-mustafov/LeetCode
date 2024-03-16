class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left: Node = left
        self.right: Node = right

    def __repr__(self):
        return f"n{self.value}"


TREE1 = Node(4, Node(2, Node(1), Node(3)), Node(7, Node(6), Node(9)))
