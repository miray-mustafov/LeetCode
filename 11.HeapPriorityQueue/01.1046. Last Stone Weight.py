import heapq


def f(stones):
    stones = [-s for s in stones]
    heapq.heapify(stones)

    while len(stones) > 1:
        first = heapq.heappop(stones)
        second = heapq.heappop(stones)
        heapq.heappush(stones, first - second)

    stones.append(0)
    return abs(stones[0])
