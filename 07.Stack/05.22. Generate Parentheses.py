def f(n):#si
    res = []

    def backtrack(openn, closed, cur):
        if openn > n or closed > openn:
            return
        if openn == n and closed == n:
            res.append(cur)
            return

        if openn < n:
            backtrack(openn + 1, closed, cur + '(')
            a = 2
        if closed < openn:
            backtrack(openn, closed + 1, cur + ')')
            a = 2

    backtrack(0, 0, '')
    return res


n = 3
print(f(n))
n = 1
print(f(n))
