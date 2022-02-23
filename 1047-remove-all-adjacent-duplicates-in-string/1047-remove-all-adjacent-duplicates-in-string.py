class Solution:
    def removeDuplicates(self, s: str) -> str:
        
        if len(s) <= 1:
            return s
        
        result = ""
        stack = []
        
        for char in s:
            if stack and char == stack[-1]:
                stack.pop()
                
                
            else:
                stack.append(char)
                
        for char in stack:
            result += char
            
        return result
        