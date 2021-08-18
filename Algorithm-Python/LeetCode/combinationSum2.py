def combinationSum2(c, t):
    ans = []
    leg = len(c)
    c.sort()
    if sum(c) < t:
        return

    def backTrack(n, sbt, ind):
        if sbt == 0:
            ans.append(n)
            return True
        if sbt < c[min(ind+1, leg-1)] or sbt < 1:
            return False
        else:
            for i in range(ind+1, len(c)):
                bo = backTrack(n+[c[i]], sbt - c[i], i)
                if bo == True:
                    return

    for i in range(len(c)):
        if i != 0 and c[i] != c[0]:
            backTrack([c[i]], t-c[i], i)
        if i == 0:
            backTrack([c[i]], t-c[i], i)

    return ans


print(combinationSum2([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                      27))
