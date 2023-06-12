class LinkedList:
    def __init__(self, nums_list):
        curnode = ListNode(val=nums_list[0])
        self.head = curnode
        for n in nums_list[1:]:
            curnode.next = ListNode(val=n)
            curnode = curnode.next


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1, l2):
    cnode, num1 = l1, ''
    while cnode is not None:
        num1 += str(cnode.val)
        cnode = cnode.next

    cnode, num2 = l2, ''
    while cnode is not None:
        num2 += str(cnode.val)
        cnode = cnode.next
    num1 = num1[::-1]
    num2 = num2[::-1]
    res = int(num1) + int(num2)

    return res


l1 = [2, 4, 3]
l2 = [5, 6, 4]
ll1 = LinkedList(l1)
ll2 = LinkedList(l2)
print(addTwoNumbers(ll1.head, ll2.head))
