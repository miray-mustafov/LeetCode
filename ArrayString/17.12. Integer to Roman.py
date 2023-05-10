from collections import deque


def to_roman(num):
    ROMANS = {
        1: "I",
        5: "V",
        10: "X",
        50: "L",
        100: "C",
        500: "D",
        1000: "M",
    }

    roman = deque()
    divisor = 10
    while num > 0:
        n = num % divisor

        while n == 0:
            divisor *= 10
            n = num % divisor

        num -= n
        curr_str = ''
        if n in ROMANS:
            curr_str = ROMANS[n]
        else:
            unit = divisor // 10
            if n + unit in ROMANS:
                curr_str = ROMANS[unit] + ROMANS[unit + n]
            else:
                while n not in ROMANS:
                    n -= unit
                    curr_str += ROMANS[unit]
                curr_str = ROMANS[n] + curr_str

        roman.appendleft(curr_str)
        divisor *= 10

    return ''.join(roman)


print(to_roman(1994))
print(to_roman(58))
print(to_roman(10))
print(to_roman(20))
print(to_roman(30))
print(to_roman(1500))
# print(to_roman(1994) == 'MCMXCIV')
