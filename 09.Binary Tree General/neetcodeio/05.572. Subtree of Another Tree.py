from utils.tree.tree import TreeNode, make_tree_from_list


def solution(root, subroot):
    def isSame(a, b):
        if not a and not b:
            return True
        if not a or not b or a.val != b.val:
            return False
        left = isSame(a.left, b.left)
        right = isSame(a.right, b.right)
        boolean = left and right
        return boolean

    def bfs(root):
        from collections import deque
        queue = deque([root])
        while queue:
            node: TreeNode = queue.popleft()
            if node.val == subroot.val and isSame(node, subroot):
                return True
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return False

    is_sub_tree = bfs(root)
    return is_sub_tree


def tutorial_solution(root, subRoot):
    def dfs(node):
        if not node:
            return False
        if node.val == subRoot.val and isSameTree(node, subRoot):
            return True
        leftt = dfs(node.left)
        rightt = dfs(node.right)
        res = leftt or rightt
        return res

    def isSameTree(p, q):
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

    if not subRoot:
        return True
    return dfs(root)


root = make_tree_from_list([3, 4, 5, 1, 2])
subRoot = make_tree_from_list([4, 1, 2])
print(solution(root, subRoot))
print(tutorial_solution(root, subRoot))

print()
root = make_tree_from_list([3, 4, 5, 1, 2, None, None, None, None, 0])
subRoot = make_tree_from_list([4, 1, 2])
print(solution(root, subRoot))
print(tutorial_solution(root, subRoot))
