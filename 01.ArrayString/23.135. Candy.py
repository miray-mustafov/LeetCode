def candy(ratings):  # My try for O(1*N) solution but unsuccessful
    min_candy = 1
    slider_dec, slider_inc = 0, 0
    for i in range(1, len(ratings)):
        if ratings[i - 1] < ratings[i]:
            min_candy += 1 + (i - slider_inc)
            slider_dec = i
        elif ratings[i - 1] > ratings[i]:
            min_candy += 1 + (i - slider_dec)
            slider_inc = i
        else:
            min_candy += 1
            slider_inc, slider_dec = i, i

    return min_candy


def candy2(ratings):
    arr = [1] * len(ratings)
    for i in range(1, len(ratings)):
        if ratings[i - 1] < ratings[i]:
            arr[i] = arr[i - 1] + 1

    for i in range(len(ratings) - 2, -1, -1):
        if ratings[i] > ratings[i + 1]:
            arr[i] = max(arr[i], arr[i + 1] + 1)

    return sum(arr)


def candy3(ratings):
    if not ratings:
        return 0

    ret, up, down, peak = 1, 0, 0, 0

    for prev, curr in zip(ratings[:-1], ratings[1:]):
        if prev < curr:
            up, down, peak = up + 1, 0, up + 1
            ret += 1 + up
        elif prev == curr:
            up = down = peak = 0
            ret += 1
        else:
            up, down = 0, down + 1
            ret += 1 + down - int(peak >= down)

    return ret


r1 = [1, 0, 2]  # 5
r2 = [1, 2, 2]  # 4
r3 = [0, 2, 3, 2, 1]  # 1 2 3 2 1 = 9
r5 = [0, 2, 3, 2, 1, 0, -1]  # 1 2 5 4 3 2 1 = 9
r4 = [1, 2, 0, 1]  # 1, 2 ,1 ,2 = 6
print(candy2(r1))
print(candy3(r5))
# print(candy(r1))
# print(candy(r2))
# print(candy(r3))
# print(candy(r4))
