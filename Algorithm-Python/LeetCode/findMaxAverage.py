def findMaxAverage(nums, k):
    ans = 0
    for i in range(len(nums) - k+1):
        sm = sum(nums[i: k+i])
        ans = max(sm, ans)
    return ans / k


print(findMaxAverage([1, 12, -5, -6, 50, 3], 4))
