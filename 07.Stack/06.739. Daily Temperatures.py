def f(temperatures):
    answer = [0] * len(temperatures)
    stack = []
    for i, t in enumerate(temperatures):
        while stack and t > stack[-1][0]:
            cur = stack.pop()
            answer[cur[1]] = i - cur[1]

        stack.append((t, i))

    return answer


a = [73, 72, 75, 71, 69, 72, 76, 73]
print(f(a))
