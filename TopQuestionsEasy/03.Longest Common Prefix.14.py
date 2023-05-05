def longestCommonPrefix(strs):
    # Vertical Scanning method
    if strs.__len__() == 1: return strs[0]

    prefix = ""
    for i_ch, ch in enumerate(strs[0]):
        for i in range(1, len(strs)):
            try:
                if ch is not strs[i][i_ch]:
                    return prefix
            except IndexError:
                return prefix

        prefix += ch

    return prefix


def horizontal_scanning(strs):
    prefix = strs[0]
    for str in strs[1:]:
        while str[:len(prefix)] != prefix:
            prefix = prefix[:-1]

            if not prefix:
                return ''
    return prefix


strs = ["flow", "flower", "flight"]  # "fl"
strs2 = ["dog", "racecar", "car"]  # ""
strs3 = ["dog"]  # "dog"
strs4 = ["cir", "car"]

print(
    longestCommonPrefix(strs),
    longestCommonPrefix(strs2),
    longestCommonPrefix(strs3),
)
print(longestCommonPrefix(strs4))

print(horizontal_scanning(strs))
print(horizontal_scanning(strs3))
print(horizontal_scanning(strs2))
