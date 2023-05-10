def roman(s):
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
    for i in range(len(s) - 1):
        if ROMANS[s[i]] < ROMANS[s[i + 1]]:
            result -= ROMANS[s[i]]
        else:
            result += ROMANS[s[i]]
    return result + ROMANS[s[-1]]


print(roman("MCMXCIV"))
