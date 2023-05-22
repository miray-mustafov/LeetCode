from collections import defaultdict


def isAnagram(s, t):
    if len(s) != len(t):
        return False
    d = defaultdict(int)
    for el in s:
        d[el] += 1
    for el in t:
        if el not in d:
            return False
        d[el] -= 1
        if d[el] == 0:
            del d[el]
    return True

s = "aan"
t = "naa"
print(isAnagram(s, t))
