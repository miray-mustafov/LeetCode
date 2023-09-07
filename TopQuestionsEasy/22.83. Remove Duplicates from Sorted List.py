# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def deleteDuplicates(head):
    dummy = ListNode(0, head)
    n = head
    while n:
        helper = n.next
        while helper and helper.val == n.val:
            helper = helper.next
        n.next = helper
        n = helper
    return dummy.next


head = ListNode(1, next=ListNode(1, ListNode(1, ListNode(2, ListNode(3)))))
deleteDuplicates(head)
# 123
