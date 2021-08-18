def parse_int(s):
    num = {"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10, "eleven": 11, "twelve": 12,
           "thirteen": 13, "fourteen": 14, "fifteen": 15, "sixteen": 16, "seventeen": 17, "eighteen": 18, "nineteen": 19,
           "twenty": 20, "thirty": 30, "forty": 40, "fifty": 50, "sixty": 60, "seventy": 70, "eighty": 80, "ninety": 90, }
    multiMap = {"hundred": 100, "thousand": 1000, "million": 1000000}
    value = s.split(" ")
    ans = 0
    for i in value:
        if i in num:
            ans += num[i]
        elif i in multiMap:
            old = multiMap[i] * \
                (ans % 10) if ans % 10 != 0 else multiMap[i] * 1
            ans = multiMap[i]*ans if old > ans else(old - (ans % 10)) + ans
        elif len(i.split("-")) > 1:
            x = i.split("-")
            ans = ans + num[x[0]] + num[x[1]]
    print(ans)


parse_int("eighteen")
