def rob(nums):
    rob1, rob2 =0,0
    for n in nums:
        temp = max(n+rob1,rob2)
        rob1 = rob2
        rob2 = temp
    return rob2

houses = [5,2,2,4, 1]
print(rob(houses))