def divisorSubstrings(num, k):
    str_num = str(num)
    # if k == len(str_num):
    #     return 1
    res = 0
    for i in range(len(str_num) - (k-1)):
        window = int(str_num[i:i + k])
        if window and num % window == 0:
            res += 1
    return res


num = 240
k = 2
num2 = 430043
k2 = 2
print(divisorSubstrings(num, k))  # 2
print(divisorSubstrings(num2, k2))  # 2
