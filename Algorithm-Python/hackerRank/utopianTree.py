def utopianTree(n):
    x = 1
    for i in range(1, n+1):
        if i % 2 == 0:
            x += 1
        else:
            x *= 2
    print(x)
    return


utopianTree(1)
