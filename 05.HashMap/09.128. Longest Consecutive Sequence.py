def f(nums):
    hset = set(nums)
    longest = 0
    for n in hset:
        if n - 1 not in hset:
            length = 0
            while n + length in hset:
                length += 1
            longest = max(longest, length)

    return longest


nums = [100, 4, 200, 1, 3, 2]
nums2 = [0, 3, 7, 10, 2, 5, 8, 4, 6, 0, 1]
print(f([9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6]))
