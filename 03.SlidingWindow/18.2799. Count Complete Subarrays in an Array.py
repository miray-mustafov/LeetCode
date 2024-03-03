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


nums = [1, 3, 1, 2, 2]  # 4
nums2 = [1, 3, 1, 2, 2, 2]  # 6
print(sol(nums))
print(sol(nums2))
"""
def numberOfSubstrings(s: str):
    n, l, r = len(s), 0, 0
    abc = {'a': 0, 'b': 0, 'c': 0}
    res = 0
    while r < n:
        abc[s[r]] += 1
        while abc['a'] and abc['b'] and abc['c']:
            res += n - r
            abc[s[l]] -= 1
            l += 1
        r += 1
    return res
"""
