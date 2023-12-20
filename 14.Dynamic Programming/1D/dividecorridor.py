# 2147. Number of Ways to Divide a Long Corridor
def numberOfWays(corridor):
    memo = [[-1] * 3 for _ in range(len(corridor))]  # 1.memoization declaration
    modulo = 10 ** 9 + 7

    def bfa(i, s):
        if i == len(corridor):
            return 1 if s == 2 else 0
        if memo[i][s] != -1:  # 2.memoization suspend repeated work
            return memo[i][s]

        res = 0
        if s == 2:
            if corridor[i] == 'S':
                res = bfa(i + 1, 1)
            else:
                res = (bfa(i + 1, 0) + bfa(i + 1, 2)) % modulo
        else:
            if corridor[i] == 'S':
                res = bfa(i + 1, s + 1)
            else:
                res = bfa(i + 1, s)

        memo[i][s] = res  # 3.fill memoization dict
        return res

    return bfa(0, 0)


corridor = "SSPPSPS"  # 3
corridor2 = "PPPPPSPPSPPSPPPSPPPPSPPPPSPPPPSPPSPPPSPSPPPSPSPPPSPSPPPSPSPPPPSPPPPSPPPSPPSPPPPSPSPPPPSPSPPPPSPSPPPSPPSPPPPSPSPSS"

print(numberOfWays(corridor))
print(numberOfWays(corridor2))  # 919999993 (after theh %10^9 + 7)
