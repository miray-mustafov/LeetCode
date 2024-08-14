def f(s):
    if len(s) == 1:
        return True
    l, r = 0, len(s) - 1
    while True:
        while not s[l].isalnum() and l < r:
            l += 1
        while not s[r].isalnum() and r > l:
            r -= 1

        if l >= r:
            break
        if s[l].lower() != s[r].lower():
            return False

        l, r = l + 1, r - 1

    return True


s = ",,Aman, a plan, a canal: Panama"
print(f(s))
s = "race a car"
print(f(s))
s = ",."
print(f(s))
s = "0P"
print(f(s))
