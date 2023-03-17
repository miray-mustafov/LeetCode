def twoSumOnComplexity(nums, target):
    d = {}
    for i, j in enumerate(nums):
        r = target - j
        if r in d: return [d[r], i]
        d[j] = i


def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


nums = [2, 7, 11, 15, ]
target = 9

print(twoSum(nums, target))
