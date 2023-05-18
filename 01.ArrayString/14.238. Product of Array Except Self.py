# Like

def pes_division_On(nums):
    product_all = 1
    zero_idx = -1
    N = len(nums)
    for i in range(N):
        if nums[i] == 0:
            if zero_idx != -1:
                return N * [0]  # When zeroes count > 1 in n
            zero_idx = i
            continue
        product_all *= nums[i]

    if zero_idx != -1:
        answer = [0] * N
        answer[zero_idx] = product_all
        return answer  # When zeroes count is 1 in n

    answer = []
    for i in range(N):
        answer.append(product_all // nums[i])
    return answer  # When no zeroes


def pes(nums):  # tutorial
    res = [1] * (len(nums))

    prefix = 1
    for i in range(len(nums)):
        res[i] = prefix
        prefix *= nums[i]
    postfix = 1
    for i in range(len(nums) - 1, -1, -1):
        res[i] *= postfix
        postfix *= nums[i]
    return res


nums = [1, 2, 3, 4]  # [24,12,8,6]
nums2 = [-1, 1, 0, -3, 3]  # [0, 0, 9, 0, 0]
print(pes_division_On(nums))
print(pes_division_On(nums2))
print(pes(nums))
print(pes(nums2))
