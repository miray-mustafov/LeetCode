# think out of the box task
def min_operations(nums, x):
    target = sum(nums) - x
    if target == 0:
        return len(nums)

    n = len(nums)
    current_sum = 0
    max_length = -1
    left = 0

    for right in range(n):
        current_sum += nums[right]

        while current_sum > target and left <= right:
            current_sum -= nums[left]
            left += 1

        if current_sum == target:
            max_length = max(max_length, right - left + 1)

    if max_length == -1:
        return -1

    return n - max_length


# Example usage:
print(min_operations([1, 1, 4, 2, 3], 5))  # Output: 2
print(min_operations([5, 6, 7, 8, 9], 4))  # Output: -1
print(min_operations([3, 2, 20, 1, 1, 3], 10))  # Output: 5
