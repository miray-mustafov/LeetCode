nums = [0, 1, 6, 7, 9, 7, 12]
n = len(nums)
print(n)
print(n - 2)


def hIndex_not_logn(nums):
    n = len(nums)
    for i in range(n):
        diff = n - i
        if nums[i] >= diff:
            return diff

