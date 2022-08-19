class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        
        if num == 0 or num == 1:
            return True
    
        start, end = 1, num
        
        while start <= end:
            mid = (start + end) // 2
            
            if mid * mid == num:
                return True
            
            if mid * mid > num:
                end = mid - 1
                
            else:
                start = mid + 1
        
        return False
            
        