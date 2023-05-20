# def twoSumOnComplexity(nums, target):
#     d = {}
#     for i, j in enumerate(nums):
#         r = target - j
#         if r in d: return [d[r], i]
#         d[j] = i


def f2(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


def f(nums, target):
    d = {}
    for i in range(len(nums)):
        r = target - nums[i]
        if r in d:
            return [d[r], i]
        d[nums[i]] = i


nums = [1, 2, 10, 7, 11, 15, 4]
target = 9

print(f(nums, target))
print(f2(nums, target))
