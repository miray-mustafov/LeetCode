class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        return str(f"n{self.data}")


def inorderTraversal(root):
    def inorder(node):
        if not node: return

        inorder(node.left)
        res.append(node.data)
        inorder(node.right)

    res = []
    inorder(root)
    return res


my_binary_tree = Node(1)
my_binary_tree.right = Node(2)
my_binary_tree.right.left = Node(3)
print(inorderTraversal(my_binary_tree))
