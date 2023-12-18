# 1672. Richest Customer Wealth
def maximumWealth(accounts):
    res = 0
    for customer in accounts:
        res = max(res, sum(customer))
    return res


accounts = [[1, 2, 3], [3, 2, 1]]  # res = 6
accounts2 = [[1, 5],
             [7, 3],
             [3, 5], ]

print(maximumWealth(accounts))
