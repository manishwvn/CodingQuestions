class Solution:
    def reverseVowels(self, s: str) -> str:
        if len(s) == 1:
            return s[0]
        
        vowels = "aeiouAEIOU"
        reverse = [None for _ in range(len(s))]
        left, right = 0, len(s) - 1
        while left <= right:
            if s[left] in vowels and s[right] in vowels:
                reverse[left] = s[right]
                reverse[right] = s[left]
                left += 1
                right -= 1
            
            elif s[left] in vowels and s[right] not in vowels:
                reverse[right] = s[right]
                right -= 1
                
            elif s[left] not in vowels and s[right] in vowels:
                reverse[left] = s[left]
                left += 1
                
            else:
                reverse[left] = s[left]
                reverse[right] = s[right]
                left += 1
                right -= 1
                
        rev_str = "".join(char for char in reverse)
        return rev_str
            