def search(nums, target):
    l, r = 0, len(nums) - 1
    while l <= r:
        m = l + ((r - l) // 2)
        if target > nums[m]:
            l = m + 1
        elif target < nums[m]:
            r = m - 1
        else:
            return m
    return -1


nums = [-1, 0, 3, 5, 9, 12]
target = 9  # 4
print(search(nums, target))
