def convert(s, numRows):
    if numRows == 1:
        return s
    sbt = max((numRows - 3) + numRows, 1) + 1
    i = 0
    ans = ""
    while i < len(s) and sbt > 0:
        x = i
        while x <= len(s) - 1:
            ans += s[x]
            print(s[x], x, ans, sbt)
            x += sbt
        sbt -= 2
        i += 1
    print(sbt, ans)
    return


convert("PAYPALISHIRING", 4)
