# 231. Power of Two
def powerOfFour(n):
    pow = 1
    while pow < n:
        pow <<= 2
    if pow == n:
        return True
    return False


print(powerOfFour(1))
print(powerOfFour(16))
print(powerOfFour(17))
print(powerOfFour(64))
print(powerOfFour(256))
