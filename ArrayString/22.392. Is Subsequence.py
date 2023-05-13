def f(s, t):
    i, j = 0, 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
        j += 1

    return True if i == len(s) else False


def f2(s, t):
    if s == '':
        return True
    if len(s) == 1:
        for el in t:
            if s == el: return True
        return False

    l, r, i, j = 0, len(t) - 1, 0, len(s) - 1
    while l < r and i <= j:
        if s[i] == t[l]:
            i += 1
        if s[j] == t[r]:
            j -= 1
        l, r = l + 1, r - 1
    if i > j:
        return True
    return False


s = 'c'
t = 'ahbdgc'
print(f2(s, t))
