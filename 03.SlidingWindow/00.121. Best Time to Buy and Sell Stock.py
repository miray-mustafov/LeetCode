def max_profit_stock(prices):
    max_profit = 0
    l, r = 0, 1
    while r < len(prices):
        if prices[l] < prices[r]:
            profit = prices[r] - prices[l]
            max_profit = max(max_profit, profit)
        else:
            l = r
        r += 1

    return max_profit


prices = [7, 1, 5, 3, 6, 4]  # 5
prices2 = [10, 100, 7, 1, 5, 3, 6, 4]
prices3 = [5, 100, 6, 7, 4, 90, ]
print(max_profit_stock(prices))
print(max_profit_stock(prices3))
