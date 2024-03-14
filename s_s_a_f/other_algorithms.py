def PI(n: int) -> List[int]:
    primes = list( range(2, n) )

    i = 0
    while i < len(primes):
        primes = [x for x in primes if x not in range(primes[i]*2, n+1, primes[i])]
        i += 1
    
    return primes
