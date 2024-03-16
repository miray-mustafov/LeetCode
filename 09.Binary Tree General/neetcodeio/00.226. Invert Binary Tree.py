from utils.tree.tree import Node, TREE1

# def solution(root):
#     def invert(node):
#         if not node:
#             return
#         invert(node.left)
#         invert(node.right)
#         node.left, node.right = node.right, node.left
#
#     invert(root)
#     return root

def solution(root):
    def invert(node):
        if not node:
            return
        invert(node.left)
        invert(node.right)
        node.left, node.right = node.right, node.left

    def bfs(root):
        if not root:
            return []
        from collections import deque
        res, queue = [], deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            res.append(node.value)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return res

    invert(root)
    return bfs(root)


root: Node = TREE1
print(solution(root))
