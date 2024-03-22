def permute(nums):
    res = []
    if len(nums) == 1:
        return [nums[:]]

    for i in range(len(nums)):
        n = nums.pop(0)
        perms = permute(nums)

        for perm in perms:
            perm.append(n)
        res.extend(perms)
        nums.append(n)

    return res


def permute2(nums):
    def backtrack(current):
        if len(current) == len(nums):
            result.append(current[:])
            return
        for num in nums:
            if num not in current:
                current.append(num)
                backtrack(current)
                current.pop()
            a = 3
        a = 5

    result = []
    backtrack([])
    return result


nums = [1, 2, 3]
actual = permute(nums.copy())
actual.sort()
expected = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
print(actual == expected)
print()
actual2 = permute2(nums.copy())
actual2.sort()
print(actual2 == expected)
