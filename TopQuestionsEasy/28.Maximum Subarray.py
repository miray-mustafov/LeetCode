def maxSubArr(nums):
    maxSub = nums[0]
    curSum = 0
    for n in nums:
        if curSum < 0:
            curSum = 0
        curSum += n
        maxSub = max(maxSub, curSum)
    return maxSub


arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
arr2 = [-1,-2,-3]
print(maxSubArr(arr))
