class Solution:
    def isHappy(self, n: int) -> bool:
        
        def getSqSum(n):
            sqSum = 0
            
            while n:
                rem = n % 10
                n = n // 10
                sqSum += rem ** 2
            
            return sqSum
        
        
        if n == 1: return True
        
        t = getSqSum(n)
        h = getSqSum(getSqSum(n))
        
        if t == 1 or h == 1:
            return True
        
        while t != h:
            
            t = getSqSum(t)
            h = getSqSum(getSqSum(h))
            
            if t == 1 or h == 1:
                return True
            
        return False    
        
            
        
            
        
        
        
            
        