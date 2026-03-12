"""
Write a function to return the minimum number of intervals that must be removed
from a given array intervals, where intervals[i] consists of a starting point starti
and an ending point endi, to ensure that the remaining intervals do not overlap.
"""


def nonOverlappingIntervals(intervals):
    """correct"""
    if not intervals:
        return 0
    intervals.sort(key=lambda x: x[1])
    end = intervals[0][1]
    count = 1
    for i in range(1, len(intervals)):  # [[2, 3], [3, 4], [1, 5], [4, 6]] = 1
        # Non-overlapping interval found
        if intervals[i][0] >= end:
            end = intervals[i][1]
            count += 1
    return len(intervals) - count


def f(intervals):
    """
    THIS IS WRONG
    IT COUNTS THE CONSECUTIVE NON-OVERLAPPING INTERVALS instead
    (because I am pessimistic and think that the problem is harder by default)

    the idea is to remove as few meetings as possible so that we can attend more meetings
    the remaining intervals should not overlap
    i will turn around the logic and find the most non-overlapping intervals
    """
    if len(intervals) == 1:
        return 0
    elif len(intervals) == 2:
        return 0 if intervals[0][1] <= intervals[1][0] else 1

    intervals.sort(key=lambda x: x[1])
    intervals_length = len(intervals)
    # intervals.append([float('inf'), float('inf')])  # [[2, 3], [3, 4], [1, 5], [4, 6]] = 1
    res_max = float('-inf')
    cur_max = 1
    i = 0
    while i < len(intervals) - 2:
        s1, e1 = intervals[i]
        s2, e2 = intervals[i + 1]
        if s2 < e1:
            res_max = max(res_max, cur_max)
            if not e1 <= intervals[i + 2][0]:
                cur_max = 1
                i += 1
                continue
            i += 1

        i += 1
        cur_max += 1  # as long as next start is >= previous end, we increment

    res_max = max(res_max, cur_max)
    return intervals_length - res_max


"""
sorted intervals by end date:
---
---
---
1 2 3 4 5 6 7 8 9 10 11 12 13
"""
print(f([[2, 3], [3, 4], [1, 5], [4, 6]]))  # 1
print(f([[1, 3], [5, 8], [4, 10], [11, 13]]))  # 1
print(f([[1, 2], [1, 2], [1, 2]]))  # 2
print(f([[1, 3], [2, 5]]))  # 1
print(f([[1, 2], [2, 3]]))  # 0
