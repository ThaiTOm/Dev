import math


def round_opposite(n):
    ans, w = math.modf(n)
    print(ans)
    if ans >= 0.5:
        print(math.floor(n))
        return math.floor(n)
    else:
        print(math.ceil(n))
        return math.ceil(n)


round_opposite(1.0)
