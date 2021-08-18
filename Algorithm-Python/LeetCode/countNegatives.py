def countNegatives(arr):
    ans = 0
    leg = len(arr[0])
    for i in range(len(arr)):
        for x in range(leg):
            if arr[i][x] < 0:
                ans += leg - x
                break

    return ans


print(countNegatives(
    [[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]
))
