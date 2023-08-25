# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def averageOfLevels(root):
    from collections import defaultdict
    S = defaultdict(float)
    T = defaultdict(int)

    def dfs(node, h):
        if not node: return
        dfs(node.left, h + 1)
        dfs(node.right, h + 1)
        S[h] += node.val
        T[h] += 1

    dfs(root, 0)

    res = []
    for i in range(len(S)):
        res.append(S[i] / T[i])
    return res
