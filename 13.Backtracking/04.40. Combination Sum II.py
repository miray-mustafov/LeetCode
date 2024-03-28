def combinationSum2(candidates, target):
    def dfs(i, total, sub):
        if total == target:
            res.append(sub.copy())
            return
        if i >= len(c) or total > target:
            return

        sub.append(c[i])
        dfs(i + 1, total + c[i], sub)

        sub.pop()
        while i + 1 < len(c) and c[i] == c[i + 1]:
            i += 1
        dfs(i + 1, total, sub)

    candidates.sort()
    res, c = [], candidates
    dfs(0, 0, [])
    return res


def sol(candidates, target):
    candidates.sort()
    res = []

    def backtrack(cur, i, target):
        if target == 0:
            res.append(cur.copy())
        if target <= 0:
            return
        prev = -1
        for i in range(i, len(candidates)):
            if candidates[i] == prev:
                continue
            cur.append(candidates[i])
            backtrack(cur, i + 1, target - candidates[i])
            cur.pop()
            prev = candidates[i]

    backtrack([], 0, target)
    return res


# candidates = [10, 1, 2, 7, 6, 1, 5]
candidates = [1, 2, 6, 1, 5]
target = 8
expected = [
    [1, 1, 6],
    [1, 2, 5],
    [1, 7],
    [2, 6]
]
print(combinationSum2(candidates.copy(), target))
print(sol(candidates.copy(), target))
