# 1876. Substrings of Size Three with Distinct Characters
def countGoodSubstrings(s):
    res = 0
    for a, b, c in zip(s, s[1:], s[2:]):
        if a != b and b != c and c != a:
            res += 1
    return res


s = "xyzzaz"  # 1
s2 = "aabdbcabc"  # 4
print(countGoodSubstrings(s))
print(countGoodSubstrings(s2))
