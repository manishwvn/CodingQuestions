class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        #using hashmap
        
        l = 0
        counts = {}
        res = 0
        for i in range(len(s)):
            if s[i] in counts:
                counts[s[i]] += 1
                
            else:
                counts[s[i]] = 1
                
            while (i - l + 1) - max(counts.values()) > k:
                counts[s[l]] -= 1
                l += 1
                
            res = max(res, i - l + 1)
            
        return res
            
            