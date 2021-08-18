def minRemovals(arr, k):
    n = len(arr) - 1
    arr.sort()
    i = 0
    sm = 999999
    while i < len(arr) and n > 0 and n != i:
        va = arr[n] - arr[i]
        print(va,  arr, i, n, len(arr))
        if va <= k and (len(arr) - (n - i) - 1) < sm:
            sm = (len(arr) - (n - i) - 1)
            i += 1
        elif va > k:
            i += 1
        else:
            n -= 1

    print(sm)


minRemovals(
    [1, 7, 14, 0, 9], 3
)
