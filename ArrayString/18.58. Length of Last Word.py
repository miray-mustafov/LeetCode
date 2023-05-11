def lenlastwor(s):
    s = s.rstrip()
    res = 0
    i = len(s) - 1
    while i > -1:
        if s[i] == ' ':
            return res
        res += 1
        i -= 1
    return res


s = "Hello       World   "
print(lenlastwor(s))
print(lenlastwor(' world '))
