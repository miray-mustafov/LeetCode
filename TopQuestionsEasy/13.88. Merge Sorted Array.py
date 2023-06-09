def merge(nums1, m, nums2, n):
    i, m, n = len(nums1) - 1, m - 1, n - 1

    while m > -1 and n > -1:
        if nums1[m] > nums2[n]:
            nums1[i] = nums1[m]
            m -= 1
        else:
            nums1[i] = nums2[n]
            n -= 1
        i -= 1
    while n > -1:
        nums1[i] = nums2[n]
        n -= 1
        i -= 1


nums1 = [3, 3, 4, 0, 0, 0, 0]
m = 3
nums2 = [1, 2, 5, 6]
n = 4
merge(nums1, m, nums2, n)
print(nums1)
