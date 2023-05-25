def f(nums):  # sorted and unique
    if len(nums) == 1:
        return [f"{nums[0]}"]
    elif len(nums) == 0:
        return []

    res = []
    nums.append('.')
    a = nums[0]
    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1] + 1:
            b = nums[i]
        else:
            if a == nums[i - 1]:
                res.append(f"{a}")
            else:
                res.append(f"{a}->{b}")
            a = nums[i]

    return res


nums = [0, 2, 3, 4, 6, 8, 9]
# ["0","2->4","6","8->9"]
nums2 = [0, 1, 2, 4, 5, 7]
print(f(nums))
print(f(nums2))
