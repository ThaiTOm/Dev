def demo(s):
    symbol = {
        ")": "(", "}": "{", "]": "["
    }
    arr = []
    for i in s:
        if i in symbol.values():
            arr.append(i)
        elif arr and arr[-1] == symbol[i]:
            arr.pop()
        else:
            print(False)
    print(arr == [])


demo("({})")
