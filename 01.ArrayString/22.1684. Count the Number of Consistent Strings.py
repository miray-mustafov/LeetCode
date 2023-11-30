def f(allowed, words):
    allowed = set([x for x in allowed])
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

allowed = "abc"
words = ["a", "b", "c", "ab", "ac", "bc", "abc"]
print(f(allowed, words))
