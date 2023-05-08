def can_jump(nums):
    if len(nums) == 1:
        return True
    elif nums[0] == 0:
        return False

    i = len(nums) - 2
    while i > 0:
        if nums[i] == 0:
            j = i - 1
            can_jump_over0 = False
            while j > -1:
                if nums[j] + j > i:
                    can_jump_over0 = True
                    break
                j -= 1
            if not can_jump_over0:
                return False
            i = j
            continue
        i -= 1

    return True


nums_true = [2, 3, 1, 1, 4]
nums_true2 = [6, 4, 2, 1, 0, 4]
nums_true3 = [2, 0, 4, 2, 1, 0, 1, 4]
nums_false = [2, 0, 3, 2, 1, 0, 4]
nums_false2 = [1, 0, 3, 2, 0, 4]
nums_false3 = [3,0,0,0]
print(can_jump(nums_false))
