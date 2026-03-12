def spiral_order(matrix):
    result = []
    while matrix:
        result += matrix.pop(0)
        if matrix and matrix[0]:
            for row in matrix:
                result.append(row.pop())
        if matrix:
            result += matrix.pop()[::-1]  # reversed copy of that
        if matrix and matrix[0]:
            for row in matrix[::-1]:
                result.append(row.pop(0))
    return result


matrix = [
    [0, 1, 2, 3, 2],
    [11, 12, 13, 4, 2],
    [10, 15, 14, 5, 2],
    [9, 8, 7, 6, 2],
    [9, 8, 7, 6, 2]
]

print(spiral_order(matrix.copy()))
# print(f(matrix.copy()))
