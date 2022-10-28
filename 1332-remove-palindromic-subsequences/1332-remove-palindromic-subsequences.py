class Solution:
    def isPal(self, s):
        l, r = 0, len(s) - 1
        
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
            
        return True
            
    def removePalindromeSub(self, s: str) -> int:
        if not s: return 0
        if self.isPal(s): return 1
        return 2
        
        
        