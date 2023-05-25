def isValid(s):
    if len(s) % 2 == 1:
        return False
    ocp = {'(': ')', '[': ']', '{': '}'}
    opens = []
    for char in s:
        if char in ocp:
            opens.append(char)
        elif not opens or ocp[opens.pop()] != char:
            return False

    return True if not opens else False


s = "([]{})"
print(isValid(s))
