def f(pattern, s):  # O(m+n)
    s = s.split()
    if len(s) != len(pattern):
        return False
    word_char, char_word = {}, {}
    for ch, w in zip(pattern, s):
        if ch in char_word and char_word[ch] != w:
            return False
        if w in word_char and word_char[w] != ch:
            return False
        char_word[ch] = w
        word_char[w] = ch
    return True


pattern = "abbac"
s = "dog cat cat dog fish"

pattern1 = "abba"
s1 = "dog cat cat fish"

pattern2 = "aaaa"
s2 = "dog cat cat dog"

print(f(pattern, s))
print(f(pattern1, s1))
print(f(pattern2, s2))
