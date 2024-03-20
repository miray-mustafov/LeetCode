def minimumOneBitOperations(n):
    if n == 0:
        return 0
    k = 0
    while 2 ** k <= n:
        k += 1
    k -= 1
    return 2 ** (k + 1) - 1 - minimumOneBitOperations(2 ** k ^ n)


print(minimumOneBitOperations(3))  # 2
print(minimumOneBitOperations(4))  # 7
print(minimumOneBitOperations(6))  # 4
print(minimumOneBitOperations(8))  # 15
print(minimumOneBitOperations(10))  # 12
