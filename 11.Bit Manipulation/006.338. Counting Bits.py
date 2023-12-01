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


n = 5
# Output: [0,1,1,2,1,2]
print(countBits(n))
