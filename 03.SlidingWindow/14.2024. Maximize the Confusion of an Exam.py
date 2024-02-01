def maxConsecutiveAnswers(answerKey, k):
    def max_consecutive_answers_helper(s, k, target_char):
        ans = l = r = cnt = 0

        while r < len(s):
            if s[r] == target_char:
                cnt += 1
            while cnt > k:
                if s[l] == target_char:
                    cnt -= 1
                l += 1
            ans = max(ans, r - l + 1)
            r += 1

        return ans

    result_t = max_consecutive_answers_helper(answerKey, k, 'F')
    result_f = max_consecutive_answers_helper(answerKey, k, 'T')

    return max(result_t, result_f)


s = "TFFTFTFTT"
answerKey = "TTFFFTTFT"
k = 2
result = maxConsecutiveAnswers(s, k)
result2 = maxConsecutiveAnswers(answerKey, k)
print(result)
print(result2)