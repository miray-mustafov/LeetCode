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
print(productExceptSelf(nums))
nums = [-1, 1, 0, -3, 3]  # [0,0,9,0,0]
print(productExceptSelf(nums))
nums = [0, 4, 0]
print(productExceptSelf(nums))
nums = [0, 0]
print(productExceptSelf(nums))
