def remindCombinationSum(c, target):
    def dfs(i, total):
        if total == target:
            res.append(sub.copy())
            return
        if i >= len(c) or total > target:
            return

        sub.append(c[i])
        dfs(i, total + c[i])
        sub.pop()
        dfs(i + 1, total)

    res, sub = [], []
    dfs(0, 0)
    return res


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
res1 = remindCombinationSum(candidates, target)
res2 = combinationSum(candidates, target)
print(res1)  # [[2,2,3],[7]]
print(res2)  # [[2,2,3],[7]]
print(res1 == res2)
