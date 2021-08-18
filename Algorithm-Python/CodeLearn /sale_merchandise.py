def sale_merchandise(s, si):
    ans = {}
    res = []
    for i in s:
        if i in ans:
            ans[i] = ans[i] + 1
        else:
            ans[i] = 1
    for i in si:
        if i in ans and ans[i] > 1:
            res.append(ans[i]//2)
        else:
            res.append(0)
    print(res)
    return ans


sale_merchandise([3, 8, 8, 1, 5], [3, 1, 8])
