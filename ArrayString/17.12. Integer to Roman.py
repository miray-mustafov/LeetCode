from collections import deque


def to_roman(num):  # Super solo
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


def tutorial(num):
    symList = [["I", 1], ["IV", 4], ["V", 5], ["IX", 9], ["X", 10],
               ["XL", 40], ["L", 50], ["XC", 90], ["C", 100],
               ["CD", 400], ["D", 500], ["CM", 900], ["M", 1000]]
    res = ""
    for sym, val in reversed(symList):
        if num // val:
            count = num // val
            res += (sym * count)
            num = num % val
    return res


print(tutorial(1994))
print(tutorial(58))
print(to_roman(10))
print(to_roman(20))
print(to_roman(30))
print(to_roman(1500))
# print(to_roman(1994) == 'MCMXCIV')
