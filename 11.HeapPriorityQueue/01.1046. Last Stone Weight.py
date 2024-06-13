def lastStoneWeight(stones):  # O (n logn)
    import heapq as h
    stones = [-n for n in stones]  # On
    h.heapify(stones)  # On

    while len(stones) > 1:  # On
        x = h.heappop(stones)  # Ologn
        y = h.heappop(stones)  # Ologn
        res_stone = - abs(x - y)  # O1
        if res_stone != 0:  # O1
            h.heappush(stones, res_stone)  # Ologn
    stones.append(0)
    return -stones[0]


stones = [2, 7, 4, 1, 8, 1]
print(lastStoneWeight(stones))

# import heapq
#
#
# def f(stones):
#     stones = [-s for s in stones]
#     heapq.heapify(stones)
#
#     while len(stones) > 1:
#         first = heapq.heappop(stones)
#         second = heapq.heappop(stones)
#         heapq.heappush(stones, first - second)
#
#     stones.append(0)
#     return abs(stones[0])
