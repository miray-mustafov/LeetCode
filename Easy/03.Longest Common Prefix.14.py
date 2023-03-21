def longestCommonPrefix(strs):
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


strs = ["flower", "flow", "flight"]  # "fl"
strs2 = ["dog", "racecar", "car"]  # ""
strs3 = ["dog"]  # "dog"
strs4 = ["cir", "car"]
print(
    longestCommonPrefix(strs),
    longestCommonPrefix(strs2),
    longestCommonPrefix(strs3),
)
print(longestCommonPrefix(strs4))
