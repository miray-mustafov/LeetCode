def remindSubsets(nums):
    def dfs(i):
        if i >= len(nums):
            res.append(sub[::])
            return

        sub.append(nums[i])
        dfs(i + 1)
        sub.pop()
        dfs(i + 1)

    res = []
    sub = []
    dfs(0)
    return res


def subsets(nums):
    res = []

    subset = []

    def dfs(i):
        if i >= len(nums):
            res.append(subset.copy())
            return

        subset.append(nums[i])
        dfs(i + 1)
        subset.pop()
        dfs(i + 1)

    dfs(0)
    return res


nums = [1, 2, 3]
res1 = subsets(nums)
res2 = remindSubsets(nums)
print(str(res1) + '\n' + str(res2))
print(res1 == res2)
