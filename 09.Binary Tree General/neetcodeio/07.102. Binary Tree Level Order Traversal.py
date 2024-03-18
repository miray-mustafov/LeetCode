from utils.tree.tree import TreeNode, make_tree_from_list


def level_order_traversal(root):
    res = []
    from collections import deque
    q = deque([root])
    while q:
        cur_level = []
        for i in range(len(q)):
            node = q.popleft()
            if node:
                cur_level.append(node.val)
                q.append(node.left)
                q.append(node.right)
        if cur_level:
            res.append(cur_level)
    return res
