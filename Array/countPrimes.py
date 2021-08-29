#https://leetcode.com/problems/count-primes/
class Solution(object):
    def countPrimes(self, n):
        if n < 3:
            return 0
        primes = [1] * n
        primes[0] = primes[1] = False
        for i in range(0, int(n ** 0.5)+1): # Range 0 to sqrt(n)
            if primes[i]:                   # Only look at values still potentially marked as prime.
                for j in range(i*i, n, i):  # a[start:stop:step] # start through not past stop, by step
                    primes[j] = 0
                    
        return sum(primes)                  
                
        """
        :type n: int
        :rtype: int
        """
        