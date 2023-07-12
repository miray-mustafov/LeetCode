class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSymmetric(self, root):
    def dfs(left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False

        return left.val == right.val and dfs(left.left, right.right) and dfs(left.right, right.left)

    return dfs(root.left, root.right)


root = TreeNode()
root.left = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)

print(isSymetric(root))
