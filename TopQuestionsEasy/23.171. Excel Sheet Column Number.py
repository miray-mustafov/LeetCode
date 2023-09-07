def f(s):
    multiplier = 1
    columnNumber = 0
    for i in range(len(s) - 1, -1, -1):
        columnNumber += (ord(s[i]) - 64) * multiplier
        multiplier *= 26
    return columnNumber


print(f('BBC'))
