def countGoodSubstrings(s):
    ans = 0
    for i in range(len(s)-2):
        ss = {}
        bol = True
        for x in range(i, i+3):
            if s[x] in ss:
                bol = False
                break
            else:
                ss[s[x]] = x
        if bol == True:
            ans += 1

    return ans


print(countGoodSubstrings("aababcabc"))
