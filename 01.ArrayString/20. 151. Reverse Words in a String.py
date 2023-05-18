def reverseWords(s):
    res = []
    s = s.strip().split()
    for i in range(len(s) - 1, -1, -1):
        if s[i] != ' ':
            res.append(s[i])
    return ' '.join(res)


s = "  the   sky  is blue  "
print(reverseWords(s))  # "blue is sky the"
