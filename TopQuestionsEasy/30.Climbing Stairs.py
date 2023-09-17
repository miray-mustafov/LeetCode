def climbStairs(n):  # time efficient

    if n <= 3:
        return n

    steps = [0, 1, 2, 3]
    for i in range(4, n + 1):
        steps.append(steps[i - 1] + steps[i - 2])
    return steps.pop()


def clstr(n):  # memory efficient
    one, two = 1, 1
    for i in range(n-1):
        one, two = two + one, one
    return one


# print(climbStairs(7))
print(clstr(7))
