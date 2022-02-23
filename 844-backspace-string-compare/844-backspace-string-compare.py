class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        if s == t:
            return True
        
        stack1, stack2 = [], []
        
        for char in s:
            if stack1 and char == "#":
                stack1.pop()
                
            if char != "#":
                stack1.append(char)
                
        for char in t:
            if stack2 and char == "#":
                stack2.pop()
                
            if char != "#":
                stack2.append(char)
                

        
        return stack1 == stack2
            
        