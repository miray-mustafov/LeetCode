from utils.tree.tree import make_tree_from_list


def solution(root):
    if not root:
        return True
    res = [True]

    def depth(node):
        if not node:
            return 0
        left_depth = depth(node.left)
        right_depth = depth(node.right)
        if abs(left_depth - right_depth) > 1:
            res[0] = False
        return 1 + max(left_depth, right_depth)

    depth(root)
    return res[0]


root = make_tree_from_list([1, 2, 2, 3, None, None, 3, 4, None, None, 4])
print(solution(root))
