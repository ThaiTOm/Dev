def beautifulDays(i, j, k):
    num = 0
    for i in range(i, j+1):
        st = int(str(i)[::-1])
        x = abs(i - st) % k
        print(x)
        if x == 0:
            num += 1
    print(num)
    return


beautifulDays(20, 23, 6)
