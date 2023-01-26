class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        l = 0
        counts = defaultdict(int)
        maxf = 0
        res = 0
        for i in range(len(s)):
            
            counts[s[i]] += 1
#             if s[i] in counts:
#                 counts[s[i]] += 1
                
#             else:
#                 counts[s[i]] = 1
                
            maxf = max(maxf, counts[s[i]])
            while (i - l + 1) - maxf > k:
                counts[s[l]] -= 1
                l += 1
                
            res = max(res, i - l + 1)
            
        return res
            
            
        