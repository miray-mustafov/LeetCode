def rotate_array(nums, k):
    """
    Rotates the given array to the right by k steps in place.
    """
    n = len(nums)
    k %= n
    nums[:] = nums[n - k:] + nums[:n - k]
    print(nums)


def rotate(nums, k):
    def reverse_subarray(arr, start, end):
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start, end = start + 1, end - 1

    n = len(nums)
    k = k % n
    reverse_subarray(nums, 0, n - 1)
    reverse_subarray(nums, 0, k - 1)
    reverse_subarray(nums, k, n - 1)
    print(nums)


nums = [1, 2, 3, 4, 5, 6, 7]
nums2 = [1, 2, 3]  # [3,1,2] [2,3,1] [1,2,3]
k = 3
rotate_array(nums.copy(), k)
rotate(nums.copy(), k)
# [5,6,7,1,2,3,4]
