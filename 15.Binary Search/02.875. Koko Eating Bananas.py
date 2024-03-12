import math


def binary_search_solution(piles, h):
    l, r = 1, max(piles)
    res = r
    while l <= r:
        k = l + ((r - l) // 2)

        cur_h = 0
        for p in piles:
            cur_h += math.ceil(p / k)

        if cur_h <= h:
            res = min(res, k)
            r = k - 1
        else:
            l = k + 1
    return res


def brute_force(piles, h):
    piles.sort()
    for bananas in range(1, piles[-1] + 1):
        cur_h = 0
        for p in piles:
            cur_h += math.ceil(p / bananas)
        if cur_h == h:
            return bananas


piles, h = [3, 6, 7, 11], 8  # 4
piles2, h2 = [30, 11, 23, 4, 20], 5  # 30
piles3, h3 = [30, 11, 23, 4, 20], 6  # 23
print(brute_force(piles, h))
print(brute_force(piles2, h2))
print(brute_force(piles3, h3))
print()
print(binary_search_solution(piles, h))
print(binary_search_solution(piles2, h2))
print(binary_search_solution(piles3, h3))
