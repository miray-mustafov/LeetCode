def max_profit_stock(prices):
    profit = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            profit += (prices[i] - prices[i - 1])
    return profit

prices = [7, 1, 5, 3, 6, 8, 9, 4]
prices1 = [7, 1, 5, 3, 6, 4]  # 7
prices2 = [10, 100, 7, 1, 5, 3, 6, 4]
prices3 = [5, 100, 6, 7, 4, 90, ]
print(max_profit_stock(prices))
