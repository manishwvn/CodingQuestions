class Solution:
    def maxPower(self, s: str) -> int:
        
        if len(s) == 1:
            return 1
        
        curr_pow, max_pow = 1, 1
        for i in range(1, len(s)):
            if s[i] != s[i - 1]:
                curr_pow = 1
                
            else:
                curr_pow += 1
                
            max_pow = max(curr_pow, max_pow)
            
        return max_pow
                
        