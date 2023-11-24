def uniquePathsII(obstacleGrid):  # space O(m*n)
    m, n = len(obstacleGrid), len(obstacleGrid[0])
    for i in range(1, m):
        for j in range(1, n):
            if obstacleGrid[i][j] == 0:
                continue
            obstacleGrid[i][j] = obstacleGrid[i][j - 1] + obstacleGrid[i - 1][j]

    return obstacleGrid[m - 1][n - 1]


grid = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
grid2 = [[1, 0], [1, 1]]
print(uniquePathsII(grid))
print(uniquePathsII(grid2))
