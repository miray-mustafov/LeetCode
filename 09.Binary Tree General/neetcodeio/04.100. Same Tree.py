from utils.tree.tree import make_tree_from_list


def isSameTree(p, q):
    def bfs(root):
        if not root:
            return []
        from collections import deque
        res, queue = [], deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            if node:
                res.append(node.val)
            else:
                res.append(None)
                continue

            queue.append(node.left)

            queue.append(node.right)

        return res

    p_list = bfs(p)
    q_list = bfs(q)
    if len(p_list) != len(q_list):
        return False
    for i in range(len(p_list)):
        if p_list[i] != q_list[i]:
            return False
    return True


def tutorial(p, q):
    if not p and not q:
        return True
    if not p or not q or p.val != q.val:
        return False
    left = tutorial(p.left, q.left)
    right = tutorial(p.right, q.right)
    boolean = left and right
    return boolean


p = make_tree_from_list([1, 2, 3])
q = make_tree_from_list([1, 2, 3])
print(isSameTree(p, q))
print(tutorial(p, q))
print()
p = make_tree_from_list([1, 2])
q = make_tree_from_list([1, None, 2])
print(tutorial(p, q))
print(isSameTree(p, q))
