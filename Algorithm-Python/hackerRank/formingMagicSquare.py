def formingMagicSquare(s):
    arr = [
        [[8, 1, 6], [3, 5, 7], [4, 9, 2]],
        [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
        [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
        [[2, 9, 4], [7, 5, 3], [6, 1, 8]],
        [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
        [[4, 3, 8], [9, 5, 1], [2, 7, 6]],
        [[6, 7, 2], [1, 5, 9], [8, 3, 4]],
        [[2, 7, 6], [9, 5, 1], [4, 3, 8]],
    ]

    def check(ar):
        an = 0
        for i in range(len(ar)):
            for x in range(len(ar[i])):
                an += abs(ar[i][x] - s[i][x])
        return an

    ans = 9999999999
    for i in arr:
        ol = check(i)
        if ol < ans:
            ans = ol
    print(ans)


formingMagicSquare([[4, 8, 2], [4, 5, 7], [6, 1, 6]])
