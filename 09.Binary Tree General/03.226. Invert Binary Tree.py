class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invertTree(root):
    if not root:
        return None
    root.left, root.right = root.right, root.left
    invertTree(root.left)
    invertTree(root.right)
    return root

root = TreeNode()
root.left = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)

print(invertTree(root))