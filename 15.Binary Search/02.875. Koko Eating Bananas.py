import math


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
