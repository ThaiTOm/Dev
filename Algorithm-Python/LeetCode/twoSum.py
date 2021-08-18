def twoSum(nums, target):
    ls = {}
    for i in range(len(nums)):
        if (target - nums[i]) in ls:
            return [ls[target - nums[i]], i]
        else:
            ls[nums[i]] = i
    return


print(twoSum([2, 7, 11, 15], 9))
