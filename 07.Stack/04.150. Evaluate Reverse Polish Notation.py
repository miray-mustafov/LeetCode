def evalRPN(tokens):
    nums = []

    for t in tokens:
        if t.isdigit() or (t[0] == '-' and t[1:].isdigit()):
            nums.append(int(t))
        else:
            n2, n1 = nums.pop(), nums.pop()
            if t == '+':
                nums.append(n1 + n2)
            elif t == '-':
                nums.append(n1 - n2)
            elif t == '*':
                nums.append(n1 * n2)
            elif t == '/':
                nums.append(int(n1 / n2))
    return nums.pop()


tokens2 = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
tokens = ["2", "1", "+", "3", "*"]
tokens1 = ["4", "13", "5", "/", "+"]
print(evalRPN(tokens2))
'''note
1. make ifs elifs
'''
