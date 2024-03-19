from utils.tree.tree import TreeNode, make_tree_from_list


def sol(root, k):
    res = []

    def inorder(node):
        if not node:
            return
        inorder(node.left)
        res.append(node.val)
        inorder(node.right)

    inorder(root)
    return res[k - 1]


root = make_tree_from_list([5, 3, 6, 2, 4, None, None, 1])
print(sol(root, 3))
