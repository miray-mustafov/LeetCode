def plusOne(digits):
    number = ''
    for n in digits:
        number += str(n)
    number = int(number) + 1
    result = []
    for n in str(number):
        result.append(int(n))
    return result

digits = [1, 2, 3]  # [1,2,4]
digits2 = [9]  # [1,0]
digits3 = [199]  # [2,0,0]
print(plusOne(digits))
print(plusOne(digits2))
print(plusOne(digits3))