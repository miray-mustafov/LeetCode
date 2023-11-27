def decode(encoded, first):
    encoded.append(0)
    for i in range(len(encoded)):
        temp = encoded[i]
        encoded[i] = first
        first ^= temp
    return encoded


encoded = [1, 2, 3]
first = 1
# Output: [1,0,2,1]
print(decode(encoded, first))
