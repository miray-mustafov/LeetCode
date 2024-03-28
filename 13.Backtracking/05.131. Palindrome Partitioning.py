def partition(s):
    def isPali(s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1
        return True

    res, part = [], []

    def dfs(i):
        if i >= len(s):
            res.append(part.copy())
            return
        for j in range(i, len(s)):
            if isPali(s, i, j):
                part.append(s[i:j + 1])
                dfs(j + 1)
                part.pop()
            a=4

    dfs(0)
    return res


string = 'aab'
print(partition(string))
