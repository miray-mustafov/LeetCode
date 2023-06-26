# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return str(self.val) + 'node'


def removeNthFromEnd(head, n: int):
    curr, count, d = head, -1, {}
    while curr is not None:
        count += 1
        d[count] = curr
        curr = curr.next

    spot = count - n
    if spot == -2:
        return None
    elif spot == -1:
        return head.next

    prev = d[spot]
    prev.next = prev.next.next
    return head


def pointers(head, n: int):
    dummy = ListNode(0, head)
    l = dummy
    r = head
    while n > 0 and r:
        r = r.next
        n -= 1
    while r:
        l = l.next
        r = r.next
    l.next = l.next.next
    return dummy.next


head1 = ListNode(1)
head = ListNode(1, next=ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
removeNthFromEnd(head, 1)
