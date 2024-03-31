# just for exercise, it exceeds time limit
def uniquePaths(m, n):  # store the actual path too
    grid = [[0] * n for _ in range(m)]
    grid[-1][-1] = 1
    count, paths, path = [0], [], []

    def dfs(r, c):
        if r >= m or c >= n:
            return
        if grid[r][c] == grid[-1][-1]:
            count[0] += 1
            paths.append(path.copy())
            return
        path.append((r, c))
        dfs(r + 1, c)
        path.pop()

        path.append((r, c))
        dfs(r, c + 1)
        path.pop()

    dfs(0, 0)
    return count[0], paths


count, paths = uniquePaths(3, 2)
print(count, *paths, sep='\n')  # 3
print()
count, paths = uniquePaths(3, 7)
print(count, *paths, sep='\n')  # 28
