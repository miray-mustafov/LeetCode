def isPalindrome(s):
    word = ''
    is_palindrome = True
    for ch in s:
        if ch.isalnum():
            word += ch.lower()

    r = len(word) - 1
    for l in range(len(word)//2):
        if not word[l] == word[r]:
            return False
        r -= 1

    return is_palindrome


s = "A man, a plan, a canal: Panama"
s2 = "race a car"
print(isPalindrome(s))
print(isPalindrome(s2))
