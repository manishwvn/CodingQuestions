class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        n = len(digits)
        
        for i in range(n):
            idx = n - i - 1
            
            if digits[idx] == 9:
                digits[idx] = 0
            
            else:
                digits[idx] += 1
                
                return digits
        
        return [1] + digits
        