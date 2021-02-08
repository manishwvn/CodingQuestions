import math
class Solution:
    def countPrimes(self, n: int) -> int:
        
        if n <= 2:
            return 0
        
        primes = [True] * (n+1)
        primes[0] = False
        primes[1] = False
        
        for p in range(2, int(math.sqrt(n) + 1)):
            if primes[p] == True:
                for i in range(p*p, n+1, p):
                    primes[i] = False
                    
        count = 0
        for i in range(0, len(primes) - 1):
            if primes[i] == True:
                count += 1
                
        return count
            
            