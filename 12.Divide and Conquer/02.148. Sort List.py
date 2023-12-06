class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return str(self.val)


class Solution:
    def getMid(self, head):
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def merge(self, left, right):
        tail = dummy = ListNode()
        while left and right:
            if left.val < right.val:
                tail.next = left
                left = left.next
            else:
                tail.next = right
                right = right.next
            tail = tail.next
        if left:
            tail.next = left
        if right:
            tail.next = right

        return dummy.next

    def sortList(self, head):
        if not head or not head.next:
            return head

        left = head
        right = self.getMid(head)
        tmp = right.next
        right.next = None
        right = tmp

        left = self.sortList(left)
        right = self.sortList(right)
        return self.merge(left, right)


# head = ListNode(4, ListNode(2, ListNode(1, ListNode(3))))
head = ListNode(4, ListNode(2, ListNode(1, ListNode(3, ListNode(5)))))

sol = Solution()
res = Solution.sortList(sol, head)

print(res)
node = res
while node:
    print(node.val, end=' ')
    node = node.next
