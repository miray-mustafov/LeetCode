# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def countNodes(root):
    if not root:
        return 0

    def calc_lefth(node):
        if not node:
            return 0
        return calc_lefth(node.left) + 1

    def calc_righth(node):
        if not node:
            return 0
        return calc_righth(node.right) + 1

    lh, rh = calc_lefth(root), calc_righth(root)
    if lh == rh:
        return (2 ** lh) - 1
    return 1 + countNodes(root.left) + countNodes(root.right)


root = TreeNode(0, left=TreeNode(1, left=TreeNode(2)), right=TreeNode(1))
print(countNodes(root))
