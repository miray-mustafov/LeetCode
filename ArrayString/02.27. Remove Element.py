def removeElement(nums, val):
    l = 0
    r = len(nums) - 1
    while l <= r:
        if nums[r] == val:
            nums[r], r = '_', r - 1
        else:
            if nums[l] == val:
                nums[l] = '_'
                nums[l], nums[r] = nums[r], nums[l]
                r, l = r - 1, l + 1
            else:
                l += 1
    return l


nums = [0, 1, 2, 2, 3, 0, 4, 2]
val = 2
print(removeElement(nums, val))  # Output: 5, n = [0,1,4,0,3,_,_,_]
print(removeElement([1], 1))
