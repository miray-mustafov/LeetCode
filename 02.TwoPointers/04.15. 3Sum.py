"""Constraints:
n[i] + n[j] + n[k] == 0
i != j, i != k, and j != k
Notice that the wrongsol set must not contain duplicate triplets.
3 <= n.length <= 3000
"""


def f(n):
    res = []
    n.sort()
    for i in range(len(n) - 2):
        if i > 0 and n[i] == n[i - 1]:
            continue

        l, r = i + 1, len(n) - 1
        while l < r:
            sum3 = n[i] + n[l] + n[r]
            if sum3 > 0:
                r -= 1
            elif sum3 < 0:
                l += 1
            else:
                res.append([n[i], n[l], n[r]])
                l += 1
                while l < r and n[l] == n[l - 1]:
                    l += 1

    return res


nums = [-1, 0, 1, 2, -1, -4]
nums2 = [-2, -2, -2, 0, 0, 2, 2]
print(f(nums))  # [[-1,-1,2],[-1,0,1]]
