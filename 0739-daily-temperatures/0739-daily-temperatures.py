class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        if len(temperatures) == 1:
            return [0]
        
        n = len(temperatures)
        result = [0] * n
        
        maxm = 0
        
        for i in range(n-1, -1, -1):
            if temperatures[i] >= maxm:
                maxm = temperatures[i]
                continue
                
            days = 1
            while temperatures[i + days] <= temperatures[i]:
                days += result[i + days]
                
            result[i] = days
            
        return result
            
        