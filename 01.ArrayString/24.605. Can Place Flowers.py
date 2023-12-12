def canPlaceFlowers(flowerbed, n):  # On On
    f = [0] + flowerbed + [0]
    for i in range(1, len(f) - 1):
        if f[i - 1] == f[i] == f[i + 1] == 0:
            f[i], n = 1, n - 1
    return n <= 0


def canPlaceFlowers2(flowerbed, n):
    empty = 0 if flowerbed[0] else 1
    for f in flowerbed:
        if f:
            n -= int((empty - 1) / 2)  # in division round tow zero
            empty = 0
        else:
            empty += 1
    n -= empty // 2
    return n <= 0


flowerbed = [1, 0, 0, 0, 1]
n = 1

flowerbed2 = [1, 0, 0, 0, 1]
n2 = 2
flowerbed3 = [1, 0, 0, 0, 1, 0, 0]
flowerbed4 = [1, 0, 0, 1, 0, 0]
print(canPlaceFlowers2(flowerbed3, n2))
