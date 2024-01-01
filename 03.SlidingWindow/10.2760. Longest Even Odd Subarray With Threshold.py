def longestAlternatingSubarray(nums, threshold):
    res, l = 0, 0
    while l < len(nums):
        cur_res = 0
        if nums[l] & 1 == 0 and nums[l] <= threshold:
            cur_res, r = 1, l + 1
            while r < len(nums):
                if nums[r] % 2 != nums[r - 1] % 2 and nums[r] <= threshold:
                    cur_res += 1
                else:
                    l = r - 1
                    break
                r += 1

        res = max(res, cur_res)
        l += 1
    return res


#          .3.   9-NO       .3.           .4!.
nums = [4, 5, 2, 9, 2, 2, 2, 1, 2, 2, 2, 3, 4, 1]
threshold = 7
nums2, threshold2 = [1, 2], 2
print(longestAlternatingSubarray(nums, threshold))  # 4
print(longestAlternatingSubarray(nums2, threshold2))  # 1
print(longestAlternatingSubarray([4], 1))  # 0
print(longestAlternatingSubarray([4, 10, 3], 10))  # 2
