# 2147. Number of Ways to Divide a Long Corridor
def numberOfWays(corridor):
    def dfs(i, seats):
        if i == len(corridor):
            return 1 if seats == 2 else 0

        res = 0
        if seats == 2:
            if corridor[i] == 'S':
                res = dfs(i + 1, 1)
            else:
                res = dfs(i + 1, 0) + dfs(i + 1, 2)
        else:
            if corridor[i] == 'S':
                res = dfs(i + 1, seats + 1)
            else:
                res = dfs(i + 1, seats)

        return res

    return dfs(0, 0)


corridor = "SSPPSPSPSS"  # 3
print(numberOfWays(corridor))
