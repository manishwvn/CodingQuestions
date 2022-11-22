class Solution:
    def calculate(self, s: str) -> int:
        
        result, curr, sign, = 0, 0, 1
        stack = []
        
        for char in s:
            #digit
            if char.isdigit():
                curr = curr * 10 + int(char)
            
            #+-
            elif char in "+-":
                result += (curr * sign)
                curr = 0
                if char == "-":
                    sign = -1
                    
                else:
                    sign = 1
            
            #(
            elif char == "(":
                stack.append(result)
                stack.append(sign)
                result = 0
                sign = 1
            
            #)
            elif char == ")":
                result += (curr * sign)
                result *= stack.pop()
                result += stack.pop()
                curr = 0
        
        return result + (curr * sign)
        