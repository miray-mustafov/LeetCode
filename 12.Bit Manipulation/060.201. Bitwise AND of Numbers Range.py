def rangeBitwiseAnd(left, right):
    count = 0
    while left != right:
        left >>= 1
        right >>= 1
        count += 1
    return left << count


left = 5
right = 7
left2 = 1
right2 = 2147483647
print(rangeBitwiseAnd(left, right))
print(rangeBitwiseAnd(left2, right2))
