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


s = 'PAYPALISHIRING'
n = 3
print(convert(s, 4))
print(convert(s, 3) == 'PAHNAPLSIIGYIR')
print(convert(s, 4) == 'PINALSIGYAHRPI')
