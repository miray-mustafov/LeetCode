def maxSumTwoNoOverlap(nums, firstLen, secondLen):  # sliding w On time O1 space
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


def maxSumTwoNoOverlap2(nums, firstLen, secondLen):  # prefix sum On time/space
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

print('maxSumTwoNoOverlap3')
print(maxSumTwoNoOverlap(nums2, 3, 2))  # output 18
print(maxSumTwoNoOverlap(nums, 1, 2))  # Output 20
print('maxSumTwoNoOverlap4')
print(maxSumTwoNoOverlap2(nums2, 3, 2))  # output 18
print(maxSumTwoNoOverlap2(nums, 1, 2))  # Output 20
