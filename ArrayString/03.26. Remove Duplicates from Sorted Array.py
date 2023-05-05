def removeDuplicates(nums):
    curr_i = 0
    for i in range(1, len(nums)):
        if nums[curr_i] == nums[i]:
            nums[i] = '_'
        else:
            curr_i += 1
            nums[curr_i], nums[i] = nums[i], nums[curr_i]
    return curr_i + 1, nums

nums = [1, 1, 2]  # [1,2,_]
nums2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]  # [0,1,2,3,4,_,_,_,_,_]

print('k =', removeDuplicates(nums))
print('k =', removeDuplicates(nums2))
