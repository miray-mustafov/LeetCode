"""Constraints:
n[i] + n[j] + n[k] == 0
i != j, i != k, and j != k
Notice that the wrongsol set must not contain duplicate triplets.
3 <= n.length <= 3000
"""


def f(nums):
    res = []
    nums.sort()
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        l, r = i + 1, len(nums) - 1
        while l < r:
            sum3 = nums[i] + nums[l] + nums[r]
            if sum3 > 0:
                r -= 1
            elif sum3 < 0:
                l += 1
            else:
                res.append([nums[i], nums[l], nums[r]])
                l += 1
                while l < r and nums[l] == nums[l - 1]:
                    l += 1

    return res


def f2(nums):  # not working
    res = []
    nums.sort()
    for i in range(len(nums) - 2):
        a = nums[i]
        if i > 0 and a == nums[i - 1]:
            continue
        target = -a
        s = set()
        j = i + 1
        while j < len(nums):
            b = nums[j]
            c = target - b
            if c in s:
                res.append([a, b, c])
                while j + 1 < len(nums) and nums[j] == nums[j + 1]:
                    j += 1  # Skip duplicates for the second element
            s.add(b)
            j += 1

    return res


nums = [-1, 0, 1, 2, -1, -4]
nums2 = [-2, -2, -2, 0, 0, 2, 2]
nums3 = [-1, 1, -2, 0, 0, -1, 1]
print(f(nums))  # [[-1,-1,2],[-1,0,1]]
print(f(nums2))
print(f(nums3))
print()
print(f2(nums))  # [[-1,-1,2],[-1,0,1]]
print(f2(nums2))
print(f2(nums3))
