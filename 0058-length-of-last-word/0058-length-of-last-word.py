class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        i, length = len(s), 0
        
        while i:
            i -= 1
            
            if s[i] != ' ':
                length += 1
                
            elif length > 0:
                return length
            
        return length
        