def f(nums, k):
    d = {}
    for i in range(len(nums)):
        if nums[i] in d:
            if abs(i - d[nums[i]]) <= k:
                return True

        d[nums[i]] = i
    return False


nums = [1, 2, 1, 1]
nums1 = [1, 2, 3, 1]
k = 3
print(f(nums, 1))
