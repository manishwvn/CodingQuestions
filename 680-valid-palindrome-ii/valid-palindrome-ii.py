class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        i, j = 0, len(s) - 1
        while i < len(s) - 1 and j > -1:
            if s[i] != s[j]:
                skipL, skipR = s[i+1:j+1], s[i:j]
                return (skipL == skipL[::-1] or skipR == skipR[::-1])
            i += 1
            j -= 1
        
        return True

        
        