class Solution:
    def reverseString(self, s: List[str]) -> None:
        if len(s) == 1:
            return [s[0]]
        
        left, right = 0, len(s) -1
        
        while left <= right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
                    
        