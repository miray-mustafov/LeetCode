def findLHS(nums):
    s = set(nums)
    res = 0
    for el in s:
        if el + 1 in s:
            res = max(res, (nums.count(el) + nums.count(el + 1)))
    return res


def findLHS2(nums):
    num_count = {}

    # Count the occurrences of each number
    for num in nums:
        num_count[num] = num_count.get(num, 0) + 1

    res = 0

    # Check for harmonious subsequence
    for num in num_count:
        if num + 1 in num_count:
            res = max(res, num_count[num] + num_count[num + 1])

    return res


nums = [1, 3, 2, 2, 5, 2, 3, 7]  # 5
nums2 = [1, 2, 3, 4]  # 2
nums3 = [1, 1, 1, 1]  # 0

print(findLHS2(nums))
print(findLHS2(nums2))
print(findLHS2(nums3))
