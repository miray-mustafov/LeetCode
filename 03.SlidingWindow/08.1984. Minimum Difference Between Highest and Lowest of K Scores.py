def minimumDifference(nums, k):
    nums.sort()
    min_diff = float('inf')
    for i in range(k - 1, len(nums)):
        min_diff = min(min_diff, nums[i] - nums[i - k + 1])
    return min_diff


nums, k = [90], 1  # 0
nums2, k2 = [9, 4, 1, 7], 2  # 2
print(minimumDifference(nums, k))
print(minimumDifference(nums2, k2))
