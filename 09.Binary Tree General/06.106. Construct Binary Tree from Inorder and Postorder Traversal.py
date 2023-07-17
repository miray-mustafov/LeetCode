# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder, postorder):
        if not postorder or not inorder:
            return None
        root = TreeNode(postorder.pop())

        idx = inorder.index(root.val)
        root.right = self.buildTree(inorder[idx + 1:], postorder)
        root.left = self.buildTree(inorder[:idx], postorder)
        return root


inorder = [9, 3, 15, 20, 7]
postorder = [9, 15, 7, 20, 3]
