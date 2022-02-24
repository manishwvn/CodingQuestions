class Solution:
    def findBuildings(self, h: List[int]) -> List[int]:
        
        if len(h) == 1:
            return [0]
        
        n = len(h)
        
        buffer = [-1] * n
        buffer[-1] = n - 1
        
        stack = [h[n-1]]
        result = []
        
        for i in range(n-2, -1, -1):
            if h[i] > stack[-1]:
                buffer[i] = i
                stack.pop()
                stack.append(h[i])
                
        for num in buffer:
            if num != -1:
                result.append(num)
        
        return result
        