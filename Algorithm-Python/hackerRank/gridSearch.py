def gridSearch(g, p):
    i = 0
    while i < len(g):
        if p[0] in g[i]:
            ind = g[i].index(p[0])
            x = 1
            bol = 1
            while x < len(p):
                if (i+x > len(g)-1) or (p[x] not in g[i+x]) or (g[i+x].index(p[x]) != ind):
                    x = len(p)
                else:
                    bol += 1
                    x += 1
            print(bol, len(p))
            if bol >= len(p) - 1 and len(p) - 1 > 1:
                print("yes")
                return "YES"
        i += 1
    return "NO"


gridSearch([
    '111111111111111',
    '111111111111111',
    '111111111111111',
    '111111011111111',
    '111111111111111',
    '111111111111111',
    '101010101010101'
],
    [
    '11111',
    '11111',
    '11111',
    '11110'
])
