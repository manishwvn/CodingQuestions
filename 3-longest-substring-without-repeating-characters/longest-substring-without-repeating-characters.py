class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if not s or len(s) == 0:
            return 0
        if len(s) == 1:
            return 1

        char_index = {}
        l = 0
        max_len = 0
        for r in range(len(s)):
            #if char is present in hm 
            if s[r] in char_index and char_index[s[r]] >= l:
                l = char_index[s[r]] + 1
            char_index[s[r]] = r
            max_len = max(max_len, r - l + 1)
        
        return max_len