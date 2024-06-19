import heapq


def f(tasks, n):
    from collections import defaultdict, deque
    # count the occurrences of each letter
    count_dict = defaultdict(int)
    for key in tasks:
        count_dict[key] += 1

    max_heap = [-c for c in count_dict.values()]
    heapq.heapify(max_heap)

    time, q = 0, deque()
    while max_heap or q:
        time += 1
        if max_heap:
            cnt = 1 + heapq.heappop(max_heap)
            if cnt:
                q.append([cnt, time + n])
        if q and q[0][1] == time:
            heapq.heappush(max_heap, q.popleft()[0])
    return time


tasks, n = ["A", "A", "A", "B", "B", "C"], 5  # 10
print(f(tasks, n))
