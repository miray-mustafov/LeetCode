def combinationSum(c, target):
    res = []
    subset = []

    def dfs(i, cur_sum):
        if cur_sum == target:
            res.append(subset.copy())
            return
        if i >= len(c) or cur_sum > target:
            return
        subset.append(c[i])
        dfs(i, cur_sum + c[i])
        subset.pop()
        dfs(i + 1, cur_sum)

    dfs(0, 0)
    return res


candidates = [2, 3, 6, 7]
target = 7
print(combinationSum(candidates, target))  # [[2,2,3],[7]]
