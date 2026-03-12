import heapq


class KthSmallest:

    def __init__(self, k: int, nums):
        self.maxHeap = [-num for num in nums]
        heapq.heapify(self.maxHeap)
        cur_length = len(self.maxHeap)
        while cur_length > k:
            heapq.heappop(self.maxHeap)
            cur_length -= 1

    def add(self, val: int) -> int:
        self.maxHeap.heappush(-val)
        if len(self.maxHeap) > self.k:
            heapq.heappop(self.maxHeap)

    @property
    def kth_smallest(self):
        return -self.maxHeap[0]


ks = KthSmallest(4, [1, 2, 3, 4, 5, 6, 7])
print(ks.kth_smallest)
