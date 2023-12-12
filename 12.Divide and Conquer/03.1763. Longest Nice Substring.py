def longestNiceSubstring(s):
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


s = 'YazaAay'
s2 = 'YayaAaz'
s3 = "Bb"
s4 = "c"
print(longestNiceSubstring(s))
print(longestNiceSubstring(s2))
print(longestNiceSubstring(s3))
print(longestNiceSubstring(s4))
