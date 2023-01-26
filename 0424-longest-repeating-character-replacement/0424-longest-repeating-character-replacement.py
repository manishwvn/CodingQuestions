class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        l = 0
        counts = defaultdict(int)
        maxf = 0
        res = 0
        for r in range(len(s)):            
            counts[s[r]] += 1                
            maxf = max(maxf, counts[s[r]])
            
            while (r - l + 1) - maxf > k:
                counts[s[l]] -= 1
                l += 1
                
            res = max(res, r - l + 1)
            
        return res
            
            
        