def groupAnagrams(strs):
    from collections import defaultdict
    def orderByAscii(string):
        ordered_chars = sorted(string, key=lambda x: ord(x))
        return ''.join(ordered_chars)

    d = defaultdict(list)
    for s in strs:
        s_ordered = orderByAscii(s)
        d[s_ordered].append(s)
    res = list(d.values())
    return res


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

print(groupAnagrams(strs))
