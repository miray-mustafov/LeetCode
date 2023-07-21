# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

    def __repr__(self):
        return str(self.val)


def connect(root):
    cur, nxt = root, root.left if root else None

    while cur and nxt:
        cur.left.next = cur.right
        if cur.next:
            if cur.next.left:
                cur.right.next = cur.next.left
            elif cur.next.right:
                cur.right.next = cur.next.right

        cur = cur.next
        if not cur:
            cur = nxt
            nxt = cur.left
    return root


root = Node(1)
root.left = Node(2)
root.left.left = Node(4)
root.left.right = Node(5)

root.right = Node(3)
root.right.right = Node(7)

connect(root)
