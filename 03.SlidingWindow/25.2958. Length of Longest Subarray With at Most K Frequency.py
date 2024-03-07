def f(nums, k):
    from collections import defaultdict
    l = res = 0
    nums_freq = defaultdict(int)
    for r in range(len(nums)):
        nums_freq[nums[r]] += 1
        while nums_freq[nums[r]] > k:
            nums_freq[nums[l]] -= 1
            l += 1
        res = max(res, r - l + 1)
    return res


nums = [1, 2, 3, 1, 2, 3, 1, 2]
k = 2
print(f(nums, k))  # 6
