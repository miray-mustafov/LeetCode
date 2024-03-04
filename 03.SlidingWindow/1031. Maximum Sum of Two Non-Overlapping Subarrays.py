def maxSumTwoNoOverlap(nums, firstLen, secondLen):
    n = len(nums)
    maxSumFirst = [0] * n
    maxSumSecond = [0] * n

    # Precompute maximum sum of subarrays of length firstLen
    currSum = sum(nums[:firstLen])
    maxSumFirst[firstLen - 1] = currSum
    for i in range(firstLen, n):
        currSum += nums[i] - nums[i - firstLen]
        maxSumFirst[i] = currSum

    # Precompute maximum sum of subarrays of length secondLen
    currSum = sum(nums[:secondLen])
    maxSumSecond[secondLen - 1] = currSum
    for i in range(secondLen, n):
        currSum += nums[i] - nums[i - secondLen]
        maxSumSecond[i] = currSum

    maxSum = 0
    # Calculate the maximum sum considering non-overlapping subarrays
    for i in range(n):
        if i >= firstLen - 1:
            maxSum = max(maxSum, maxSumFirst[i] + maxSumSecond[i - firstLen])
        if i >= secondLen - 1:
            maxSum = max(maxSum, maxSumFirst[i - secondLen] + maxSumSecond[i])

    return maxSum


def maxSumTwoNoOverlap2(nums, firstLen, secondLen):
    n = len(nums)
    maxSumFirst = [0] * n
    maxSumSecond = [0] * n

    # Precompute maximum sum of subarrays of length firstLen
    currSum = sum(nums[:firstLen])
    maxSumFirst[firstLen - 1] = currSum
    for i in range(firstLen, n):
        currSum += nums[i] - nums[i - firstLen]
        maxSumFirst[i] = max(currSum, maxSumFirst[i - 1])

    # Precompute maximum sum of subarrays of length secondLen
    currSum = sum(nums[:secondLen])
    maxSumSecond[secondLen - 1] = currSum
    for i in range(secondLen, n):
        currSum += nums[i] - nums[i - secondLen]
        maxSumSecond[i] = max(currSum, maxSumSecond[i - 1])

    maxSum = 0
    # Calculate the maximum sum considering non-overlapping subarrays
    for i in range(n):
        if i >= firstLen - 1:
            maxSum = max(maxSum, maxSumFirst[i] + maxSumSecond[i - firstLen + 1])
        if i >= secondLen - 1:
            maxSum = max(maxSum, maxSumFirst[i - secondLen + 1] + maxSumSecond[i])

    return maxSum


def maxSumTwoNoOverlap3(nums, firstLen, secondLen):  # sliding w
    def maxSum(L: int, M: int) -> int:
        sumL = sumM = 0
        for i in range(0, L + M):
            if i < L:
                sumL += nums[i]
            else:
                sumM += nums[i]
        maxL, ans = sumL, sumL + sumM
        for i in range(L + M, len(nums)):
            sumL += nums[i - M] - nums[i - L - M]
            maxL = max(maxL, sumL)
            sumM += nums[i] - nums[i - M]
            ans = max(ans, maxL + sumM)
        return ans

    return max(maxSum(firstLen, secondLen), maxSum(secondLen, firstLen))


def maxSumTwoNoOverlap4(nums, firstLen, secondLen):  # prefix sum
    def maxSum(L: int, M: int) -> int:
        maxL = ans = 0
        for i in range(L + M, len(prefixSum)):
            maxL = max(maxL, prefixSum[i - M] - prefixSum[i - L - M])
            ans = max(ans, maxL + prefixSum[i] - prefixSum[i - M])
        return ans

    prefixSum = [0] * (len(nums) + 1)
    for i, a in enumerate(nums):
        prefixSum[i + 1] = prefixSum[i] + a
    return max(maxSum(firstLen, secondLen), maxSum(secondLen, firstLen))


nums = [0, 6, 5, 2, 2, 5, 1, 9, 4]
nums2 = [1, 3, 3, 5, 4, 3, 1]
print('maxSumTwoNoOverlap')
print(maxSumTwoNoOverlap(nums2, 3, 2))  # output 18
print(maxSumTwoNoOverlap(nums, 1, 2))  # Output has to be 20 but its 15
print('maxSumTwoNoOverlap2')
print(maxSumTwoNoOverlap2(nums2, 3, 2))  # output 18
print(maxSumTwoNoOverlap2(nums, 1, 2))  # Output  20
print('maxSumTwoNoOverlap3')
print(maxSumTwoNoOverlap3(nums2, 3, 2))  # output 18
print(maxSumTwoNoOverlap3(nums, 1, 2))  # Output 20
print('maxSumTwoNoOverlap4')
print(maxSumTwoNoOverlap4(nums2, 3, 2))  # output 18
print(maxSumTwoNoOverlap4(nums, 1, 2))  # Output 20
