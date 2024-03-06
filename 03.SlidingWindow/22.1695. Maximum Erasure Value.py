def f(nums):  # slight diff with the continue keyword
    unique_sub = set()
    l = res = cur_res = 0
    for r in range(len(nums)):
        if nums[r] not in unique_sub:
            unique_sub.add(nums[r])
            cur_res += nums[r]
            continue
        res = max(res, cur_res)
        while True:
            if nums[l] == nums[r]:
                l += 1
                break
            unique_sub.remove(nums[l])
            cur_res -= nums[l]
            l += 1
        res = max(res, cur_res)
    return max(res, cur_res)


def f2(nums):  # correct one
    unique_sub = set()
    l = res = cur_res = 0
    for r in range(len(nums)):
        if nums[r] not in unique_sub:
            unique_sub.add(nums[r])
            cur_res += nums[r]
        else:
            while True:
                if nums[l] == nums[r]:
                    l += 1
                    break
                unique_sub.remove(nums[l])
                cur_res -= nums[l]
                l += 1
        res = max(res, cur_res)
    return max(res, cur_res)


nums = [4, 2, 4, 5, 6]  # res 17
print(f2(nums))
nums = [5, 2, 1, 2, 6, 2, 1, 2, 5]  # res 9
print(f2(nums))

nums = [449, 154, 934, 526, 429, 732, 784, 909, 884, 805, 635, 660, 742, 209, 742, 272, 669, 449, 766, 904, 698, 434,
        280, 332, 876, 200, 333, 464, 12, 437, 269, 355, 622, 903, 262, 691, 768, 894, 929, 628, 867, 844, 208, 384,
        644, 511, 908, 792, 56, 872, 275, 598, 633, 502, 894, 999, 788, 394, 309, 950, 159, 178, 403, 110, 670, 234,
        119, 953, 267, 634, 330, 410, 137, 805, 317, 470, 563, 900, 545, 308, 531, 428, 526, 593, 638, 651, 320, 874,
        810, 666, 180, 521, 452, 131, 201, 915, 502, 765, 17, 577, 821, 731, 925, 953, 111, 305, 705, 162, 994, 425, 17,
        140, 700, 475, 772, 385, 922, 159, 840, 367, 276, 635, 696, 70, 744, 804, 63, 448, 435, 242, 507, 764, 373, 314,
        140, 825, 34, 383, 151, 602, 745]
print(f(nums))
print(f2(nums))  # res 30934

from compare_time import compare_time_of2

compare_time_of2(f, f2, nums)
