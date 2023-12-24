def findRepeatedDnaSequences(s):
    if len(s) <= 10:
        return []
    res, check_set = set(), set()
    for i in range(len(s) - 9):
        curr_dna_sequence = s[i:i + 10]
        if curr_dna_sequence not in check_set:
            check_set.add(curr_dna_sequence)
        else:
            res.add(curr_dna_sequence)
    return list(res)


s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"  # ["AAAAACCCCC","CCCCCAAAAA"]
s2 = "AAAAAAAAAAA"  # Output: ["AAAAAAAAAA"]
print(findRepeatedDnaSequences(s))
print(findRepeatedDnaSequences(s2))
