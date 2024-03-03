def numberOfSubstrings(s):
    abc = {'a': 0, 'b': 0, 'c': 0}
    l = res = 0
    for r in range(len(s)):
        abc[s[r]] += 1
        while abc['a'] and abc['b'] and abc['c']:
            abc[s[l]] -= 1
            res += len(s) - r
            l += 1
    return res


s = "abcabc"
print(numberOfSubstrings(s))
s = "aaacb"
print(numberOfSubstrings(s))
