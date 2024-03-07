def maximumLength(s):
    h = {}
    res = -1

    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            cur_sub = s[i:j]
            if len(set(cur_sub)) == 1:
                if cur_sub not in h:
                    h[cur_sub] = 0
                h[cur_sub] += 1
                if h[cur_sub] >= 3:
                    res = max(res, len(cur_sub))
    return res


s = "abcaba"  # 1
print(maximumLength(s))
print(maximumLength('aaaab'))
