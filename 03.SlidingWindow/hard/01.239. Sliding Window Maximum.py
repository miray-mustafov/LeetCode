def maxSlidingWindow(nums, k):
    res = []
    for i in range(len(nums)-(k-1)):
        cur_max = nums[i]
        for j in range(i, i + k):
            cur_max = max(nums[j], cur_max)
        res.append(cur_max)
    return res

nums = [1, 3, -1, -3, 5, 3, 6, 7]  # Output: [3,3,5,5,6,7]
k = 3
print(maxSlidingWindow(nums, k))
