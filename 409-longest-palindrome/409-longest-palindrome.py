class Solution:
    def longestPalindrome(self, s: str) -> int:
        chars = set()
        count = 0
        for char in s:
            if char in chars:
                count += 2
                chars.remove(char)
            else:
                chars.add(char)
                
        return count + 1 if len(chars) != 0 else count
                
        
        