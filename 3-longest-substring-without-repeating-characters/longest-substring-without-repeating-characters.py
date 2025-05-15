class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if not s or len(s) == 0:
            return 0
        if len(s) == 1:
            return 1

        char_set = set()
        l = 0
        r = 1
        char_set.add(s[l])
        max_len = 1
        for r in range(1, len(s)):

            #if char is present in set
            if s[r] in char_set:
                while s[r] in char_set:
                    char_set.remove(s[l])
                    l += 1
            #else char is not present
            char_set.add(s[r])
            max_len = max(max_len, r - l + 1)
        
        return max_len