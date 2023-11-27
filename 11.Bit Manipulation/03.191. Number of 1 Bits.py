def sumIndicesWithKSetBits(nums, k):  # My low efficiency solution
    sum = 0
    for i in range(len(nums)):
        current_count_set_bits, current_i = 0, i
        for j in range(32):
            current_count_set_bits += current_i & 0b1
            current_i >>= 1
            if current_i == 0:
                break
        if current_count_set_bits == k:
            sum += nums[i]
    return sum


nums = [5, 10, 1, 5, 2]
k = 1
print(sumIndicesWithKSetBits(nums, k))  # Output: 13 (10 + 1 + 3)
