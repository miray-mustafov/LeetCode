def f(s, k):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    cur_max = 0
    for el in s[:k]:
        cur_max += el in vowels
    res_max = cur_max
    for i in range(k, len(s)):
        cur_max = cur_max - (s[i - k] in vowels) + (s[i] in vowels)
        res_max = max(res_max, cur_max)
    return res_max


def max_vowels_substring(s, k):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    cur_max = sum(1 for el in s[:k] if el in vowels)
    res_max = cur_max
    for i in range(k, len(s)):
        cur_max -= s[i - k] in vowels
        cur_max += s[i] in vowels
        res_max = max(res_max, cur_max)
    return res_max


s, k = "abciiidef", 3  # res = 3
print(f(s, k))
print(max_vowels_substring(s, k))
