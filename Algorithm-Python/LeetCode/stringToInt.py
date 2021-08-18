def myAtoi(s):
    s = s.replace(" ", "")
    tr = te = len(s)
    i = 0
    while i < len(s) - 1:
        if s[i].isnumeric():
            tr = min(i, tr)
            i += 1
        elif s[i].isalpha():
            s = s.replace(s[i], "")
            te = min(i, te)
        if te < tr:
            return 0
    s = int()
    if s > 2147483647:
        return 2147483647
    elif s < -2147483648:
        return -2147483648
    return s


myAtoi("4193 with words")
