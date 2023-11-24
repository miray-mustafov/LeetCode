def uniquePaths(m, n):  # space O(m*n)
    dp = [[1] * n for _ in range(m)]

    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    return dp[m - 1][n - 1]


def uniquePaths2(m, n):  # space On
    dp = [1] * n  # Initialize a 1D array with all elements set to 1

    for i in range(1, m):
        for j in range(1, n):
            dp[j] += dp[j - 1]  # Update the 1D array using the previous row

    return dp[n - 1]


def uniquePaths3(m, n):  # O(1) Math factorial calculations may become impractical for large values of m and n
    import math
    total_moves = m + n - 2
    down_moves = m - 1
    return math.factorial(total_moves) // (math.factorial(down_moves) * math.factorial(total_moves - down_moves))


m = 3
n = 7
# Output: 28
print(uniquePaths(m, n))
print(uniquePaths2(m, n))
print(uniquePaths3(m, n))
