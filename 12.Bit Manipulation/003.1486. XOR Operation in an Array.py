def xorOperation(n, start):
    res = start
    for i in range(1, n):
        res = res ^ (start + 2 * i)
    return res


n = 5
start = 0
Output: 8

n2 = 4
start2 = 3
# Output: 8
print(xorOperation(n, start))
print(xorOperation(n2, start2))
