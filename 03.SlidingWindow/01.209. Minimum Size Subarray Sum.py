def f(target, nums):
    l, r, total = 0, 0, 0
    res = float('inf')
    while r < len(nums):
        total += nums[r]
        while total >= target:
            res = min(r - l + 1, res)
            total -= nums[l]
            l += 1
        r += 1

    return 0 if res == float('inf') else res


target = 7
nums = [2, 3, 1, 2, 4, 3]
print(f(target, nums))
print(f(11, [1, 2, 3, 4, 5]))
print(f(6, [2, 2, 2, 2, 4]))
print(f(6, [2, 2, 3, 3]))
