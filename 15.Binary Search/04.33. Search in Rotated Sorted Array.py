def solution(nums, target):
    l, r = 0, len(nums) - 1
    while l <= r:
        m = (l + r) // 2
        if nums[m] == target:
            return m
        if nums[m] < nums[r]:
            if nums[m] < target <= nums[r]:
                l = m + 1
            else:
                r = m - 1
        else:
            if nums[l] <= target < nums[m]:
                r = m - 1
            else:
                l = m + 1
    return -1


nums, target = [4, 5, 6, 7, 0, 1, 2], 0  # 4
print(solution(nums, target))
print(solution([1, 3], 3))
