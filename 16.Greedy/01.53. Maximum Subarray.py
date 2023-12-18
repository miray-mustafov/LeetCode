def maxSubArray(nums):
    maxSum = nums[0]
    curSum = 0

    for n in nums[1:]:
        if curSum < 0:
            curSum = 0
        curSum += n
        maxSum = max(maxSum, curSum)
    return maxSum


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]  # output 6
numsNegative = [-2, -2, -1, -5, -4]  # -1
print(maxSubArray(nums))
print(maxSubArray(numsNegative))
