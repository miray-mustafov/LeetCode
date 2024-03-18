from utils.tree.tree import TreeNode, make_tree_from_list


def level_order_traversal(root):
    res = []
    from collections import deque
    q = deque([root])
    while q:
        mostright_node_at_cur_level = None
        for i in range(len(q)):
            node = q.popleft()
            if node:
                mostright_node_at_cur_level = node.val
                q.append(node.left)
                q.append(node.right)
        if mostright_node_at_cur_level:
            res.append(mostright_node_at_cur_level)
    return res


root = make_tree_from_list([3, 9, 20, None, 2, 15, 7])
print(level_order_traversal(root))
