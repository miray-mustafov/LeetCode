# 2706. Buy Two Chocolates
def buyChoco(prices, money):  # the problem breaks down to finding the two minimums
    if money == 1:
        return money
    min1, min2 = prices[0], prices[1]
    for i in range(2, len(prices)):
        if prices[i] < money and (prices[i] < min1 or prices[i] < min2):
            if min1 > min2:
                min1 = prices[i]
            else:
                min2 = prices[i]

    return money - (min1 + min2) if money - (min1 + min2) >= 0 else money


def buyChoco2(prices, money):  # the more conscise solution
    min1 = min2 = float('inf')
    for p in prices:
        if p < min1:
            min2, min1 = min1, p
        elif p < min2:
            min2 = p
    return money - (min1 + min2) if money - (min1 + min2) >= 0 else money


money = 3
prices = [3, 2, 2, 1]
prices2 = [3, 2, 3]
print(buyChoco(prices, money))
print(buyChoco(prices2, money))
