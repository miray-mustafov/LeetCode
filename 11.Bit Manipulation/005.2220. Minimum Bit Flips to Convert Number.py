def minBitFlips(start, goal):
    return bin(start ^ goal).count('1')


start = 10
goal = 7
print(minBitFlips(start, goal))
