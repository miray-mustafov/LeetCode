def f(intervals):
    if len(intervals) == 0:
        return True

    intervals.sort(key=lambda x: x[0])
    for i in range(len(intervals) - 1):
        s1, e1 = intervals[i]
        s2, e2 = intervals[i + 1]
        if s2 < e1:
            return False

    return True


intervals = [(1, 5), (6, 8), (3, 9)]
"""
sorted intervals:
---------
    -------------
          -----  
1 2 3 4 5 6 7 8 9
"""
print(f(intervals))  # False
print(f([(1, 5), (9, 13), (5, 8)]))  # True
