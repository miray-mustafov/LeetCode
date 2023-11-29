def numSteps(num):
    steps = 0
    while num > 0:
        if num & 1 == 1:
            num -= 1
        else:
            num >>= 1
        steps += 1
    return steps


num = 14
print(numSteps(num))
