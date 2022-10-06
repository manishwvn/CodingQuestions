class Solution:
    def removeDuplicates(self, s: str) -> str:
        
        stack = []
        result = ""
        
        for i in range(len(s)):
            if not stack or stack[-1] != s[i]:
                stack.append(s[i])
                
            else:
                stack.pop()
                
        for char in stack:
            result += char
            
        return result
        