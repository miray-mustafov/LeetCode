from utils.tree.tree import TreeNode, view_tree


def buildTree(preorder, inorder):
    if not preorder:
        return
    root: TreeNode = TreeNode(preorder[0])
    split = inorder.index(preorder[0])
    root.left = buildTree(preorder[1:split + 1], inorder[:split])
    root.right = buildTree(preorder[split + 1:], inorder[split + 1:])
    return root


preorder = [3, 9, 8, 20, 15, 7]
inorder = [9, 8, 3, 15, 20, 7]
buildTree(preorder, inorder)
# view_tree(root)
