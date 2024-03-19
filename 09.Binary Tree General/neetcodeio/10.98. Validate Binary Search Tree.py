from utils.tree.tree import TreeNode, make_tree_from_list


def solution(root):
    def dfs(node, left, right):
        if not node:
            return True
        if not (left < node.val < right):
            return False
        l = dfs(node.left, left, node.val)
        r = dfs(node.right, node.val, right)

        return l and r

    return dfs(root, float('-inf'), float('inf'))


def isValidBST(root):  # Wrong
    res = [True]

    def dfs(node: TreeNode, prev: int = None):
        if node.left:
            l = node.left.val
            if l >= node.val or (prev is not None and l <= prev):
                res[0] = False
        if node.right:
            r = node.right.val
            if r <= node.val or (prev is not None and r >= prev):
                res[0] = False

        if node.left:
            dfs(node.left, min(float('inf') if prev is None else prev, node.val))
        if node.right:
            dfs(node.right, max(float('-inf') if prev is None else prev, node.val))

    dfs(root)
    return res[0]


root = make_tree_from_list([5, 1, 4, None, None, 3, 6])  # False
print(isValidBST(root))
root = make_tree_from_list([2, 2, 2])  # False
print(isValidBST(root))
root = make_tree_from_list([5, 4, 7, None, None, None, 9, None, None, 6, None])  # False
print(isValidBST(root))
print()
print(solution(root))
