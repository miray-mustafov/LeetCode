# D&C algorithm QuickSelect implemented variation of QuickSort
# 215. Kth Largest Element in an Array
def findKthLargest(nums, k):  # average ON time complexity, worst case ON^2
    k = len(nums) - k

    def quickSelect(l, r):
        pivot, p = nums[r], l
        for i in range(l, r):
            if nums[i] <= pivot:
                nums[p], nums[i] = nums[i], nums[p]
                p += 1

        nums[p], nums[r] = nums[r], nums[p]
        if p > k:
            return quickSelect(l, p - 1)
        elif p < k:
            return quickSelect(p + 1, r)
        else:
            return nums[p]

    return quickSelect(0, len(nums) - 1)


def findKthLargest3(nums, k):
    nums.sort()
    return nums[-k]


def findKthLargest2(nums, k):
    import heapq
    min_heap = nums[:k]
    heapq.heapify(min_heap)

    for num in nums[k:]:
        if num > min_heap[0]:
            heapq.heappushpop(min_heap, num)

    return min_heap[0]


nums, k = [3, 6, 1, 0, 7, 5, 2, 4], 3  # Output: 5
nums2, k2 = [3, 2, 3, 1, 2, 4, 5, 5, 6], 4  # Output: 4

print(findKthLargest2(nums.copy(), k))
print(findKthLargest2(nums2.copy(), k2))
print(findKthLargest3(nums.copy(), k))
print(findKthLargest3(nums2.copy(), k2))
