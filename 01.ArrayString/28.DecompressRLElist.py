def decompressRLElist(nums):
    res = []
    for i in range(1, len(nums), 2):
        l, r = nums[i - 1], nums[i]
        for _ in range(l):
            res.append(r)
    return res


def f(nums):
    result = []
    for i in range(0, len(nums) - 1, 2):

        while nums[i] > 0:
            result.append(nums[i + 1])
            nums[i] -= 1
    return result


nums = [1, 2, 3, 4]
print(decompressRLElist(nums))
print(f(nums))