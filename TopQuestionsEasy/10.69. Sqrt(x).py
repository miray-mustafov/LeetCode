def mySqrt(x):
    l, r = 0, x
    res = 0
    while l <= r:
        m = l + ((r-l) // 2)
        if m * m > x:
            r = m - 1
        elif m * m < x:
            l = m + 1
            res = m
        else:
            return m
    return res


print(mySqrt(1))
print(mySqrt(2))
print(mySqrt(4))
print(mySqrt(8))
print(mySqrt(169))
