from graphviz import Digraph
from utils.tree.tree import TreeNode
from collections import deque
from utils.tree.tree import make_tree_from_list

def view_tree(root_node: TreeNode | list):
    if not root_node:
        return print("tree empty")
    if isinstance(root_node, list):
        root_node = make_tree_from_list(root_node)

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
