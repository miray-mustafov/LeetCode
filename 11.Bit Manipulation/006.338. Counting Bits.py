def countBits(n):
    def helper(n):
        current_num_bits = 0
        while n:
            n &= (n - 1)
            current_num_bits += 1
        return current_num_bits

    arr = []
    for i in range(n + 1):
        arr.append(helper(i))
    return arr


def countBits2(n):
    dp = [0] * (n + 1)
    offset = 1
    for i in range(1, len(dp)):
        if offset * 2 == i:
            offset = i
        dp[i] = 1 + dp[i - offset]
    return dp


n = 10
# Output: [0,1,1,2,1,2]
print(countBits(n))
print(countBits2(n))
