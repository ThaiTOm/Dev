def combinationSum(lf, c, t):
    """
    :type candidates: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    ans = []

    def backTrack(sbt, node):
        if sbt == 0:
            node.sort()
            b = node
            if b not in ans:
                ans.append(b)
            return
        if sbt < 0:
            return
        else:
            for i in c:
                arr = node
                backTrack(sbt-i, arr+[i])
    for i in c:
        backTrack(t-i, [i])

    return ans
