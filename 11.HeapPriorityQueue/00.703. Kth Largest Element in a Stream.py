import heapq

from utils.tree.tree import view_tree


class KthLargest:

    def __init__(self, k: int, nums):
        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

def left(i):
    return 2 * i


def right(i):
    return 2 * i + 1


def parent(i):
    return i // 2


def max_heapify(arr, heap_size, i):
    l = left(i)
    r = right(i)

    largest = i

    if l < heap_size and arr[l] > arr[i]:
        largest = l

    if r < heap_size and arr[r] > arr[largest]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, heap_size, largest)


def build_max_heap(arr):
    heap_size = len(arr)

    for i in range(heap_size // 2, 0, -1):
        max_heapify(arr, heap_size, i)


def main():
    # root is at index 1
    # it can be at index zero but see here: https://www.quora.com/Why-do-indexes-for-heaps-start-at-1
    # and: https://stackoverflow.com/questions/22900388/why-in-a-heap-implemented-by-array-the-index-0-is-left-unused

    arr = [None, 0, 5, 20, 6, 12, 65, 1, 4, 9, 3, 89, 22, 25, 28, 10]
    build_max_heap(arr)

    # view_tree(arr[1:])

    print(f'Heap: {arr[1:]}')


main()
