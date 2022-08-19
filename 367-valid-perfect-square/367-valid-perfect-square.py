class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        start, end = 1, math.sqrt(num)
        while start <= end:
            mid = (start + end) // 2
            if mid * mid == num:
                return True
            if mid * mid > num:
                end = mid - 1
            else:
                start = mid + 1
        
        return False
            
        