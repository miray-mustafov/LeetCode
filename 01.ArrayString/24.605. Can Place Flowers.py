def canPlaceFlowers(flowerbed, n):
    f = [0] + flowerbed + [0]
    for i in range(1, len(f) - 1):
        if f[i - 1] == f[i] == f[i + 1] == 0:
            f[i], n = 1, n - 1
    return True if n <= 0 else False


flowerbed = [1, 0, 0, 0, 1]
n = 1

flowerbed2 = [1, 0, 0, 0, 1]
n2 = 2
flowerbed3 = [1, 0, 0, 0, 1, 0, 0]
print(canPlaceFlowers(flowerbed3, n2))
