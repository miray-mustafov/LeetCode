def numDecodingsDP(s):  # 0(n) space
    dp = [0] * (len(s) + 1)
    dp[len(s)] = 1
    for i in range(len(s) - 1, -1, -1):
        if s[i] == "0":
            dp[i] = 0
        else:
            dp[i] = dp[i + 1]
        if i + 1 < len(s) and (s[i] == '1' or
                               s[i] == '2' and s[i + 1] in '0123456'):
            dp[i] += dp[i + 2]

    return dp[0]


def numDecodingsDP2(s):  # 0(1) space
    current, nextt, after_next = 0, 1, 1
    for i in range(len(s) - 1, -1, -1):
        current = 0
        if s[i] != "0":
            current = nextt
        if i + 1 < len(s) and (s[i] == '1' or s[i] == '2' and s[i + 1] in '0123456'):
            current += after_next

        after_next = nextt
        nextt = current
    return current


print(numDecodingsDP('11106'))  # 2
print(numDecodingsDP2('11106'))  # 2
