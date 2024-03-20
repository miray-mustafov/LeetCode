from graphviz import Digraph
from utils.tree.tree import TreeNode


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
