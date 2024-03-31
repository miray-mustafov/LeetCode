def findWordsBFS(board, words):  # heavy bfs approach
    def backtr(r, c, word):
        if word in words:
            res.add(word)
        if not -1 < r < ROWS or not -1 < c < COLS or (r, c) in visited:
            return

        visited.add((r, c))
        backtr(r, c + 1, word + board[r][c])
        backtr(r + 1, c, word + board[r][c])
        backtr(r - 1, c, word + board[r][c])
        backtr(r, c - 1, word + board[r][c])
        visited.remove((r, c))

    ROWS, COLS = len(board), len(board[0])  # board len >= 1 !
    res, visited = set(), set()
    words = set(words)

    for r in range(ROWS):
        for c in range(COLS):
            backtr(r, c, '')

    return list(res)


board = [["o", "a", "a", "n"],
         ["e", "t", "a", "e"],
         ["i", "h", "k", "r"],
         ["i", "f", "l", "v"]]
words = ["oath", "pea", "eat", "rain"]
# Output: ["eat","oath"]
print(findWordsBFS(board, words))
board = [["a"]]
words = ["a"]
print(findWordsBFS(board, words))
