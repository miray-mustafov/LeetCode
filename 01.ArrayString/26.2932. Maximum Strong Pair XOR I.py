# 2932. Maximum Strong Pair XOR I
def f(nums):
    max_pair_res = 0
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            x, y = nums[i], nums[j]
            cur_pair_res = x ^ y
            if abs(x - y) <= min(x, y) and cur_pair_res > max_pair_res:
                max_pair_res = cur_pair_res
    return max_pair_res


nums = [1, 2, 3, 4, 5]  # 7
nums2 = [10, 100]
print(f(nums))
print(f(nums2))
