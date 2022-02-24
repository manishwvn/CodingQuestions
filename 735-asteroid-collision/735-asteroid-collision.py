class Solution:
    def asteroidCollision(self, a: List[int]) -> List[int]:
        
        if not a:
            return []
        
        stack = []
        
        for i in range(len(a)):
            if not stack or a[i] > 0:
                stack.append(a[i])
                
            else:
                while True:
                    if stack[-1] < 0:
                        stack.append(a[i])
                        break
                        
                    elif stack[-1] == -a[i]:
                        stack.pop()
                        break
                        
                    elif stack[-1] > -a[i]:
                        break
                    
                    else:
                        stack.pop()
                        if not stack:
                            stack.append(a[i])
                            break
                            
        
        return stack
            
            
            
        