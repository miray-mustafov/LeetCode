def tutorial(nums):  # O1 space
    res = [1] * len(nums)
    prefix = 1
    for i in range(len(nums)):
        res[i] = prefix
        prefix *= nums[i]

    postfix = 1
    for i in range(len(nums) - 1, -1, -1):
        res[i] *= postfix
        postfix *= nums[i]
    return res

def noDivisionSolution(nums):  # On memory and runtime
    output = []
    prefix = [1, ]
    postfix = nums[::]  # On
    postfix.append(1)

    for i in range(len(nums)):  # On
        prefix.append(prefix[i] * nums[i])

    for i in range(len(nums) - 1, -1, -1):  # On
        postfix[i] = nums[i] * postfix[i + 1]

    for i in range(len(nums)):  # On
        output.append(prefix[i] * postfix[i + 1])
    return output


def productExceptSelf(nums):
    answer = []
    product_no_zeroes = 1
    zeroes_count = 0

    for el in nums:
        if el == 0:
            zeroes_count += 1
            continue

        product_no_zeroes *= el

    if zeroes_count >= 2:
        return [0] * len(nums)

    for el in nums:
        if zeroes_count:
            if el == 0:
                answer.append(product_no_zeroes)
            else:
                answer.append(0)
        else:
            answer.append(product_no_zeroes // el)

    return answer


nums = [1, 2, 3, 4]  # [24,12,8,6]
print(productExceptSelf(nums.copy()))
print(noDivisionSolution(nums.copy()))
print(tutorial(nums.copy()))

print()
nums = [-1, 1, 0, -3, 3]  # [0,0,9,0,0]
print(productExceptSelf(nums))
print(noDivisionSolution(nums))
print(tutorial(nums.copy()))

print()
nums = [0, 4, 0]
print(productExceptSelf(nums))
print(noDivisionSolution(nums))
print(tutorial(nums.copy()))

print()
nums = [0, 0]
print(productExceptSelf(nums))
print(noDivisionSolution(nums))
print(tutorial(nums.copy()))
