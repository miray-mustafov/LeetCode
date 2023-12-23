def mergeTriplets(triplets, target):
    good_indices = set()
    for t in triplets:
        if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
            continue
        for i, v in enumerate(t):
            if v == target[i]:
                good_indices.add(i)
    return 3 == len(good_indices)


triplets = [[2, 5, 3], [2, 3, 4], [1, 2, 5], [5, 2, 3]]
target = [5, 5, 5]
triplets2 = [[2, 5, 3], [1, 8, 4], [1, 7, 5]]
target2 = [2, 7, 5]
triplets3 = [[3, 4, 5], [4, 5, 6]]
target3 = [3, 2, 5]
print(mergeTriplets(triplets, target))
print(mergeTriplets(triplets2, target2))
print(mergeTriplets(triplets3, target3))  # false
