import re


def isPalindrome(s):
    word = ''
    is_palindrome = True
    for ch in s:
        if ch.isalnum():
            word += ch.lower()

    r = len(word) - 1
    for l in range(len(word) // 2):
        if not word[l] == word[r]:
            return False
        r -= 1

    return is_palindrome


def is_palindrome_optimized(s):
    l, r = 0, len(s) - 1
    while l < r:
        while l < r and not s[l].isalnum():
            l += 1
        while l < r and not s[r].isalnum():
            r -= 1

        if not s[l].lower() == s[r].lower():
            return False
        l += 1
        r -= 1
    return True


def is_palindrome_withregex(s):
    s = re.sub('[^a-z0-9]', '', s.lower())
    l, r = 0, len(s) - 1
    while l < r:
        if not s[l] == s[r]:
            return False
        l += 1
        r -= 1
    return True


s = "A man, a plan, a canal: Panama"
s2 = "race a car"
print(is_palindrome_optimized(s))
print(is_palindrome_optimized(s2))
print(is_palindrome_optimized('.,'))
print()
print(is_palindrome_withregex(s))
print(is_palindrome_withregex(s2))
print(is_palindrome_withregex('.,'))
