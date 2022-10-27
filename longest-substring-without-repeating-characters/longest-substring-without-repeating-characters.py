class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s or len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
         
        char_set = set(s[0])
        i, j = 0, 1
        length = 0
        while j < len(s):
            if s[j] not in char_set:
                char_set.add(s[j])
                j += 1
                
            else:
                char_set.remove(s[i])
                i += 1
        
            length = max(length, len(char_set))
        return length
                
                
                
            
        