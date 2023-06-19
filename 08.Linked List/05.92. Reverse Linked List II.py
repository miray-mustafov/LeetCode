# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return str(self.val)


def linkedList(arr):
    dummy = ListNode()
    curr = dummy
    for el in arr:
        curr.next = ListNode(el)
        curr = curr.next

    return dummy.next


def reverseBetween(head, left: int, right: int):
    dummy = ListNode(0, head)
    leftPrev, cur = dummy, head
    for i in range(left - 1):
        leftPrev, cur = cur, cur.next
    print(leftPrev, cur)
    prev = None
    for i in range(right - left + 1):
        tmpNext = cur.next
        cur.next = prev
        prev, cur = cur, tmpNext
    print(leftPrev, prev, cur)

    leftPrev.next.next = cur
    leftPrev.next = prev
    return dummy.next


arr = [1, 2, 3, 4, 5]
llist = linkedList(arr)
res = reverseBetween(llist, 2, 4)
