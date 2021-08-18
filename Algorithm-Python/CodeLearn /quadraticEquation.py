import math


def quadraticEquation(s):
    arr = s.split("x^2")
    if len(arr) < 2:
        return "Math error"
    br = arr[1].split("*x")
    if len(br) < 2:
        return "Math error"
    cr = br[1].split("=")
    if "*" in arr[0]:
        a = int(arr[0][0:-1])
    elif "^" not in arr[0]:
        a = 1
    else:
        return "Math error"
    print(arr)
    b = int(br[0])
    c = int(cr[0])
    den = pow(b, 2) - (4*a*c)
    if den < 0:
        print("no")
        return "No solution"
    elif den == 0:
        print(-(b/(2*a)))
        return -(b/(2*a))
    else:
        x1 = (-b+math.sqrt(den))/(2*a)
        x2 = (-b-math.sqrt(den))/(2*a)
        print(x1, x2)


quadraticEquation("x^2+2*x-20=0"
                  )
