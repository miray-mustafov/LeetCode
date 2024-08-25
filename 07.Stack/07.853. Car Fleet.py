# simplifying the problem
# visualization needed


def carFleet(target: int, position: list, speed: list[int]) -> int:
    fleets_stack = []
    pairs = [(p, s) for p, s in zip(position, speed)]

    for p, s in sorted(pairs, reverse=True):  # descending by position (the first el in the tuples)
        trt = (target - p) / s  # current t-ime to r-each the t-arget
        if fleets_stack and fleets_stack[-1] >= trt:
            continue
        fleets_stack.append(trt)

    return len(fleets_stack)


target = 12
position = [10, 8, 0, 5, 3]
speed = [2, 4, 1, 1, 2]
print(carFleet(target, position, speed))
