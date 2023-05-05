"""
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
"""


class Solution(object):

    def romanToInt(self, s):
        ROMANS = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,

            'II': 2,
            'IV': 4,
            'IX': 9,
            'XL': 40,
            'XC': 90,
            'CD': 400,
            'CM': 900,
        }
        result = 0
        s += ' '
        i = 0
        while i < len(s) - 1:
            pair = s[i] + s[i + 1]
            try:
                result += ROMANS[pair]
                i += 2
            except KeyError:
                result += ROMANS[s[i]]
                i += 1

        return result

    def better_solution(self, s):
        ROMANS = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        result = 0
        for a, b in zip(s, s[1:]):
            if ROMANS[a] < ROMANS[b]:
                result -= ROMANS[a]
            else:
                result += ROMANS[a]
        return result + ROMANS[s[-1]]

    def creative_solution(self, s):
        translations = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        number = 0
        s = s.replace("IV", "IIII").replace("IX", "VIIII")
        s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
        for char in s:
            number += translations[char]
        return number


three = 'III'
four = 'IV'
fourteen = 'XIV'
nineteen = 'XIX'
five8 = 'LVIII'
one994 = 'MCMXCIV'

attempt = Solution()
print("My first attempt beats 25%:")
print(
    attempt.romanToInt(three),
    attempt.romanToInt(four),
    attempt.romanToInt(fourteen),
    attempt.romanToInt(five8),
    attempt.romanToInt(one994),
)

print("Better algorithm beats 35%:")
print(attempt.better_solution(one994))

print('Creative algorithm beats 38%:')
print(attempt.creative_solution(one994))
