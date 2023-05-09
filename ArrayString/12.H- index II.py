def hIndex(citations):
    n = len(citations)
    for i in range(n):
        diff = n - i
        if citations[i] >= diff:
            return diff
    return 0


def hIndex_logn(citations):
    if not citations or citations[-1] == 0:
        return 0
    N = len(citations)
    l, r = 0, N - 1
    while l < r:
        m = (l + r) // 2
        if N - m > citations[m]:
            l = m + 1
        else:
            r = m
    return N - l


nums = [0, 1, 2, 6, 7, 9, 7, 12]
print(hIndex(nums))
print(hIndex_logn(nums))
