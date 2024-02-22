def numberOfSubstrings(s: str):
    n, l, r = len(s), 0, 0
    abc = {'a': 0, 'b': 0, 'c': 0}
    res = 0
    while r < n:
        abc[s[r]] += 1
        while abc['a'] and abc['b'] and abc['c']:
            res += n - r
            abc[s[l]] -= 1
            l += 1
        r += 1
    return res


s = "abccbac"
print(numberOfSubstrings(s))
s = "aaacb"
print(numberOfSubstrings(s))
