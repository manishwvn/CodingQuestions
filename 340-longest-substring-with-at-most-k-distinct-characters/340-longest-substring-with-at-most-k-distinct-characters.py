class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        
        if not str or k == 0:
            return 0
        
        l, r = 0, 0
        max_len = 1
        hm = OrderedDict()
        for r in range(0, len(s)):
            
            if s[r] in hm:
                del hm[s[r]]
                
            hm[s[r]] = r
            
            if len(hm) == k + 1:
                char, i = hm.popitem(last = False)
                l = i + 1
                
            max_len = max(max_len, r - l + 1)
            
        return max_len
            

                
            
        