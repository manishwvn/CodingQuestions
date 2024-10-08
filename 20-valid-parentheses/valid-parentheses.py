class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []

        for char in s:
            if char in '({[':
                stack.append(char)
            
            else:
                if not stack:
                    return False

                popped = stack.pop()
                if popped == '(' and char != ')':
                    return False
                if popped == '{' and char != '}':
                    return False
                if popped == '[' and char != ']':
                    return False
                
        return stack == []

        