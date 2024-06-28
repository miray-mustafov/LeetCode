def f(word1, word2):
    idx1 = idx2 = 0
    i1 = i2 = 0
    while idx1 < len(word1) and idx2 < len(word2):
        w1, w2 = word1[idx1], word2[idx2]

        while i1 < len(w1) and i2 < len(w2):
            if w1[i1] != w2[i2]:
                return False
            i1, i2 = i1 + 1, i2 + 1

        if not i1 < len(w1):
            i1, idx1 = 0, idx1 + 1
        if not i2 < len(w2):
            i2, idx2 = 0, idx2 + 1

    # if i1 != 0 or i2 != 0:  # the edge case, means one is longer
    if idx1 < len(word1) or idx2 < len(word2):
        return False
    return True


def f2(word1, word2):  # no brain solution
    w1 = ''.join(word1)
    w2 = ''.join(word2)
    return w1 == w2


word1, word2 = ["ab", "c"], ["a", "bc"]
print(f(word1, word2))
word1, word2 = ["a", "cb"], ["ab", "c"]
print(f(word1, word2))
word1, word2 = ["a", "b", 'c'], ["abc"]
print(f(word1, word2))  # True
word1, word2 = ["a", "b", 'cc'], ["abc"]  # the edge case
print(f(word1, word2))  # False

print()
word1 = ["a"]
word2 = ["a", "b"]
print(f(word1, word2))  # False
