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


r1 = [1, 0, 2]  # 5
r2 = [1, 2, 2]  # 4
r3 = [0, 2, 3, 2, 1]  # 1 2 3 2 1
r4 = [1, 2, 0, 1]  # 1, 2 ,1 ,2 = 6
print(candy2(r1))
# print(candy(r1))
# print(candy(r2))
# print(candy(r3))
# print(candy(r4))
