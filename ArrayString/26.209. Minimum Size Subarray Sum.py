def f(target, nums):
    windows = []
    suma = 0
    l = 0
    for r in range(len(nums)):
        suma += nums[r]
        if suma > target:
            l = r
            suma = 0
        elif suma == target:
            windows.append(r - l)

    return min(windows)


target = 7
nums = [2, 3, 1, 2, 4, 3]
print(f(target, nums))
