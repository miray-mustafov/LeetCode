def solution(nums):
    l, r = 0, len(nums) - 1
    res = nums[0]
    while l <= r:
        if nums[l] < nums[r]:
            res = min(res, nums[l])
            break

        m = l + ((r - l) // 2)
        res = min(res, nums[m])
        if nums[m] >= nums[l]:
            l = m + 1
        else:
            r = m - 1
    return res


nums = [4, 5, 0, 1, 2, 3]
print(solution(nums))
