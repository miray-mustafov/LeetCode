def moveZeroes(nums):
    # if len(nums) == 1:
    #     return
    l = 0
    for r in range(len(nums)):
        if nums[r]:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1


nums = [1, 0, 1, 0, 3, 12]
# Output: [1,3,12,0,0]
moveZeroes(nums)
print(nums)
