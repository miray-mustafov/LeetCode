# Optimization: Finds the FEWEST number of coins to return the change
def coinChange(coins, amount):
    import sys
    dp = [0] * (amount + 1)

    for money in range(1, amount + 1):
        current_min = sys.maxsize
        for coin in coins:
            if money - coin >= 0:
                current_min = min(dp[money - coin], current_min)
        dp[money] = current_min + 1
    return dp[amount] if dp[amount] != sys.maxsize + 1 else -1


# Combinatoric: Finds the total ways to return the change
def coinChangeWays(coins, amount):
    dp = [0] * (amount + 1)
    dp[0] = 1
    for money in range(1, amount + 1):
        for coin in coins:
            if money - coin >= 0:
                dp[money] += dp[money - coin]
    return dp[amount]


coins = [1, 2, 5]
amount = 11
print(coinChange([2], 3))
# Output: 3
