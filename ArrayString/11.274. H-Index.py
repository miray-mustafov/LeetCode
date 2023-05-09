def hIndex(citations):
    citations.sort(reverse=True)
    for i, c in enumerate(citations):
        if i >= c:
            return i
    return len(citations)


citations = [4, 0, 6, 1, 5]
citations2 = [1, 3, 1]
print(hIndex(citations))
print(hIndex(citations2))
