class Solution:
    def isPal(self, string):
        l, r = 0, len(string) - 1
        
        while l < r:
            if string[l] != string[r]:
                return False
            l += 1
            r -= 1
        return True
        
    
    def breakPalindrome(self, palindrome: str) -> str:
        
        if len(palindrome) == 1: return ""
        
        string = list(palindrome)
        
        for i in range(len(string)):
            if string[i] != 'a':
                string[i] = 'a'
                break
        
        print(f"first: {string}")
        print(self.isPal(string))
        if not self.isPal(string):
            return "".join(string)
        
        string = list(palindrome)
        for i in range(len(string) - 1, -1, -1):
            if string[i] != 'b':
                string[i] = 'b'
                break
        
        print(f"Second: {string}")
        return "".join(string)
        
        
                
        
            
        
        
        
        
        