class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self):
        return str(f"n{self.val}")


def inorderTraversal(root):
    def inorder(node):
        if not node: return

        inorder(node.left)
        res.append(node.val)
        inorder(node.right)

    res = []
    stack = []
    cur = root
    while cur or stack:
        while cur:
            stack.append(cur)
            cur = cur.left
        cur = stack.pop()
        res.append(cur.val)
        cur = cur.right

    # inorder(root1)
    return res


my_binary_tree = Node(1)
my_binary_tree.left = Node(2)
my_binary_tree.left.left = Node(3)
my_binary_tree.left.right = Node(4)
my_binary_tree.right = Node(5)
print(inorderTraversal(my_binary_tree))  # [3, 2, 4, 1, 5]
