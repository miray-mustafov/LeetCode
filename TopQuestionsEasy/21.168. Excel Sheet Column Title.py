def f(columnNumber):
    res = ''
    while columnNumber > 0:
        offset = (columnNumber - 1) % 26
        res += chr(ord("A") + offset)
        columnNumber = (columnNumber - 1) // 26
    n = 701
    return res[::-1]


print(f(701))
