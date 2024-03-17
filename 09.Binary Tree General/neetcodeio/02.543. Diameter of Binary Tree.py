from utils.tree.tree import TreeNode, make_tree_from_list


def wrongsol(root: TreeNode):
    def f(node):
        if not node:
            return 0
        return 1 + max(f(node.left), f(node.right))

    res = f(root.left)
    res += f(root.right)
    return res


def diameterOfBinaryTree(root: TreeNode) -> int:
    res = [0]

    def depth(node):
        if not node:
            return 0
        left_depth = depth(node.left)
        right_depth = depth(node.right)
        res[0] = max(res[0], left_depth + right_depth)
        return 1 + max(left_depth, right_depth)

    depth(root)
    return res[0]


def diameterOfBinaryTree2(root: TreeNode) -> int:
    def depth(node):
        nonlocal max_diameter
        if not node:
            return 0
        left_depth = depth(node.left)
        right_depth = depth(node.right)
        max_diameter = max(max_diameter, left_depth + right_depth)
        return 1 + max(left_depth, right_depth)

    max_diameter = 0
    depth(root)
    return max_diameter


nums1 = [1, 2, 3, 4, 5]
root1 = make_tree_from_list(nums1)
nums2 = [4, -7, -3, None, None, -9, -3, 9, -7, -4, None, 6, None, -6, -6, None, None, 0, 6, 5, None, 9, None, None, -1,
         -4, None, None, None, -2]
root2 = make_tree_from_list(nums2)
print(wrongsol(root1))  # 3
print(wrongsol(root2))  # 8
print()
print(diameterOfBinaryTree(root1))  # 3
print(diameterOfBinaryTree(root1))  # 3
print()
print(diameterOfBinaryTree2(root1))  # 3
print(diameterOfBinaryTree2(root2))  # 8
