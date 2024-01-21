def solution(s, k):
    count, l, r = 0, 0, 1
    sett = set(s[l])
    while r < len(s):
        if s[r] not in sett:
            sett.add(s[r])
            if len(sett) == k:
                count += 1
                sett.remove(s[l])
                l += 1
        else:
            sett.clear()
            l = r + 1
        r += 1
    return count

s = 'havefunonleetcode'
k = 5
print(solution(s, k))  # 6
