import heapq
from abc import abstractmethod
from utils.tree.tree import view_tree


class KthLargest:

    def __init__(self, k: int, nums):
        self.minHeap, self.k = nums, k
        view_tree(nums)
        heapq.heapify(self.minHeap)
        view_tree(self.minHeap)
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]


# obj = KthLargest(3, [2, 9, 3, 5, 4])
# while True:
#     inp = input()
#     if inp == 'end':
#         break
#     res = obj.add(int(inp))
#     print(res)


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

class MyMaxHeapClass:
    def __init__(self, arr):
        self.heap = arr
        self.build_max_heap()

    @staticmethod
    def left(i):
        return 2 * i

    @staticmethod
    def right(i):
        return 2 * i + 1

    @staticmethod
    def parent(i):
        return i // 2

    def max_heapify(self, i):
        l = self.left(i)
        r = self.right(i)

        largest = i

        if l < len(self.heap) and self.heap[l] > self.heap[i]:
            largest = l

        if r < len(self.heap) and self.heap[r] > self.heap[largest]:
            largest = r

        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self.max_heapify(largest)

    def max_heap_add(self, num):
        self.heap.append(num)
        parent_i = self.parent(len(self.heap) - 1)
        self.max_heapify(parent_i)

    def build_max_heap(self):
        for i in range(len(self.heap) // 2, 0, -1):
            self.max_heapify(i)


def main_implementation():
    # root is at index 1
    # it can be at index zero but see here: https://www.quora.com/Why-do-indexes-for-heaps-start-at-1
    # and: https://stackoverflow.com/questions/22900388/why-in-a-heap-implemented-by-array-the-index-0-is-left-unused

    arr = [None, 0, 5, 20, 6, 12, 65, 1, 4, 9, 3, 89, 22, 25, 28, 10]
    my_heap = MyMaxHeapClass(arr)
    the_heap = my_heap.heap
    # view_tree(the_heap[1:])
    print(f'Heap: {the_heap[1:]}')
    #todo vij adda sus graphiz

main_implementation()
