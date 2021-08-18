def productExceptSelf(nums):
    leg = len(nums)
    leftArr = [None] * leg
    rightArr = [None] * leg
    leftArr[0] = 1
    rightArr[-1] = 1
    for i in range(1, leg):
        leftArr[i] = leftArr[i-1] * nums[i-1]
        rightArr[leg-i-1] = rightArr[leg-i] * nums[leg-i]
    ans = []
    for i in range(leg):
        ans.append(leftArr[i] * rightArr[i])
    return ans


print(productExceptSelf([1, 2, 3, 4]))
