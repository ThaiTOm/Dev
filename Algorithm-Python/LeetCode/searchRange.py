def searchRange(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    i = 0
    x = len(nums) - 1
    st = None
    ls = None
    if len(nums) == 1 and nums[0] == target:
        return [0, 0]
    while i < len(nums)-1 and x > 0:
        if nums[i] == target:
            st = i
        if nums[x] == target:
            ls = x
        if nums[i] < target:
            i += 1
        if nums[x] > target:
            x -= 1
        if st is not None and ls is not None:
            return [st, ls]
        if x == i and nums[x] == nums[i] == target:
            return [i, i]
        elif x == i:
            return [-1, -1]
    if st is not None:
        return [st, st]
    if ls is not None:
        return [ls, ls]
    return [-1, -1]
