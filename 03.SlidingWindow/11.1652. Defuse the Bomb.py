def decrypt(code, k):
    n = len(code)
    if k == 0:
        return [0] * n

    cur_sum, res = 0, []
    if k > 0:
        for i in range(1, k + 1):  # can optimize for abs(k)>n
            cur_sum += code[i % n]
        res.append(cur_sum)
        for i in range(1, n):
            cur_sum = cur_sum - code[i] + code[(i + k) % n]
            res.append(cur_sum)
    else:
        for i in range(n - 1, n + (k -1), -1):  # can optimize for abs(k)>n
            cur_sum += code[i % n]
        res.append(cur_sum)
        for i in range(1, n):
            cur_sum = cur_sum - code[(i - 1 + k) % n] + code[i - 1]
            res.append(cur_sum)
    return res


code, k = [5, 7, 1, 4], 3  # Output: [12, 10, 16, 13]
code2, k2 = [1, 2, 3, 4], 0  # output [0,0,0,0]
code3, k3 = [2, 4, 9, 3], -2  # Output: [12, 5, 6, 13]
print(decrypt(code, k))
print(decrypt(code2, k2))
print(decrypt(code3, k3))
code4 = [10, 5, 7, 7, 3, 2, 10, 3, 6, 9, 1, 6]
k4 = -4
print(decrypt(code4, k4))  # [22,26,22,28,29,22,19,22,18,21,28,19]
