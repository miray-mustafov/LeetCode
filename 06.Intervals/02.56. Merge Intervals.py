"""Same performance both mine and the tutorials solution"""


def tutorial(intervals):
    intervals.sort(key=lambda x: x[0])
    res = [intervals[0]]
    for start, end in intervals[1:]:
        lastEnd = res[-1][1]
        if start <= lastEnd:
            res[-1][1] = max(lastEnd, end)
        else:
            res.append([start, end])
    return res


def f(intervals):
    if len(intervals) == 1:
        return intervals

    intervals.sort(key=lambda x: x[0])
    res, start, end = [], intervals[0][0], intervals[0][1]

    for i in range(1, len(intervals)):
        if end < intervals[i][0]:
            res.append([start, end])
            start = intervals[i][0]
        if end < intervals[i][1]:
            end = intervals[i][1]

    res.append([start, end])
    return res


intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
intervals2 = [[1, 3], [2, 6], [8, 10], [10, 18]]
print(tutorial(intervals))  # [[1,6],[8,10],[15,18]]
print(f(intervals2))
print(f([[1, 4], [0, 1], ]))
print(f([[1, 4], [0, 1], [5, 6]]))
print(f([[1, 4], [0, 0]]))
print(tutorial([[1, 4], [2, 3]]))
