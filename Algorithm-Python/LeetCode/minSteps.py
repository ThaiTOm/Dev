def minSteps(s, t):
    lst1 = {}
    lst2 = {}
    ans = 0
    for i in range(len(t)):
        if s[i] in lst1:
            lst1[s[i]] = lst1[s[i]]+1
        if t[i] in lst2:
            lst2[t[i]] = lst2[t[i]]+1
        if s[i] not in lst1:
            lst1[s[i]] = 1
        if t[i] not in lst2:
            lst2[t[i]] = 1
    for i in lst1.keys():
        if i not in lst2:
            ans += lst1[i]
        elif i in lst2 and lst2[i] != lst1[i]:
            val = lst1[i] - lst2[i]
            if val > 0:
                ans += val

    return ans


print(minSteps("leetcode", "practice"))
