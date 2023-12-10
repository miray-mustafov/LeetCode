def candy(ratings):
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


r1 = [1, 0, 2]  # 5
r2 = [1, 2, 2]  # 4
r3=[0,2,3,2,1]# 1 2 3 2 1
print(candy(r1))
print(candy(r2))
print(candy(r3
            ))
