def numSteps(num):
    steps = 0
    while num > 0:
        if num & 1 == 1:
            num -= 1
        else:
            num >>= 1
        steps += 1
    return steps


def numSteps1line(num):
    return len(bin(num)[2:]) + bin(num).count('1') - 1


num = 14
print(numSteps(num))
print(numSteps1line(num))
