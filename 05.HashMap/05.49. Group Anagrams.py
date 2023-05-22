from collections import defaultdict


def groupAnagrams(strs):
    def orderByAscii(string):
        ordered_chars = sorted(string, key=lambda x: ord(x))
        return ''.join(ordered_chars)

    d = defaultdict(list)
    for s in strs:
        s_ordered = orderByAscii(s)
        d[s_ordered].append(s)
    res = list(d.values())
    return res


def groupAnagrams2(strs):
    def count_chars(s):
        char_count = [0] * 26  # Assuming lowercase English letters
        for char in s:
            char_count[ord(char) - ord('a')] += 1
        return tuple(char_count)

    grouped_anagrams = defaultdict(list)
    for s in strs:
        char_count = count_chars(s)
        grouped_anagrams[char_count].append(s)

    return list(grouped_anagrams.values())


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

print(groupAnagrams(strs))
print(groupAnagrams2(strs))
