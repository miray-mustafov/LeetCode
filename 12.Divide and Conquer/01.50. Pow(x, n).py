def myPow(x: float, n: int):
    def helper(x, n):
        if x == 0:
            return 0
        if n == 0:
            return 1
        res = helper(x, n // 2)
        res = res * res

        if n % 2:
            return x * res
        else:
            return res

    res = helper(x, abs(n))
    return 1 / res if n < 0 else res


print(myPow(2, 10))
print(myPow(2, -10))
