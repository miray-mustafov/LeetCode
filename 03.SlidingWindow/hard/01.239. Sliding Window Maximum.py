import collections


def maxSlidingWindow(nums, k):
    res = []
    for i in range(len(nums) - (k - 1)):
        cur_max = nums[i]
        for j in range(i, i + k):
            cur_max = max(nums[j], cur_max)
        res.append(cur_max)
    return res

#
# def wrongsol(nums, k):
#     output = []
#     q = collections.deque()
#     data = r = 0
#     while r < len(nums):
#         while q and nums[q[-1]] < nums[r]:
#             q.pop()
#         q.append(r)
#         if data < q[0]:
#             q.popleft()
#         if (r + 1) >= k:
#             output.append(nums[q[0]])
#             data += 1
#         r += 1
#
#     return output


nums = [3, 1, -1, -3, -4, 5, 3, 6, 7]
k = 3
nums2 = [1, 2, 0, 1, 9, 4, 2, 1, 4, 6, 7, 2]
k2 = 5
nums3 = [7, 6, 5, 4, 3, 2, 1, 0]  # Output: [3,3,5,5,6,7]

# print(wrongsol(nums, k))
# print(wrongsol(nums3, k))
