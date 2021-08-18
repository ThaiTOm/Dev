def sum_of_cubes_odd_number(n):
    if n <= 0:
        return-1
    n = (2*int(n)-1)
    ans = 0
    while n > 0:
        ans += pow(n, 3)
        n -= 2
    print(ans % 1000000007)
    return


sum_of_cubes_odd_number(567)
