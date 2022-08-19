class Solution:
    def mySqrt(self, x: int) -> int:
        
        if x == 0:
            return 0
        
        if x == 1:
            return 1
        
        ans = -1
        start, end = 1, x // 2
        
        while start <= end:
            mid = (start + end) // 2
            
            if mid * mid == x:
                return mid
            
            if mid * mid < x:
                start = mid + 1
                ans = mid
                
            else:
                end = mid - 1
                
        return ans
        
            
            