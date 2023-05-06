def majorityElement(nums):
    occurances = {}
    res, max_count = 0, 0
    for n in nums:
        occurances[n] = 1 + occurances.get(n, 0)
        if occurances[n] > max_count:
            res = n
        max_count = max(max_count, occurances[n])
    return res




nums = [2, 2, 1, 1, 1, 2, 2,3]
majorityElement(nums)
