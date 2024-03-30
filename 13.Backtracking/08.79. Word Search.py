def exist(board: list[list[str]], word: str) -> bool:
    ROWS, COLS = len(board), len(board[0])
    path = set()

    def dfs(r, c, i):
        if i == len(word):
            return True
        if not -1 < r < ROWS or not -1 < c < COLS or \
                board[r][c] != word[i] or (r, c) in path:
            return False

        path.add((r, c))
        res = (dfs(r, c + 1, i + 1) or
               dfs(r + 1, c, i + 1) or
               dfs(r, c - 1, i + 1) or
               dfs(r - 1, c, i + 1)
               )
        path.remove((r, c))
        return res

    for r in range(ROWS):
        for c in range(COLS):
            if dfs(r, c, 0):
                return True
    return False


board = [["A", "B", "C", "C"],
         ["S", "F", "C", "S"],
         ["A", "D", "E", "E"]]
word = "ABCCED"
print(exist(board, word))  # true
