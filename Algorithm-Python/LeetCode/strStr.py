def strStr(haystack, needle):
    if not needle and not haystack:
        return 0
    if needle not in haystack:
        return -1
    else:
        return haystack.index(needle)


print(strStr("a", "a"))
