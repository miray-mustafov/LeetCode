def longestNiceSubstring(s):  # On^3
    N, res = len(s), ''

    def is_nice(start, end):
        letters = set(s[start:end])
        for l in letters:
            if (l.lower() in letters) != (l.upper() in letters):
                return False
        return True

    for start in range(N - 1):
        for end in range(start + 2, N + 1):
            if is_nice(start, end) and end - start > len(res):
                res = s[start:end]
    return res


def longestNiceSubstring2(s):  # Onlogn
    if len(s) < 2:
        return ""

    def is_nice(sub):
        return all(ch.swapcase() in sub for ch in sub)

    mid = len(s) // 2

    left_substring = longestNiceSubstring(s[:mid])
    right_substring = longestNiceSubstring(s[mid:])

    if is_nice(s):
        return s

    return max(left_substring, right_substring, key=len)


s = 'YazaAay'
s2 = 'YayaAaz'
s3 = "Bb"
s4 = "c"
print(longestNiceSubstring(s))
print(longestNiceSubstring(s2))
print(longestNiceSubstring(s3))
print(longestNiceSubstring(s4))
print()
print(longestNiceSubstring2(s))
print(longestNiceSubstring2(s2))
print(longestNiceSubstring2(s3))
print(longestNiceSubstring2(s4))
