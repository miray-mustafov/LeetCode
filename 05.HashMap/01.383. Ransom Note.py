from collections import defaultdict


def canConstruct(ransomNote, magazine):
    if len(magazine) < len(ransomNote):
        return False
    d = defaultdict(int)
    for el in magazine:
        d[el] += 1

    for el in ransomNote:
        if el in d:
            if d[el] == 0:
                return False
            d[el] -= 1
        else:
            return False
    return True


ransomNote = "aa"
magazine = "aab"
print(canConstruct(ransomNote, magazine))
