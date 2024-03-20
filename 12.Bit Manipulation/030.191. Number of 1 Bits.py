def hammingWeight(n):
    res = 0
    for _ in range(32):
        res += n & 1
        n >>= 1
    return res


def moreEfficient(n):
    res = 0
    while n:
        n &= (n - 1)
        res += 1
    return res


n = 0b0000000000000000000000000001011
print(hammingWeight(n))
print(moreEfficient(n))
