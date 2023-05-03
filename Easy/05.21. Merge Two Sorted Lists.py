class ListNode:
    def __init__(self, val, next=None):
        if isinstance(val, list) and val is not None:
            self.val = val[0]
            self.next = next
            temp = self
            for el in val[1:]:
                temp.next = ListNode(el)
                temp = temp.next
        else:
            self.val = val
            self.next = next

    def __iter__(self):
        node = self
        while node:
            yield node
            node = node.next

    def __repr__(self):
        return str(f"{self.val} > {self.next}")


def mergeTwoLists(l1, l2):
    merged_head = ListNode(0)
    tail = merged_head

    while l1 and l2:
        if l1.val < l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next

    if l1:
        tail.next = l1
    elif l2:
        tail.next = l2

    return merged_head.next


list1_head = ListNode([0, 1, 2, 4, 6, 7])

list2_head = ListNode([1, 3, 4])

result = mergeTwoLists(list1_head, list2_head)
print([node.val for node in result])
