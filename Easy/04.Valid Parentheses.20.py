def isValid(s):
    ocp = {'(': ')', '[': ']', '{': '}'}  # open: closed dictionary
    opens = []
    closes = []
    if len(s) % 2 == 1:  # s4 = "(" False
        return False

    for char in s:
        if char in ocp:
            opens.append(char)
        else:
            closes.append(char)  # for "((" edge case
            if not opens or ocp[opens.pop()] != char:
                return False

    # "(("
    if not closes or len(opens) - len(closes) >= 0:  # "[[[]" "[[[[]]"
        return False

    return True


s = "()"
s2 = "()[]{}"
s3 = "([{]})"
s4 = "("
s5 = "(("
s6 = "[[[]"
s7 = "[[[[]]"
s8 = "[[[[[[]]"
s9 = "[]]]"
s10 = "]]"
print(isValid(s))  # True
print(isValid(s2))  # True
print(isValid(s3))  # False
print(isValid(s4))  # False
print(isValid(s5))  # False
print(isValid(s6))  # False
print(isValid(s7))  # False
print(isValid(s8))  # False
print(isValid(s9))  # False
print(isValid(s10))  # False
