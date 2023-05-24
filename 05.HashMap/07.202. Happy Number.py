def isHappy(n):
    def sum_digit_squares(n):
        total = 0
        for d in str(n):
            total += int(d) ** 2
        return total

    hset = set()
    while n != 1:
        if n in hset:
            return False
        hset.add(n)
        n = sumdsq(n)
    return True


def sumdsq(n):
    total = 0
    while n:
        digit = n % 10
        total += digit ** 2
        n = n // 10
    return total

print(isHappy(19))
print(isHappy(2))
print(isHappy(34))
print(isHappy(33))
