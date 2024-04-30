def f(points, k):
    import heapq
    minHeap = []
    for x, y in points:
        dist = (x ** 2) + (y ** 2)
        minHeap.append([dist, x, y])
    heapq.heapify(minHeap)

    res = []
    while k > 0:
        _, x, y = heapq.heappop(minHeap)
        res.append([x, y])
        k -= 1
    return res


points, k = [[1, 3], [-2, 2]], 1  # [[-2,2]]
print(f(points, k))
print()
points, k = [[3, 3], [5, -1], [-2, 4]], 2  # [[3,3],[-2,4]]
print(f(points, k))
