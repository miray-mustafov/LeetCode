def reverseBits(n):
    ans = 0
    for i in range(1, 32 + 1):
        ans = ans << 1
        ans = ans | (n & 1)
        n = n >> 1
    return ans


n1 = 0b00000010100101000001111010011100  # 43261596
n2 = 0b11111111111111111111111111111101  # 4294967293
print(reverseBits(43261596))
print(reverseBits(n1))
print()
print(reverseBits(n2))
