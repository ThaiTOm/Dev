def dinh(a):
    return a[1]


def carTrip(arr, x):
    arr.sort(key=dinh)
    a1 = 0
    a3 = 0
    for i in arr:
        if i[0] >= x:
            print(False)
            return False
        elif i[1] < a3:
            a1 += i[0]
            a3 = min(a3, i[2])
            if a1 > x:
                print(False)
                return False
        else:
            a1 = i[0]
            a3 = i[2]
    print(True)
    return True


carTrip([[1, 2, 5], [3, 3, 7]], 4)
