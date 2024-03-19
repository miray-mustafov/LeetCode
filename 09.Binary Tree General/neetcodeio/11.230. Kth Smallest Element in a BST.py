from utils.tree.tree import TreeNode, make_tree_from_list


def sol_iteratively(root, k):
    node = root
    n = 0
    stack = []
    while node or stack:
        while node:
            stack.append(node)
            node = node.left
        node = stack.pop()
        n += 1
        if n == k:
            return node.val
        node = node.right


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
print(sol_iteratively(root, 3))
