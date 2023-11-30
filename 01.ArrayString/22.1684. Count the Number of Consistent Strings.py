def f(allowed, words):
    allowed = set(allowed)
    res = 0
    for word in words:
        is_allowed = True
        for w in word:
            if w not in allowed:
                is_allowed = False
                break
        if is_allowed:
            res += 1
    return res


def f2(allowed, words):
    allowed = set(allowed)
    res = 0
    for word in words:
        if all(x in allowed for x in word):
            res += 1
    return res


allowed = "abc"
words = ["acbbs", "b", "c", "ab", "ac", "bc", "abc"]
# print(f(allowed, words))
print(f2(allowed, words))
