def f(nums, target):
    l, r = 0, len(nums) - 1
    while l < r:
        if nums[l] + nums[r] == target:
            return [l + 1, r + 1]
        elif nums[l] + nums[r] > target:
            r -= 1
        else:
            l += 1


nums = [1, 3, 4, 5, 7, 11, 11]
target = 9

print(f(nums, target))
