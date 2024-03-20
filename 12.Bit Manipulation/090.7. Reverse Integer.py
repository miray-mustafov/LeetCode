import sys


def reverse(x):
    import math, sys
    MAX = sys.maxsize
    MIN = -MAX - 1
    res = 0

    while x:
        last_digit = int(math.fmod(x, 10))
        x = int(x / 10)
        if res > MAX // 10 or res == MAX // 10 and last_digit > MAX % 10:
            return 0
        if res < int(MIN / 10) or res == int(MIN / 10) and last_digit < math.fmod(MIN, 10):
            return 0
        res = (res * 10) + last_digit

    return res


x = 123
x2 = -123
x3 = 120
print(reverse(x))  # Output: 321
print(reverse(x2))  # Output: -321
print(reverse(x3))  # Output: 21
print(reverse(7463847412))
print(reverse(-8463847412))
print(reverse(8463847412))  # 0
print(reverse(-9463847412))  # 0
print(reverse(1534236469))  # 0
