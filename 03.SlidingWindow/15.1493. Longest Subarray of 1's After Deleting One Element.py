# def sol(nums):
#     data = res = zeroes = 0
#     for r in range(len(nums)):
#         zeroes += 1 if nums[r] == 0 else 0
#         while zeroes > 1:
#             zeroes -= 1 if nums[data] == 0 else 0
#             data += 1
#         res = max(res, r - data)
#     return res

#   0  1  2  3  4  5  6  7  8  9  10


def sol(nums):
    l = res = zeroes = 0
    for r in range(len(nums)):
        zeroes += 1 if nums[r] == 0 else 0
        while zeroes > 1:
            zeroes -= 1 if nums[l] == 0 else 0
            l += 1
        res = max(res, r - l)
    return res


nums = [0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 1]  # 5
print(sol(nums))
# nums = [0, 0, 0]  # 0
# print(sol(nums))
# nums = [1, 0, 0]  # 1
# print(sol(nums))
