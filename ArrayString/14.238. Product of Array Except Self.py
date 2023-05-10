def pes_division_On(nums):
    product_all = 1
    zero_idx = -1
    N = len(nums)
    for i in range(N):
        if nums[i] == 0:
            if zero_idx != -1:
                return N * [0]  # When zeroes count > 1 in nums
            zero_idx = i
            continue
        product_all *= nums[i]

    if zero_idx != -1:
        answer = [0] * N
        answer[zero_idx] = product_all
        return answer  # When zeroes count is 1 in nums

    answer = []
    for i in range(N):
        answer.append(product_all // nums[i])
    return answer  # When no zeroes


nums = [1, 2, 3, 4]
nums2 = [-1, 1, 0, -3, 3]
# [24,12,8,6]
print(pes_division_On(nums))
print(pes_division_On(nums2))
