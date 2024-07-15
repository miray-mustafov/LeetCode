def romanToInt(s):
    d = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }
    if len(s) == 1:
        return d[s]

    res = 0
    i = 1
    while i < len(s):
        if d[s[i - 1]] < d[s[i]]:
            res += d[s[i]] - d[s[i - 1]]
            i += 1
        else:
            res += d[s[i - 1]]
        i += 1
    return res


s = "MCMXCIV"
print(romanToInt(s))
# 1994
