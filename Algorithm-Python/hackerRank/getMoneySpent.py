def getMoneySpent(k, d, b):
    value = 0
    if min(k) + min(d) > b:
        return -1
    for i in range(len(k)):
        x = 0
        while k[i] + min(d) <= b and x < len(d):
            value = k[i] + \
                d[x] if k[i] + \
                d[x] <= b and k[i] + d[x] > value else value
            print(value)
            x += 1

    print(value)


getMoneySpent([3, 1], [5, 2, 8], 10

              )
