class Solution:
    def maxDepth(self, s: str) -> int:
        
        depth = 0
        count = 0
        
        for char in s:
            if char == '(':
                count += 1
                
            if char == ')':
                count -= 1
                
            depth = max(depth, count)
            
        return depth
        
        
        