def f(temperatures):
    if len(temperatures) == 1:
        return [0]

    answer = [0] * len(temperatures)
    stack = [(temperatures[0], 0)]
    for i, t in enumerate(temperatures[1:], start=1):
        while stack and t > stack[-1][0]:
            cur = stack.pop()
            answer[cur[1]] = i - cur[1]

        stack.append((t, i))
    return answer


a = [73, 72, 75, 71, 69, 72, 76, 73]
print(f(a))
