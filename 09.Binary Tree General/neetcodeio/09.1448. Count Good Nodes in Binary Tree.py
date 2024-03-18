from utils.tree.tree import TreeNode, make_tree_from_list


def goodNodes(root):
    count = [0]

    def preorder_tr(node, cur_max):
        if not node:
            return
        if node.val >= cur_max:
            count[0] += 1
        preorder_tr(node.left, max(cur_max, node.val))
        preorder_tr(node.right, max(cur_max, node.val))

    preorder_tr(root, root.val)
    return count[0]


root = make_tree_from_list([3, 1, 4, 3, 7, 1, 5])
print(goodNodes(root))
