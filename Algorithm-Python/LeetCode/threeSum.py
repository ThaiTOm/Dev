def threeSum(nums):
    nums.sort()
    ans = []
    for i in range(len(nums)-1):
        y = len(nums)-1
        x = i+1
        sbt = 0 - nums[i]
        while x < len(nums) and y > x:
            if nums[x] + nums[y] == sbt:
                if [nums[x], nums[y], nums[i]] not in ans:
                    ans.append([nums[x], nums[y], nums[i]])
            if nums[x] + nums[y] > sbt:
                y -= 1
            else:
                x += 1

    return ans
