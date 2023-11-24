def uniquePathsIIadjustedInput(obstacleGrid):
    m, n = len(obstacleGrid), len(obstacleGrid[0])
    for i in range(1, m):
        for j in range(1, n):
            if obstacleGrid[i][j] == 0:
                continue
            obstacleGrid[i][j] = obstacleGrid[i][j - 1] + obstacleGrid[i - 1][j]

    return obstacleGrid[m - 1][n - 1]


# grid = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
# grid2 = [[1, 0], [1, 1]]
# print(uniquePathsIIadjustedInput(grid))


def uniquePathsII(grid):
    m, n = len(grid), len(grid[0])
    dp = [0] * n
    dp[n - 1] = 1
    for r in reversed(range(m)):
        for c in reversed(range(n)):
            if grid[r][c]:
                dp[c] = 0
            elif c + 1 < n:
                dp[c] = dp[c] + dp[c + 1]
    return dp[0]


grid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
grid2 = [[0, 1], [0, 0]]
grid3 = [[0, 1], [1, 0]]
print(uniquePathsII(grid))
print(uniquePathsII(grid2))
print(uniquePathsII(grid3))
