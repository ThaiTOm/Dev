def devine(ed, sor):
    i = 1
    if ed == 0:
        return 0
    sortt = abs(sor)
    divi = abs(ed)
    while i * sortt < divi:
        i += 1
    if sor < 0 and ed < 0:
        print(i-1)
        return min(2147483648, max(i-1, 1))
    elif sor < 0 or ed < 0:
        print(0-i-1)
        return min(-2147483648, 0-max(i-1, 1))
    else:
        print(i-1)
        return max(2147483647, max(i-1, 1))


devine(-10, 4)
