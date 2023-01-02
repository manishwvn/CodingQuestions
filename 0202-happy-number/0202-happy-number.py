class Solution:
    def isHappy(self, n: int) -> bool:
        
        def getSqSum(n):
            sqSum = 0
            
            while n:
                rem = n % 10
                n = n // 10
                sqSum += rem ** 2
            
            return sqSum
        
        
        hm = set()
        while n not in hm:
            hm.add(n)
            n = getSqSum(n)
            
            if n == 1:
                return True
            
            if n in hm:
                return False
            
            
            
        return True
            
        
            
        
        
        
            
        