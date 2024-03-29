def f(fruits):
    l = 0
    baskets = {}
    res = 0
    for r in range(len(fruits)):
        if fruits[r] in baskets or (len(baskets) < 2 and fruits[r] not in baskets):
            baskets[fruits[r]] = baskets.get(fruits[r], 0) + 1
        elif fruits[r] not in baskets:
            res = max(res, sum(baskets.values()))
            while len(baskets) == 2:
                baskets[fruits[l]] -= 1
                if baskets[fruits[l]] == 0:
                    del baskets[fruits[l]]
                l += 1
            baskets[fruits[r]] = 1
    return max(res, sum(baskets.values()))


def neetcode(fruits):
    from collections import defaultdict
    baskets = defaultdict(int)
    l = total = res = 0
    for r in range(len(fruits)):
        baskets[fruits[r]] += 1
        total += 1
        while len(baskets) > 2:
            lf = fruits[l]
            baskets[lf] -= 1
            total -= 1
            if not baskets[lf]:
                baskets.pop(lf)
            l += 1
        res = max(res, total)
    return res


fruits = [1, 2, 3, 2, 2]  # 4
print(f(fruits))
print(neetcode(fruits))
fruits = [1, 2, 3, 2, 2]  # 4
