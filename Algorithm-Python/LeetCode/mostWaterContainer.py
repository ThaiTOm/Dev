def maxWater(height):
    res = 0
    r = len(height) - 1
    l = 0
    hmax = max(height)
    while (r - l) * hmax >= res:
        if height[l] < height[r]:
            area = height[l] * (r - l)
        else:
            area = height[r] * (r - l)
        if area > res:
            res = area
        if height[r] > height[l]:
            l += 1
        else:
            r -= 1
    return res


maxWater([1, 8, 6, 2, 5, 4, 8, 3, 7])
