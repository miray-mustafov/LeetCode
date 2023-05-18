def majorityElement(nums):
    occurances = {}
    res, max_count = 0, 0
    for n in nums:
        occurances[n] = 1 + occurances.get(n, 0)
        if occurances[n] > max_count:
            res = n
        max_count = max(max_count, occurances[n])
    return res


def mespaceefficient(nums):
    count = 0
    res = 0
    for n in nums:
        if count == 0:
            res = n
        count += (1 if n == res else -1)
    return res


nums = [2, 2, 1, 1, 3, 2, 2]
nums2 = [3, 2, 3]
print(mespaceefficient(nums))
print(mespaceefficient(nums2))
