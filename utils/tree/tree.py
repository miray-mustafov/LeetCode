from collections import deque


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left: Node = left
        self.right: Node = right

    def __repr__(self):
        return f"n{self.value}"


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"n{self.val}"


TREE1 = Node(4, Node(2, Node(1), Node(3)), Node(7, Node(6), Node(9)))


def bfs(root):
    if not root:
        return []
    from collections import deque
    res, queue = [], deque()
    queue.append(root)
    while queue:
        node = queue.popleft()
        res.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return res


def make_tree_from_list(l):
    if not l:
        return ValueError('List empty!')  # [1,2,3,4,5]
    n = len(l)
    root = TreeNode(l[0])
    queue = deque([root])
    for i in range(n):
        node = queue.popleft()
        lidx = i * 2 + 1
        ridx = i * 2 + 2
        if lidx < n:
            node.left = TreeNode(l[lidx])
            queue.append(node.left)
        if ridx < n:
            node.right = TreeNode(l[ridx])
            queue.append(node.right)
    return root


tree = make_tree_from_list([1, 2, 3, 4, 5])
print(bfs(tree))
