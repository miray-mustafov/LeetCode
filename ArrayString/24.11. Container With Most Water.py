def f(h):
    # Brute force On^2
    res = 0
    for l in range(len(h)):
        for r in range(l + 1, len(h)):
            area = (r - l) * min(h[l], h[r])
            res = max(res, area)
    return res


def tutorial(h):  # On solution with some Greediness
    l, r = 0, len(h) - 1
    res = 0
    while l < r:
        res = max(res, (r - l) * min(h[l], h[r]))
        if h[l] < h[r]:
            l += 1
        elif h[r] < h[l]:
            r -= 1
        else:
            l, r = l + 1, r - 1
    return res


height = [1, 8, 6, 2, 5, 4, 8, 3, 7]  # n = len(height) >= 2
height2 = [1, 8, 6, 2, 5, 4, 8, 25, 7]
height3 = [2, 3, 10, 5, 7, 8, 9]
print(tutorial(height3))
