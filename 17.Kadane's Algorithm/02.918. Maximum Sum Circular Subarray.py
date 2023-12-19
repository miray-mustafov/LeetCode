# 918. Maximum Sum Circular Subarray
def maxSubarraySumCircular(nums):
    total = globalMax = curMax = globalMin = curMin = nums[0]

    for num in nums[1:]:
        curMax = max(num, curMax + num)
        globalMax = max(globalMax, curMax)
        curMin = min(num, curMin + num)
        globalMin = min(globalMin, curMin)
        total += num

    if globalMax < 0:
        return globalMax
    return max(globalMax, total - globalMin)


nums = [1, -2, 3, -2]  # 3
nums2 = [5, -3, 5]  # 10
nums3 = [-3, -2, -3]  # -2
print(maxSubarraySumCircular(nums))
print(maxSubarraySumCircular(nums2))
print(maxSubarraySumCircular(nums3))
