def f(stones):
    import math
    stone_sum = sum(stones)
    target = math.ceil(stone_sum / 2)

    def dfs(i, total):
        if total >= target or i == len(stones):
            return abs(total - (stone_sum - total))
        if (i, total) in dp:
            return dp[(i, total)]

        disclude = dfs(i + 1, total)
        includes = dfs(i + 1, total + stones[i])
        dp[(i, total)] = min(disclude, includes)
        return dp[(i, total)]

    dp = {}
    return dfs(0, 0)


input1 = [2, 7, 4, 1, 8, 1]
input2 = [31, 26, 33, 21, 40]
print(f(input1))
print(f(input2))
