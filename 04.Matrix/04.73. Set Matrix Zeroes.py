def setZeroes(matrix):
    c = []
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == 0:
                c.append((row, col))
    for cor in c:
        for col in range(len(matrix[0])):
            matrix[cor[0]][col] = 0
        for row in range(len(matrix)):
            matrix[row][cor[1]] = 0

    [print(row) for row in matrix]


def setZeroesO1(matrix):
    ROWS, COLS = len(matrix), len(matrix[0])
    first_row = False

    for r in range(ROWS):
        for c in range(COLS):
            if matrix[r][c] == 0:
                matrix[0][c] = 0  # placing the zero on the top border
                if r > 0:
                    matrix[r][0] = 0  # placing zero on left side of the matrix
                else:
                    first_row = True  # handling the edge case of overlapping 00 position

    for r in range(1, ROWS):  # Setting each el of matr except the top&left borders
        for c in range(1, COLS):
            if matrix[0][c] == 0 or matrix[r][0] == 0:
                matrix[r][c] = 0

    if matrix[0][0] == 0: # setting first column to zero if needed
        for i in range(ROWS):
            matrix[i][0] = 0

    if first_row: # setting first row to zero if true
        for i in range(COLS):
            matrix[0][i] = 0


matrix = [
    [5, 0, 9, 11],
    [2, 4, 8, 10],
    [13, 3, 0, 7],
    [15, 5, 2, 6]
]
setZeroes(matrix)
