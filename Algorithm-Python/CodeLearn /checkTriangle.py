def quarantinedPrimes(l, r):
    def primes_method5(f, t):
        out = list()
        sieve = [True] * (t+1)
        for p in range(2, t+1):
            if (sieve[p] and sieve[p] % 2 == 1):
                out.append(p)
                for i in range(p, t+1, p):
                    sieve[i] = False
        return out
    arr = primes_method5(l, r)
    ans = 0
    for i in range(1, len(arr)-1):
        if arr[i] > l and arr[i] < r and (arr[i] - arr[i-1] >= 10) and (arr[i+1] - arr[i] >= 10):
            ans += 1
    print(ans)
    return


quarantinedPrimes(0, 0)
