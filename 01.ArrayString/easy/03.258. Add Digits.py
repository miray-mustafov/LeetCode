def addDigits(num):
    num = str(num)
    cur_sum = 0
    while len(num) > 1:
        for n in num:
            cur_sum += int(n)
        num = str(cur_sum)
        cur_sum = 0
    return num

num = 38  # 2

print(addDigits(num))
