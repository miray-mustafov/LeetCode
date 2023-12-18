# 2824. Count Pairs Whose Sum is Less than Target
def f(nums, target):
    res = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] < target:
                res += 1
    return res


nums = [-6, 2, 5, -2, -7, -1, 3]
target = -2
print(f(nums, target))
