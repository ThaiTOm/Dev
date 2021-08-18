def intToRoman(num):
    units = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
    dozens = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
    hundreds = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']

    bb = ['', 'M', 'MM', 'MMM']

    u = units[int(num % 10)]
    d = dozens[int((num % 100)/10)]
    h = hundreds[int((num % 1000)/100)]
    b = bb[int(num/1000)]
    # print(h,d,u)

    roman = b + h+d + u
    return roman
