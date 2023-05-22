def isIsomorphic(s, t):
    s_to_t, t_to_s = {}, {}
    for i, j in zip(s, t):
        if i in t_to_s and t_to_s[i] != j:
            return False
        if j in s_to_t and s_to_t[j] != i:
            return False
        t_to_s[i] = j
        s_to_t[j] = i
    return True


s = "egg"
t = "add"

s2 = "foo"
t2 = "bar"

s3 = "paper"
t3 = "title"
print(isIsomorphic(s, t))
print(isIsomorphic(s2, t2))
print(isIsomorphic(s3, t3))
