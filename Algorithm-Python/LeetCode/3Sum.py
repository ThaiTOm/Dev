def threeSum(nums):
    ans = []
    i = 0
    leg = len(nums)
    nums.sort()
    if leg == 3 and sum(nums) == 0:
        return nums
    while i < len(nums) - 2:
        sbt = 0 - nums[i]
        x = i + 1
        y = leg - 1
        while x < len(nums) and y > i+2:
            sm = nums[x] + nums[y]
            if sm == sbt and x != y:
                ans.append([nums[i], nums[x], nums[y]])
            elif sm > sbt:
                y -= 1
                x -= 1
            x += 1
        i += 1
    print(ans)


threeSum(
    [0, 0, 0, 0]
)
