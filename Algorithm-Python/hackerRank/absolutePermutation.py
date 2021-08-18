def absolutePermutation(n, k):
    arr = {}
    for i in range(1, n+1):
        if i - k > 0 and (i-k) not in arr:
            arr[i-k] = i-k
        elif i+k <= n and (i+k) not in arr:
            arr[i+k] = i+k
        else:
            return -1
    print([*arr])
    return arr


absolutePermutation(3, 2)
