class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        if len(temperatures) == 1:
            return [0]
        
        n = len(temperatures)
        result = [0] * n
        
        stack = []
        
        for i in range(n):
            while stack and stack[-1][0] < temperatures[i]:
                temp, idx = stack.pop()
                result[idx] = i - idx
                
            stack.append([temperatures[i], i])
            
        return result
            
        