def gen_primes(n):
    sieve= [True] * (n+1)
    sieve[0] = False
    sieve[1] = False
    
    for i in range(2,n+1):
        if sieve[i] == True:
            
            for multiple in range(i*2,n+1,i):
                sieve[multiple ] = False
                
    primes = []
    
    for i in range(2,n+1):
        if sieve[i] :
            primes.append(i)
    return primes
    
print(gen_primes(15))
