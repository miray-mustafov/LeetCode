def f(pattern, s):  # O(m+n)
    s = s.split()
    if len(s) != len(pattern):
        return False
    d, sett = {}, set()
    for i in range(len(s)):
        if pattern[i] not in d:
            if s[i] in sett:
                return False
            else:
                d[pattern[i]] = s[i]
                sett.add(s[i])
        else:
            if s[i] not in sett:
                return False
            elif s[i] != d[pattern[i]]:
                return False
    return True


pattern = "abbac"
s = "dog cat cat dog fish"

pattern1 = "abba"
s1 = "dog cat cat fish"

pattern2 = "aaaa"
s2 = "dog cat cat dog"

print(f(pattern, s))
print(f(pattern1, s1))
print(f(pattern2, s2))
