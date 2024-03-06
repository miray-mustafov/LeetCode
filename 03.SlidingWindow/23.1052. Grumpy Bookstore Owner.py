def f(customers, grumpy, m):
    initially_happy_customers = 0
    for i, ccount in enumerate(customers):
        initially_happy_customers += 0 if grumpy[i] else ccount

    # cur_max = cur window potential bonus customers
    cur_max = sum(el for c, el in enumerate(customers[:m]) if grumpy[c])
    res_max = cur_max
    for i in range(m, len(customers)):
        cur_max -= customers[i - m] if grumpy[i - m] else 0
        cur_max += customers[i] if grumpy[i] else 0
        res_max = max(res_max, cur_max)
    return initially_happy_customers + max(res_max, cur_max)


customers = [1, 0, 1, 2, 1, 1, 7, 5]
grumpy = [0, 1, 0, 1, 0, 1, 0, 1]
minutes = 3
print(f(customers, grumpy, minutes))  # 16
print(f([1], [1], 1))
print(f([1], [0], 1))
print(f([0], [0], 1))
print(f([0], [0], 0))
