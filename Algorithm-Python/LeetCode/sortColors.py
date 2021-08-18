def sortColors(nums):
    i = 0
    while i < len(nums):
        if nums[i] == 0:
            x = 0
            while x > -1:
                if nums[x] != 0:
                    nums[x], nums[i] = nums[i], nums[x]
                    x = -10
                if i == x:
                    x = -10
                x += 1

        if nums[i] == 2:
            x = len(nums) - 1
            while x > 0:
                if nums[x] != 2:
                    nums[x], nums[i] = nums[i], nums[x]
                    i -= 1
                    x = -10
                if i == x:
                    x = -10
                x -= 1
        i += 1
    return nums


print(sortColors([1, 2, 0]))
