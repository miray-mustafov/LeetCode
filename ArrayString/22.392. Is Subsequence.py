def f(s, t):
    if s == '':
        return True
    i = 0
    for el in t:
        if i == len(s):
            return True
        if s[i] == el:
            i += 1

    if i == len(s):
        return True
    return False


s = 'abc'
t = 'ahbdgc'
print(f(s, t))
