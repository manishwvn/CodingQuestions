class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 0:
            return True
        
        newstr = ''
        
        for char in s:
            if char.isalnum():
                newstr += char.lower()
                
        return newstr == newstr[::-1]
            
        