# 231. Power of Two
def powerOfTwo(n):
    pow = 1
    while pow < n:
        pow <<= 1
    if pow == n:
        return True
    return False


print(powerOfTwo(1))
print(powerOfTwo(16))
print(powerOfTwo(17))
