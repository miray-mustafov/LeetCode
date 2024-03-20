def sumIndicesWithKSetBits(nums, k):  # My low efficiency wrongsol
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


def tutorial(nums, k):
    sum = 0
    for index, x in enumerate(nums):
        # if index.bit_count() == k: # higher Python version needed for that function
        if bin(index).count('1') == k:
            sum += x
    return sum


def my(nums, k):
    sum = 0
    for index, x in enumerate(nums):
        count = 0
        for el in str(bin(index))[2:]:
            if el == '1':
                count += 1
        if count == k:
            sum += x
    return sum


nums = [5, 10, 1, 5, 2]
k = 1
print(sumIndicesWithKSetBits(nums, k))  # Output: 13 (10 + 1 + 3)
print(tutorial(nums, k))
print(my(nums, k))
