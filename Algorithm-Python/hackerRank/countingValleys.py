def countingValleys(s, t):
    value = 0
    now = 0
    low = 0
    for i in range(s):
        print(now, value)
        now = now+1 if t[i] == "U" else now - 1
        if now < low:
            low = now
        if now == 0 and t[i] == "U":
            value += 1
    if now < 0:
        value += 1
    print(value)

    return


countingValleys(8, "UDDDUDUU")
