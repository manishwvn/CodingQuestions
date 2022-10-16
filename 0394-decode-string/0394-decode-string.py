class Solution:
    def decodeString(self, s: str) -> str:
        
        string, number = [], []
        num = 0
        curr = ""
        decode = ""
        
        for char in s:
            if char.isdigit():
                num = num * 10 + int(char)
                
            elif char == "[":
                number.append(num)
                string.append(curr)
                curr = ""
                num = 0 
                
            elif char == "]":
                decode = string.pop() + (curr * number.pop())
                curr = decode
                
            else:
                curr += char
                
        return curr
            
            