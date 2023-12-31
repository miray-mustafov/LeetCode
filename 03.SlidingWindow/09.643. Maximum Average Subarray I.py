def findMaxAverage(nums, k):
    max_sum = cur_sum = sum(nums[:k])
    for i in range(k, len(nums)):
        cur_sum = cur_sum - nums[i - k] + nums[i]
        max_sum = max(max_sum, cur_sum)
    return max_sum / k


nums, k = [1, 12, -5, -6, 50, 3], 4  # Output: 12.75000
nums2, k2 = [5], 1  # Output: 5.00000

print(findMaxAverage(nums, k))
print(findMaxAverage(nums2, k2))
