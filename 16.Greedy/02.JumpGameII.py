def jump(nums):
    res = 0
    l, r = 0, 0
    while r < len(nums) - 1:
        farthest = 0
        for i in range(l, r + 1):
            farthest = max(farthest, nums[i] + i)
        l = r + 1
        r = farthest
        res += 1
    return res


nums = [3, 2, 1, 3, 1, 1, 4]
print(jump(nums))
# print(jump_dp(n, n[0], 0, 0))
