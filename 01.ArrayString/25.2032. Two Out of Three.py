def twoOutOfThree(nums1, nums2, nums3):
    set1, set2, set3 = set(nums1), set(nums2), set(nums3)

    result_set = set()

    result_set.update(set1.intersection(set2))
    result_set.update(set2.intersection(set3))
    result_set.update(set1.intersection(set3))

    return list(result_set)


nums1 = [1, 1, 3, 2]
nums2 = [2, 3]
nums3 = [3]
print(twoOutOfThree(nums1.copy(), nums2.copy(), nums3.copy()))
