from graphviz import Digraph
from utils.tree.tree import TreeNode
from collections import deque


def view_tree(root_node: TreeNode):
    if not root_node:
        return print("tree empty")
    dot = Digraph()

    # helper function to draw each node and its children
    def draw_node(node: TreeNode):
        if not node:
            return
        dot.node(str(node.val))
        if node.left:
            dot.edge(str(node.val), str(node.left.val))
            draw_node(node.left)
        if node.right:
            dot.edge(str(node.val), str(node.right.val))
            draw_node(node.right)

    draw_node(root_node)
    dot.render(view=True)


def make_tree_from_list(l, stringified=int):
    if not l:
        return ValueError('List empty!')  # [1,2,3,4,5]
    n = len(l)
    root = TreeNode(stringified(l[0]))
    queue = deque([root])

    i = 0
    while queue:
        node = queue.popleft()
        lidx = i * 2 + 1
        ridx = i * 2 + 2
        if lidx < n and l[lidx] is not None:
            node.left = TreeNode(stringified(l[lidx]))
            queue.append(node.left)
        if ridx < n and l[ridx] is not None:
            node.right = TreeNode(stringified(l[ridx]))
            queue.append(node.right)
        i += 1
    return root
