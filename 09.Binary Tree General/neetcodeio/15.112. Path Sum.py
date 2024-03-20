from utils.tree.tree import TreeNode, make_tree_from_list


def tutorial(root: TreeNode, targetSum):
    def dfs(node, cur_sum=0):
        if not node:
            return False

        cur_sum += node.val
        if not node.left and not node.right:
            return cur_sum == targetSum

        return dfs(node.left, cur_sum) or dfs(node.right, cur_sum)

    return dfs(root)


def hasPathSum(root: TreeNode, targetSum):
    res = [False]

    def dfs(node, cur_sum=0):
        if not node:
            return
        if not node.left and not node.right:  # means we are at a leaf node
            if cur_sum + node.val == targetSum:
                res[0] = True
            return
        dfs(node.left, cur_sum + node.val)
        dfs(node.right, cur_sum + node.val)

    dfs(root)
    return res[0]


root = make_tree_from_list([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1])
targetSum = 22
print(hasPathSum(root, targetSum))
print(tutorial(root, targetSum))
