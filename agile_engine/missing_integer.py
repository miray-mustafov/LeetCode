def solution(A):
    # hset = set()
    res = 1
    A.sort()  # O Nlogn
    for i in range(len(A)):  # O N (worstcase)
        if res == A[i]:
            res += 1
        elif i > 0 and A[i] != A[i - 1]:  # res != A[i]:
            return res
    return res


A1 = [1, 2, 3]  # 4.

A2 = [-1, -3]  # 1.
A3 = [1, 3, 6, 4, 1, 2]  # 5.
A4 = [1, 1, 1, 2, 4]  # 3.

print(solution(A1))
print(solution(A2))
print(solution(A3))
print(solution(A4))
