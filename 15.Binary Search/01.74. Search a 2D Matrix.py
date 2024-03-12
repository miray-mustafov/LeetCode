def solution(matrix, target):
    def binary_search(nums, target):
        l, r = 0, len(nums) - 1
        while l <= r:
            m = l + ((r - l) // 2)
            if target > nums[m]:
                l = m + 1
            elif target < nums[m]:
                r = m - 1
            else:
                return True
        return False

    m, last_column_i = len(matrix), len(matrix[0]) - 1
    for r in range(m):
        if target < matrix[r][last_column_i]:
            return binary_search(matrix[r], target)
        elif target == matrix[r][last_column_i]:
            return True
    return False


matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
target = 30
print(solution(matrix, target))
print(solution([[1]], 1))
print(solution([[1]], 0))
