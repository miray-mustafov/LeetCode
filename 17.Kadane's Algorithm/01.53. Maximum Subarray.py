# Kadane's Algorithm involves Dynamic programming and greedy approaches
def maxSubArray(nums):
    maxSum = nums[0]
    curSum = 0

    for n in nums[1:]:
        if curSum < 0:
            curSum = 0
        curSum += n
        maxSum = max(maxSum, curSum)
    return maxSum


def maxSubArray2(nums):
    maxSum = curSum = nums[0]

    for num in nums[1:]:
        curSum = max(num, curSum + num)
        maxSum = max(maxSum, curSum)

    return maxSum


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]  # output 6
numsNegative = [-2, -2, -1, -5, -4]  # -1
print(maxSubArray(nums))
print(maxSubArray2(nums))
print(maxSubArray(numsNegative))
