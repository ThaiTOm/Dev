def createNumber(n, k):
    ans = []
    if n == 1:
        return [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    def backTrack(nums, i, arr):
        if i == n:
            ans.append(int("".join(map(str, arr))))
            return
        else:
            if nums + k < 10:
                backTrack(k+nums, i+1, arr+[nums+k])
            if nums-k > 0:
                a = nums - k
                backTrack(nums-k, i+1, arr+[nums-k])
    for i in range(1, 10):

        if i-k >= 0:
            backTrack(i-k, 2, [i, i-k])
        if i + k < 10:
            backTrack(i+k, 2, [i, i+k])
    return ans


print(createNumber(0, 1))
