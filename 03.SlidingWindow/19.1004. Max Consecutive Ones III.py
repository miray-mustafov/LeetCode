def longestOnes(nums, k):
    l = res = zeroes = 0
    for r in range(len(nums)):
        zeroes += 1 if not nums[r] else 0
        while zeroes > k:
            zeroes -= 1 if not nums[l] else 0
            l += 1
        res = max(res, r - l + 1)
    return res


nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
k = 2
# Output: 6
print(longestOnes(nums, k))
