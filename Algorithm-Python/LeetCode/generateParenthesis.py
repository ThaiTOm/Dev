def generate(n):
    stack = []
    res = []

    def back(openN, closeN):
        if (openN == closeN == n):
            res.append("".join(stack))
            return
        if openN < n:
            stack.append("(")
            back(openN+1, closeN)
            stack.pop()
        if closeN < openN:
            stack.append(")")
            back(openN, closeN+1)
            stack.pop()
    back(0, 0)
    print(res)


generate(3)
