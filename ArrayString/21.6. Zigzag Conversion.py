# My solution faster
def convert(s, numRows):
    if numRows == 1:
        return s
    output = ''
    index, n, pattern = 0, len(s), (numRows - 1) * 2
    while index < n:
        output += s[index]
        index += pattern

    for i in range(1, numRows - 1):
        index = i
        index2 = pattern - i
        while True:
            if index2 >= n:
                if index >= n:
                    break
                output += s[index]
                break
            output += s[index] + s[index2]
            index += pattern
            index2 += pattern

    index = numRows - 1
    while index < n:
        output += s[index]
        index += pattern

    return output


def tutorial(s, numRows):
    if numRows == 1: return s

    res = ''
    increment = 2 * (numRows - 1)
    for r in range(numRows):
        for i in range(r, len(s), increment):
            res += s[i]
            if 0 < r < numRows - 1 and i + increment - 2 * r < len(s):
                res += s[i + increment - 2 * r]
    return res


s = 'PAYPALISHIRING'
n = 3
print(tutorial(s, 4))
print(tutorial(s, 3) == 'PAHNAPLSIIGYIR')
print(tutorial(s, 4) == 'PINALSIGYAHRPI')
