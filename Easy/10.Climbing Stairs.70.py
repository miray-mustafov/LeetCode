def climbStairs(n):
    if n <= 3:
        return n

    steps = [0, 1, 2, 3]
    for i in range(4, n + 1):
        steps.append(steps[i - 1] + steps[i - 2])
    return steps.pop()


steps2 = 2
steps3 = 3
steps4 = 4
steps5 = 5
steps6 = 6
steps10 = 10
steps11 = 11
print(
    climbStairs(steps2),
    climbStairs(steps3),
    climbStairs(steps4),
    climbStairs(steps5),
    climbStairs(steps6),
    climbStairs(steps10),
    climbStairs(steps11),
)
