def insaneSolution(nums, k):
    hmap = {}
    freq = [[] for _ in range(len(nums) + 1)]

    for n in nums:
        hmap[n] = 1 + hmap.get(n, 0)

    for n, count in hmap.items():
        freq[count].append(n)

    res = []
    for i in range(len(freq)-1, 0, -1):
        for n in freq[i]:
            res.append(n)
            if len(res) == k:
                return res
    return res

def topk(nums, k):  # O nlogn + k
    from collections import defaultdict
    hmap = defaultdict(int)
    for n in nums:  # O n
        hmap[n] += 1

    # sorting the dictionary by values descending O nlogn
    sorted_elmnts_desc = sorted(hmap.items(), key=lambda kvp: kvp[1], reverse=True)

    res = []
    for i in range(k):  # O k
        res.append(sorted_elmnts_desc[i][0])

    return res


nums = [1, 1, 1, 2, 2, 3]
k = 2
print(topk(nums, k))
print(insaneSolution(nums, k))
print()
nums = [1]
k = 1
print(topk(nums, k))
print(insaneSolution(nums, k))
