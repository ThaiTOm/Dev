def pickingNumbers(a):
    ans = []

    def check(arr, x):
        for i in range(len(arr)):
            if abs(arr[i] - x) > 1:
                return False
        return True
    for i in range(len(a)):
        brr = [a[i]]
        x = 0
        while x < len(a):
            if x != i:
                bol = check(brr, a[x])
                print(bol, brr, a[x])
                if bol == True:
                    brr.append(a[x])
            x += 1
        if len(brr) > len(ans):
            ans = brr

    return


pickingNumbers([1, 2, 2, 3, 1, 2])
