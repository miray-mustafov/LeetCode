class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self):
        return str(f"n{self.val}")


def isSymmetric(root):
    def dfs(left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False

        return left.val == right.val \
               and dfs(left.left, right.right) \
               and dfs(left.right, right.left)

    return dfs(root.left, root.right)


tree = Node(1)
tree.left = Node(2)
tree.right = Node(2)

tree.left.left = Node(3)
tree.right.right = Node(3)

tree.left.right = Node(4)
tree.right.left = Node(4)
print(isSymmetric(tree))


def isSymmetric(self, root):
    def dfs(left, right):
        if not (left or right):
            return True
        if not (left and right):
            return False
        if left.val != right.val:
            return False
        return dfs(left.left, right.right) and dfs(left.right, right.left)

    if not root:
        return True
    return dfs(root.left, root.right)