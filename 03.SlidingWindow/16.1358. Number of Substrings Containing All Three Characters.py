def numberOfSubstrings(s: str):
    def helper(sub):
        a, b, c = 'a', 'b', 'c'
        for el in sub:
            if el == a:
                a = False
            elif el == b:
                b = False
            elif el == c:
                c = False
        if not any((a, b, c)):
            return 1
        return 0

    count = 0
    for i in range(len(s) - 3):
        for j in range(i + 3, len(s)):
            count += helper(s[i:j])

    for i in range(len(s), 2, -1):
        for j in range(i - 3, -1, -1):
            count += helper(s[j:i])

    return count


s = "abcabc"
print(numberOfSubstrings(s))
s = "aaacb"
print(numberOfSubstrings(s))
