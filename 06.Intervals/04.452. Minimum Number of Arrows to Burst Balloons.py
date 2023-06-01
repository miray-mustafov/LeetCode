def findMinArrowShots(points):
    if len(points) == 1:
        return 1

    points.sort(key=lambda x: x[1])
    last_end, arrows = points[0][1], 0
    for start, end in points[1:]:
        if start > last_end:
            arrows += 1
            last_end = end

    return arrows + 1 if points[-1][0] <= last_end else arrows


points = [[10, 16], [2, 8], [1, 6], [7, 12]]
print(findMinArrowShots([[1,2],[3,4],[5,6],[7,8]]))
print(findMinArrowShots([[1,2],[2,3],[3,4],[4,5]]))
