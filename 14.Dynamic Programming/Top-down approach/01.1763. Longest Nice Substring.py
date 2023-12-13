def longestNiceSubstring2(s):  # On^3
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


def longestNiceSubstring(s):  # possible optimization with memoization but won't decrease fundamentally the time compl
    def dfs(string):
        if len(string) < 2:
            return ''

        hashset = set(string)
        for i, s in enumerate(string):
            if string[i].swapcase() not in hashset:
                left = dfs(string[:i])
                right = dfs(string[i + 1:])
                return left if len(left) >= len(right) else right

        return string

    return dfs(s)


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
