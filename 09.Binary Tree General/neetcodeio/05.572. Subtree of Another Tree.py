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


root = make_tree_from_list([3, 4, 5, 1, 2])
subRoot = make_tree_from_list([4, 1, 2])
print(solution(root, subRoot))
root = make_tree_from_list([3, 4, 5, 1, 2, None, None, None, None, 0])
subRoot = make_tree_from_list([4, 1, 2])
print(solution(root, subRoot))
