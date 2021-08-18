def maxSubArray(nums):
    ans = -999999999
    i = 0
    a = 0
    while i < len(nums):
        a += nums[i]
        ans = max(ans, a)
        a = max(a, 0)
        i += 1
    return ans


print(maxSubArray([-2, 1]))
