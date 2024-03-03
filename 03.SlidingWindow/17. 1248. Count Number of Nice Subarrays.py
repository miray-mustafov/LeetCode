# goodone
def solution2(nums, k):
    def atMost(nums, k):
        res = l = 0
        for r in range(len(nums)):
            k -= nums[r] % 2
            while k < 0:
                k += nums[l] % 2
                l += 1
            res += r - l + 1
        return res

    return atMost(nums, k) - atMost(nums, k - 1)


nums2 = [2, 1, 1, 2]
nums3 = [2, 2, 1, 1, 2, 1, 2]
k = 2
print(solution2(nums2, k))
print(solution2(nums3, k))
print(solution2([1, 1, 2, 1, 1], 3))  # 2
print(solution2([2, 2, 2, 1, 2, 2, 1, 2, 2, 2], 2))  # 16
