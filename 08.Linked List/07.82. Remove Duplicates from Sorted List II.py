class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return str(self.val)


def deleteDuplicates(head):  # Nice
    dummy = ListNode(next=head)
    curr, prev = head, dummy
    while curr:
        if curr.next and curr.val == curr.next.val:
            while curr.next and curr.val == curr.next.val:
                curr = curr.next
            prev.next = curr.next
        else:
            prev = curr
        curr = curr.next

    return dummy.next


head = ListNode(1, next=ListNode(1, ListNode(1, ListNode(2, ListNode(3)))))
head11 = ListNode(1, next=ListNode(1))
deleteDuplicates(head)
