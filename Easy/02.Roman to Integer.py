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

    def romanToInt(self, s):
        result = 0
        s += ' '
        i = 0
        while i < len(s) - 1:
            pair = s[i] + s[i + 1]
            try:
                result += Solution.ROMANS[pair]
                i += 2
            except KeyError:
                result += Solution.ROMANS[s[i]]
                i += 1

        return print(result)

    def top_solution(self, s):
        pass


three = 'III'
four = 'IV'
fourteen = 'XIV'
nineteen = 'XIX'
five8 = 'LVIII'
one994 = 'MCMXCIV'

attempt = Solution()
print("My first attempt that beats 25%:")
result = attempt.romanToInt(three)
result = attempt.romanToInt(four)
result = attempt.romanToInt(fourteen)
result = attempt.romanToInt(five8)
result = attempt.romanToInt(one994)

print("Top algorithm:")
