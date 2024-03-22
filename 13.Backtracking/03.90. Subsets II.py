def subsetsWithDup(nums):
    res = []
    nums.sort()  # 1, 2, 2, 3

    def backtrack(i, sub):
        if i >= len(nums):
            res.append(sub[:])
            return
        sub.append(nums[i])
        backtrack(i + 1, sub)
        sub.pop()
        while i + 1 < len(nums) and nums[i + 1] == nums[i]:
            i += 1
        backtrack(i + 1, sub)

    backtrack(0, [])
    return res


nums = [1, 2, 2]
expected = [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]
actual = subsetsWithDup(nums)
actual.sort()
print(actual)
print(expected)
print(actual == expected)
