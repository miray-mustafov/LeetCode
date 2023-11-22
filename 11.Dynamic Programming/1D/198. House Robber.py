def rob(nums):
    dp = [0, 0, 0]
    dp.extend(nums)
    for i in range(3, len(dp)):
        dp[i] = dp[i] + max(dp[i - 2], dp[i - 3])
    return max(dp[-1], dp[-2])


nums = [1, 2, 3, 1]
# Output: 4
print(rob(nums))
