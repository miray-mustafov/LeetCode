def lengthOfLIS(nums):  # On^2
    if not nums:
        return 0

    n = len(nums)
    dp = [1] * n  # Initialize an array to store the length of the longest increasing subsequence

    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return dp[n - 1]


def lengthOfLIS2(nums):  # O(n logn)
    dp = [float('inf')] * len(nums)

    for num in nums:
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if dp[mid] < num:
                low = mid + 1
            else:
                high = mid - 1

        dp[low] = num

    try:
        return dp.index(float('inf'))
    except:
        return len(dp)


# Test cases
nums1 = [10, 9, 2, 5, 3, 7, 101, 18]
nums2 = [0, 1, 0, 3, 2, 3]
nums3 = [7, 7, 7, 7, 7, 7, 7]

print(lengthOfLIS(nums1))  # Output: 4
print(lengthOfLIS(nums2))  # Output: 4
print(lengthOfLIS(nums3))  # Output: 1
print()
print(lengthOfLIS2(nums1))  # Output: 4
print(lengthOfLIS2(nums2))  # Output: 4
print(lengthOfLIS2(nums3))  # Output: 1
print(lengthOfLIS2([-2]))  # 1
