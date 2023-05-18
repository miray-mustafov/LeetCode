def f(s):
    set_str = set()
    res, l = 0, 0
    for r in range(len(s)):
        if s[r] not in set_str:
            set_str.add(s[r])
        else:
            res = max(res, r - l)
            while s[l] != s[r]:
                set_str.remove(s[l])
                l += 1
            l += 1
    return max(res, len(set_str))


s = "aehbcboaomclp"
print(f(s))
print(f("abcabcbb"))
print(f("bbbbb"))
print(f("pwwkew"))
