def maxConsecutiveAnswers(s, k):
    def helper(s, k, ch):
        l = res = ch_counter = 0
        for r in range(len(s)):
            ch_counter += 1 if s[r] == ch else 0
            while ch_counter > k:
                ch_counter -= 1 if s[l] == ch else 0
                l += 1
            res = max(res, r - l + 1)
        return res

    max_Ts = helper(s, k, 'F')
    max_Fs = helper(s, k, 'T')
    return max(max_Fs, max_Ts)


s = "TFFTFTFTT"
answerKey = "TTFFFTTFT"
k = 2
result = maxConsecutiveAnswers(s, k)
result2 = maxConsecutiveAnswers(answerKey, k)
print(result)
print(result2)
