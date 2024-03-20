def decode(encoded, first):
    encoded.append(0)
    for i in range(len(encoded)):
        temp = encoded[i]
        encoded[i] = first
        first ^= temp
    return encoded


def decode2(encoded, first):
    out = [first]
    n = len(encoded)
    for i in range(n):
        out.append(out[i] ^ encoded[i])
    return out


encoded = [1, 2, 3]
first = 1
encoded2 = [1, 2, 3]
print(decode(encoded, first))
print(decode2(encoded2, first))
