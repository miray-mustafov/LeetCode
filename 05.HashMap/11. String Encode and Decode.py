class Solution:
    def encode(self, strs: list[str]) -> str:
        encoded = ''
        for s in strs:
            encoded += str(len(s)) + "#" + s
        return encoded

    def decode(self, s: str) -> list[str]:
        i, res = 0, []
        count = ''
        while i < len(s):
            if s[i].isnumeric():
                count += s[i]
                i += 1
            elif s[i] == "#":
                count = int(count)
                res.append(s[i + 1: i + count + 1])
                i = i + count + 1
                count = ''
        return res

inputt = ["we", "sa#y", '#2', '#']
obj = Solution()
encoded = obj.encode(inputt)
decoded = obj.decode(encoded)
print(encoded)
print(decoded)

"""
String Encode and Decode
Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.

Please implement encode and decode

Example 1:

Input: ["neet","code","love","you"]

Output:["neet","code","love","you"]
Example 2:

Input: ["we","say",":","yes"]

Output: ["we","say",":","yes"]
Constraints:

0 <= strs.length < 100
0 <= strs[i].length < 200
strs[i] contains only UTF-8 characters.
"""
