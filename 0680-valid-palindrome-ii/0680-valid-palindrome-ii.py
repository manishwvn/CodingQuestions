class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        def isPal(string, l, r):
            
            while l < r:
                if string[l] != string[r]:
                    return False
                l += 1
                r -= 1
                
            return True
        
        l, r = 0, len(s) - 1
        
        while l < r:
            if s[l] != s[r]:
                return isPal(s, l, r-1) or isPal(s, l+1, r)
            l += 1
            r -= 1
            
        return True
                
        
        
            
        
        
        