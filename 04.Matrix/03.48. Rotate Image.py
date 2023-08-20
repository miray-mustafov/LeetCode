def rotate(matrix):
    l, r = 0, len(matrix) - 1  # square
    while l < r:  # ?
        top, bot = l, r
        for i in range(r - l):
            top_left_el = matrix[top][l+i]

            matrix[top][l+i] = matrix[bot-i][l]
            matrix[bot-i][l] = matrix[bot][r-i]
            matrix[bot][r-i] = matrix[top+i][r]
            matrix[top+i][r] = top_left_el

        l += 1
        r -= 1

    [print(row) for row in matrix]


matrix = [
    [5, 1, 9, 11],
    [2, 4, 8, 10],
    [13, 3, 6, 7],
    [15, 5, 3, 6]
]
rotate(matrix)
