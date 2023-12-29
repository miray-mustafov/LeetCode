# 2379. Minimum Recolors to Get K Consecutive Black Blocks
def minimumRecolors(blocks, k):
    from collections import deque
    min_W_inwindow = float('inf')
    cur_W_inwindow = 0
    queue = deque()
    for color in blocks[:k]:
        if color == 'W':
            cur_W_inwindow += 1
        queue.append(color)

    min_W_inwindow = min(min_W_inwindow, cur_W_inwindow)
    for color in blocks[k:]:
        if color == 'W':
            cur_W_inwindow += 1
        if queue.popleft() == 'W':
            cur_W_inwindow -= 1
        queue.append(color)
        min_W_inwindow = min(min_W_inwindow, cur_W_inwindow)
    return min_W_inwindow


blocks, k = "WBBWWBBWBW", 7  # Output: 3
blocks2, k2 = "WBWBBBW", 2  # Output: 0

print(minimumRecolors(blocks, k))
print(minimumRecolors(blocks2, k2))
