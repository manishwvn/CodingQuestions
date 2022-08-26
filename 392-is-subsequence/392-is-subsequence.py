class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        
        i, j = 0, 0
        while i <=len(t) -1 and j <= len(s) -1:
            if t[i] == s[j]:
                i += 1
                j += 1
                
            else:
                i += 1
                
            if j == len(s):
                return True
            
        return False
        