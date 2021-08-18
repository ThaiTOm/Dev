def findMaxLength(nums):
    dic = {0: 0}
    now = 0
    ans = 0
    for i in range(len(nums)):
        now += (1 if nums[i] == 1 else -1)
        if now in dic:
            ans = max(ans, i - dic[now] + 1)
        else:
            dic[now] = i + 1
    return ans


print(findMaxLength([0, 1, 0, 0, 1, 1, 0]))
