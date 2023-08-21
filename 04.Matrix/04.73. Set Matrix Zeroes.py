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
    pass


matrix = [
    [5, 0, 9, 11],
    [2, 4, 8, 10],
    [13, 3, 0, 7],
    [15, 5, 2, 6]
]
setZeroes(matrix)
