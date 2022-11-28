class Solution:
    def calculate(self, s: str) -> int:
        
        i = 0
        curr = res = prev = 0
        op = "+"
        
        while i < len(s):
            
            char = s[i]
            
            if char.isdigit():
                while i < len(s) and s[i].isdigit():
                    curr = curr * 10 + int(s[i])
                    i += 1
                    
                i -= 1
                
                if op == "+":
                    res += curr    
                    prev = curr
                    
                elif op == "-":
                    res -= curr
                    prev = -curr
                    
                elif op == "*":
                    
                    res -= prev
                    res += prev * curr
                    prev = prev * curr
                    
                else:
                    res -= prev
                    res += int(prev / curr)
                    prev = int(prev / curr)
                
                curr = 0
                
            elif char != " ":
                op = char
                
            i += 1
                
        return res
                
                
        
        
        
        