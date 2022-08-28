class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False
        
        stack = []
        for char in s:
            if char in "({[":
                stack.append(char)
            
            elif len(stack) > 0:
                popped = stack.pop()
                if popped == '(' and char != ')':
                    return False
                elif popped == '[' and char != ']':
                    return False
                elif popped == '{' and char != '}':
                    return False
            
            else:
                return False
                    
        return len(stack) == 0
                
        