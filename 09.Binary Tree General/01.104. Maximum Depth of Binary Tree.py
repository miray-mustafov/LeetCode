class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def maxDepth(root):
    if not root:
        return 0
    return 1 + max(maxDepth(root.left), maxDepth(root.right))


root = TreeNode()
root.left = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)

print(maxDepth(root))
