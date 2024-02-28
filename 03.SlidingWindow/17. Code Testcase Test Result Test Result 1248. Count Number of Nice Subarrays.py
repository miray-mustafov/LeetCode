def poorattempt(nums, k):
    res = r = l = 0
    counter = 0
    while r < len(nums):
        if nums[r] % 2 == 1:
            counter += 1
        while counter >= k:
            if nums[l] % 2 == 1:
                counter -= 1
            res += len(nums) - r
            l += 1

        r += 1
    return res


def solution2(nums, k):
    def atMost(nums, k):
        res = i = 0
        for j in range(len(nums)):
            k -= nums[j] % 2
            while k < 0:
                k += nums[i] % 2
                i += 1
            res += j - i + 1
        return res

    return atMost(nums, k) - atMost(nums, k - 1)


nums2 = [2, 2, 1, 1, 2, 2, 2]
nums3 = [2, 2, 1, 1, 2, 1, 2]
k = 2
print(solution2(nums2, k))
print(solution2(nums3, k))
print(solution2([1, 1, 2, 1, 1], 3))  # 2
print(solution2([2, 2, 2, 1, 2, 2, 1, 2, 2, 2], 2))  # 16
