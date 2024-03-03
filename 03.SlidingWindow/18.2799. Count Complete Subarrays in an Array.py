def sol(nums):
    def is_complete(d):
        for key in d:
            if d[key] == 0:
                return False
        return True

    d = {}
    for num in nums:
        if num not in d:
            d[num] = 0

    res = l = 0
    for r, num in enumerate(nums):
        d[num] += 1
        while is_complete(d):
            res += len(nums) - r
            d[nums[l]] -= 1
            l += 1
    return res


def count_complete_subarrays(nums):
    def is_complete(sub_count, total_count):
        return sub_count == total_count

    total_nums_count = len(set(nums))  # Total distinct elements in the array
    l = res = 0
    d = {}
    for r, num in enumerate(nums):
        d[num] = d.get(num, 0) + 1

        while is_complete(len(d), total_nums_count):
            d[nums[l]] -= 1
            if d[nums[l]] == 0:
                del d[nums[l]]
            res += len(nums) - r
            l += 1

    return res


nums = [1, 3, 1, 2, 2]  # 4
nums2 = [1, 3, 1, 2, 2, 2]  # 6
print(sol(nums))
print(sol(nums2))
print()
print(count_complete_subarrays(nums))
print(count_complete_subarrays(nums2))
