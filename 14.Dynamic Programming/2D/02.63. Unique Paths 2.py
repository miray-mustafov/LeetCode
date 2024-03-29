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


def uniquePathsIIreversed(grid):  # time Om+n space On
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


def uniquePathsII(grid):  # time Om+n space On
    m, n = len(grid), len(grid[0])
    dp = [0] * n
    dp[0] = 1
    for r in range(m):
        for c in range(n):
            if grid[r][c]:
                dp[c] = 0
            elif c - 1 > -1:
                dp[c] = dp[c] + dp[c - 1]
    return dp[n - 1]


# -----------------------------------------------------------------------
def uniquePathsIItableReversed(grid):
    m, n = len(grid), len(grid[0])
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    dp[m - 1][n - 1] = 1
    for r in reversed(range(m)):
        for c in reversed(range(n)):
            if grid[r][c]:
                dp[r][c] = 0
            else:
                dp[r][c] += dp[r + 1][c] + dp[r][c + 1]
    return dp[0][0]


def uniquePathsIItable(grid):
    m, n = len(grid), len(grid[0])
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    dp[1][1] = 1
    for r in range(1, m + 1):
        for c in range(1, n + 1):
            if grid[r - 1][c - 1]:
                dp[r][c] = 0
            else:
                dp[r][c] += dp[r - 1][c] + dp[r][c - 1]
    return dp[m][n]


# grid4 = [[0, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 0]]  # output: 4
grid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
grid2 = [[0, 1], [0, 0]]
grid3 = [[0, 1], [1, 0]]
print(uniquePathsIItable(grid))
print(uniquePathsIItable(grid2))
print(uniquePathsIItable(grid3))
print()
print(uniquePathsII(grid))
print(uniquePathsII(grid2))
print(uniquePathsII(grid3))
