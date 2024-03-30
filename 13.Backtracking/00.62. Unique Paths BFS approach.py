def uniquePaths(m, n):
    grid = [[0] * n for _ in range(m)]
    grid[-1][-1] = 1
    res = [0]

    def dfs(r, c):
        if r >= m or c >= n:
            return
        if grid[r][c] == grid[-1][-1]:
            res[0] += 1
            return
        dfs(r + 1, c)
        dfs(r, c + 1)

    dfs(0, 0)
    return res[0]


print(uniquePaths(3, 7))  # 28
print(uniquePaths(3, 2))  # 3
