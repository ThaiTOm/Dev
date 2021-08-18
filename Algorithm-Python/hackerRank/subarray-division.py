def birthday(s, d, m):
    value = 0

    for i in range(len(s)):
        sm = 0
        for x in range(m):
            if x + i < len(s):
                sm += s[x + i]
        if sm == d:
            value += 1
    print(value)
    return value


birthday([4], 4, 1)
