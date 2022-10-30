class Solution:
    def checkValidString(self, s: str) -> bool:
        
        min_, max_ = 0, 0 
        
        for char in s:
            if char == '(':
                min_ += 1
                
            else:
                min_ -= 1
                
            if char != ")":
                max_ += 1
                
            else:
                max_ -= 1
                
            if max_ < 0: 
                break
                
            min_ = max(min_, 0)
        
        return min_ == 0
                