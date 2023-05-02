'''
single = nums[0]
cycle the nums
consider every el thats not in dict and add it to stack

'''


def single_number(nums):  # runtime (On) space (On)
    num_set = set()
    for num in nums:
        if num in num_set:
            num_set.remove(num)
        else:
            num_set.add(num)
    return num_set.pop()


nums = [2, 2, 1]
nums2 = [4, 1, 2, 1, 2]
nums3 = [1]
print(single_number(nums))
print(single_number(nums2))
print(single_number(nums3))
