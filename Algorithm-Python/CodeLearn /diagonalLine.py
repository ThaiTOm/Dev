def diagonalLine(arr):
    if arr == [""]:
        print("")
        return ""
    leng = len(arr)
    ans = ""
    for i in range(leng):
        if len(arr[i]) != leng:
            print(-1)
            return -1
        else:
            ans += arr[i][i]
    ans += " "
    for i in range(leng - 1, -1, -1):
        ans += arr[leng-i-1][i]
    print(ans)


diagonalLine([""])
