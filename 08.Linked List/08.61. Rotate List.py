''''
Reminder:
Revise this with neetcode
'''





class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return str(self.val)


def rotate(head, k):
    if k == 0:
        return head
    hmap = {}
    cur, pos = head, 1
    while cur:
        hmap[pos] = cur
        cur, pos = cur.next, pos + 1

    llen = len(hmap)
    if llen == 0:
        return None

    k = k % llen
    if k == 0:
        return head

    right = hmap[llen - k + 1]
    hmap[llen - k].next = None
    hmap[llen].next = head
    return right


head = ListNode(1, next=ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
k = 2
ksame = 7
rotate(head, 2)
