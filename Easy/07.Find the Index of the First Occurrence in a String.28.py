"""my first attempt 20%, 89%"""
def strStr(haystack, needle):
    replaced = haystack.replace(needle, ' ', 1)

    try:
        return replaced.index(' ')
    except ValueError:
        return -1


haystack = "sssadbutsad"
needle = "sad"

haystack2 = "leetcode"
needle2 = "leeto"
print(strStr(haystack, needle))

print(strStr(haystack2, needle2))
