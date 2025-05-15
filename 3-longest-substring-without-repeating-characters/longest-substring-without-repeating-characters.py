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
        while r < len(s):

            #if char is present in set
            if s[r] in char_set:
                char_set.remove(s[l])
                l += 1

            #else char is not present
            else:
                char_set.add(s[r])
                r += 1

            max_len = max(max_len, len(char_set))
        
        return max_len