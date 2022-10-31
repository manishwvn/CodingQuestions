class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        
        numStr = "123456789"
        
        result = []
        n = 10
        
        for j in range(len(str(low)), len(str(high)) + 1):
            for i in range(n - j):
                num = int(numStr[i:i+j])
                
                if num >= low and num <= high:
                    result.append(num)
                    
        return result
            
            
        