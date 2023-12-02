def singleNumber(nums):
    one, two = 0, 0
    for num in nums:
        two = two ^ (one & num)
        one = one ^ num
        not_three = ~(two & one)

        one = not_three & one
        two = not_three & two
    return one


nums1 = [2, 3, 2, 1, 2, 3, 3]
nums2 = [4, 1, 1, 2, 1, 2, 2]
nums3 = [1]
print(singleNumber(nums1))
print(singleNumber(nums2))
print(singleNumber(nums3))
