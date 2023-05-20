import collections


def isValidSudoku(board):
    help_set = set()
    for row in range(9):  # Rows check
        help_set.clear()
        for col in range(9):
            if board[row][col] not in help_set:
                if board[row][col] != '.':
                    help_set.add(board[row][col])
            else:
                return False

    for col in range(9):  # Cols check
        help_set.clear()
        for row in range(9):
            if board[row][col] not in help_set:
                if board[row][col] != '.':
                    help_set.add(board[row][col])
            else:
                return False

    for r in range(0, 9, 3):
        for c in range(0, 9, 3):
            help_set.clear()
            for row in range(r, r + 3):
                for col in range(c, c + 3):
                    if board[row][col] not in help_set:
                        if board[row][col] != '.':
                            help_set.add(board[row][col])
                    else:
                        return False
    return True


def tutorial(board):
    cols = collections.defaultdict(set)
    rows = collections.defaultdict(set)
    squares = collections.defaultdict(set)
    for r in range(9):
        for c in range(9):
            if board[r][c] == '.':
                continue
            if board[r][c] in rows[r] or \
                    board[r][c] in cols[c] or \
                    board[r][c] in squares[(r // 3, c // 3)]:
                return False
            rows[r].add(board[r][c])
            cols[c].add(board[r][c])
            squares[(r // 3, c // 3)].add(board[r][c])
    return True


board_true = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"], ]

board_false = [
    ["8", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"], ]

board_false2 = [
    [".", ".", "5", ".", ".", ".", ".", ".", "."],
    ["1", ".", ".", "2", ".", ".", ".", ".", "."],
    [".", ".", "6", ".", ".", "3", ".", ".", "."],
    ["8", ".", ".", ".", ".", ".", ".", ".", "."],
    ["3", ".", "1", "5", "2", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", "4", "."],
    [".", ".", "6", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", "9", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."], ]

print(isValidSudoku(board_true))
print(isValidSudoku(board_false))
print(isValidSudoku(board_false2))
print('tutorial: ')
print(isValidSudoku(board_true))
print(tutorial(board_false2))
