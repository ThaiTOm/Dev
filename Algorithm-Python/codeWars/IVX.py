def solution(a):
    symbol = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    ans = 0
    old = 0
    for i in a[::-1]:
    	if symbol[i] < old:
    		ans = ans - symbol[i]
    	else:
    		ans = ans + symbol[i]
    	old = symbol[i]
    print(ans)


solution("XIVV")