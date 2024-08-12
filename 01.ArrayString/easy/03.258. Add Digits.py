def addDigits(num):
    def helper(num):
        digits_sum = 0
        num = str(num)
        for n in num:
            digits_sum += int(n)
        return digits_sum

    while num > 9:
        cur_num = num % 9
        if cur_num == 0:
            num = helper(num)
        else:
            num = cur_num

    return num


num = 388  # 2

print(addDigits(num))
