def divisorSubstrings(num, k):
    str_num = str(num)
    # if k == len(str_num):
    #     return 1
    res = 0
    for i in range(len(str_num) - (k - 1)):
        window = int(str_num[i:i + k])
        if window and num % window == 0:
            res += 1
    return res


def f(num, k):
    str_num = str(num)
    n = len(str_num)

    if k > n:
        return 0

    res = 0
    current_window = int(str_num[:k])

    if current_window and num % current_window == 0:
        res += 1

    for i in range(1, n - (k - 1)):
        # Update the current window by removing the leftmost digit
        # and adding the next digit to the right
        current_window = (current_window % (10 ** (k - 1))) * 10 + int(str_num[i + k - 1])

        if current_window and num % current_window == 0:
            res += 1

    return res


num = 240
k = 2
num2 = 430043
k2 = 2
print(divisorSubstrings(num, k))  # 2
print(divisorSubstrings(num2, k2))  # 2
print(f(num, k))  # 2
print(f(num2, k2))  # 2
