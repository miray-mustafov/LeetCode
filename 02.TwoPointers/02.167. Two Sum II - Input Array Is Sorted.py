def f(nums, target):
    l, r = 0, len(nums) - 1
    while l < r:
        curr_sum = nums[l] + nums[r]
        if curr_sum < target:
            l += 1
        elif curr_sum > target:
            r -= 1
        else:
            return [l + 1, r + 1]


nums = [1, 3, 4, 5, 7, 11, 11]
target = 9

print(f(nums, target))
