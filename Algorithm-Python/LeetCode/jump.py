def jump(nums):
    ans = 0
    l = 0
    r = 0
    while l < len(nums) and r < len(nums):
        if nums[l] < nums[r]:
            l = r
            r = r+1
            ans += 1
        elif r == len(nums) - 1:
            ans += 1
            r = len(nums)
        else:
            r += 1

    return ans


print(jump([1, 3, 2]))
