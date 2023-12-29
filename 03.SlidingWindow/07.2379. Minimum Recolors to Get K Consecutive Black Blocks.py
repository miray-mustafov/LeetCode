def minimumRecolors(blocks, k):
    cur_W_inwindow = 0
    for i in blocks[:k]:
        if i == 'W':
            cur_W_inwindow += 1

    min_W_inwindow = cur_W_inwindow
    for i in range(k, len(blocks)):
        if blocks[i] == 'W':
            cur_W_inwindow += 1
        if blocks[i - k] == 'W':
            cur_W_inwindow -= 1
        min_W_inwindow = min(min_W_inwindow, cur_W_inwindow)

    return min_W_inwindow


blocks, k = "WBBWWBBWBW", 7  # Output: 3
blocks2, k2 = "WBWBBBW", 2  # Output: 0

print(minimumRecolors(blocks, k))
print(minimumRecolors(blocks2, k2))
