def rob(nums):
    def helper(nums):
        rob1, rob2 = 0, 0
        for n in nums:
            temp = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2

    return max(helper(nums[1:]), helper(nums[:-1]))


nums = [2, 3, 4, 4]
nums2 = [2, 3, 2]
print(rob(nums2))
print(rob(nums))
