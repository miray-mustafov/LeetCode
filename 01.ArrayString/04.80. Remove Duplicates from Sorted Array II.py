def removed(nums):
    if len(nums) < 3:
        return len(nums)

    l = 2
    for r in range(2, len(nums)):
        if nums[r] != nums[l - 2]:
            nums[l] = nums[r]
            l += 1

    return l


nums = [-1, 0, 1, 1, 1, 1, 1, 2, 3, 3, 3, 3, 3, 3]
print(removed(nums), nums)
