def f(turnedOn):
    output = []
    for h in range(12):
        for m in range(60):
            temp = (bin(h) + bin(m)).count('1')
            if temp == turnedOn:
                time = '%d:%02d' % (h, m)
                output.append(time)
    return output


turnedOn = 1
turnedOn2 = 2
turnedOn3 = 9
print(f(turnedOn))
print(f(turnedOn2))
print(f(turnedOn3))
print(f(8))
