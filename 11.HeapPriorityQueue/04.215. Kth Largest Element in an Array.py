# with heap
def findKthLargest(nums, k):
    import heapq as h
    for i in range(len(nums)):
        nums[i] = -nums[i]

    h.heapify(nums)
    for _ in range(k - 1):
        h.heappop(nums)

    return -h.heappop(nums)


# with sorting
def f(nums, k):
    nums.sort(reverse=True)
    return nums[k-1]


nums, k = [3, 2, 1, 5, 6, 4], 2
print(findKthLargest(nums.copy(), k))
print(f(nums.copy(), k))
nums, k = [3, 2, 3, 1, 2, 4, 5, 5, 6], 4
print(findKthLargest(nums.copy(), k))
print(f(nums.copy(), k))
