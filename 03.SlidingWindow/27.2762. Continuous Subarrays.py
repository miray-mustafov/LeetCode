def solution(nums):
    if len(nums) == 1:
        return 1

    l = res = 0
    for r in range(1, len(nums)):
        if 0 <= abs(nums[r - 1] - nums[r]) <= 2:
            res += 1
        else:
            res += (r - l - 1) if (r - l - 1) > 0 else 0
            l = r

    res += (r - l - 1) if (r - l - 1) > 0 else 0
    return res + len(nums)

nums2 = [0, 3, 0, 4, 2, 4]

print(solution([5, 4, 2, 4]))  # 9
print(solution([1, 2, 3]))
print(solution([0, 3, 0, 4, 2, 4]))
