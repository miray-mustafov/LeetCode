def twoSumOnComplexity(nums, target):
    d = {}
    for i, j in enumerate(nums):
        r = target - j
        if r in d: return [d[r], i]
        d[j] = i


nums = [2, 7, 11, 15, ]
target = 9

print(twoSumOnComplexity(nums, target))
