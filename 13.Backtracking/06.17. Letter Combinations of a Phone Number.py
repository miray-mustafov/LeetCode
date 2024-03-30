def letterCombinations(digits):
    hmap = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }
    res = []

    def dfs(i, cur_str):
        if i >= len(digits):
            res.append(cur_str)
            return
        for ch in hmap[digits[i]]:
            cur_str += ch
            dfs(i + 1, cur_str)
            cur_str = cur_str[:-1]
        return

    dfs(0, '')
    return res


def tutorial(digits):
    hmap = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }
    res = []

    def dfs(i, cur_str):
        if i >= len(digits):
            res.append(cur_str)
            return
        for ch in hmap[digits[i]]:
            dfs(i + 1, cur_str + ch)
        return

    if digits:
        dfs(0, '')
    else:
        return []
    return res


digits = '234'
print(letterCombinations(digits))
print(tutorial(digits))
