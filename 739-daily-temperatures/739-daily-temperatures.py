class Solution:
    def dailyTemperatures(self, t: List[int]) -> List[int]:
        
        n = len(t)
        
        result = [0] * n
        
        for i in range(n - 2, -1, -1):
            count = 1
            
            while count and t[i + count] <= t[i]:
                
                if result[i + count]:
                    count += result[i + count]
                    
                else:
                    count = 0
                    
            result[i] = count
                    
        return result
        