from utils.tree.tree import TreeNode


def max_path_sum(root):
    max_sum = [root.val]

    # return max path sum without split
    def dfs(node):
        if not node:
            return 0

        left_max = dfs(node.left)
        right_max = dfs(node.right)
        left_max = max(left_max, 0)
        right_max = max(right_max, 0)

        # consider max path sum with a split
        max_sum[0] = max(max_sum[0], node.val + left_max + right_max)
        res = node.val + max(left_max, right_max)
        return res

    dfs(root)
    return max_sum[0]


root = TreeNode(-10)
root.left = TreeNode(100)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(max_path_sum(root))
