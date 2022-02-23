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
                
#         for char in stack1:
#             if char == "#":
#                 stack1.pop()
        
#         for char in stack2:
#             if char == "#":
#                 stack2.pop()
                
        print(stack1)
        print(stack2)
        
        if stack1 == stack2:
            return True
        else:
            return False
        