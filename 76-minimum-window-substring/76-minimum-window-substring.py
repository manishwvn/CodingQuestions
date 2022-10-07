class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if s == t: return s
        
        if len(t) > len(s): return ""
        
        counts_t, window = Counter(t), {}
        have, need = 0, len(counts_t)
        result, length = [-1,-1], float("inf")
        l = 0
        
        for r in range(len(s)):
            char = s[r]
            window[char] = 1 + window.get(char, 0)
            
            if char in counts_t and window[char] == counts_t[char]:
                have += 1
                
            while have == need:
                if r - l + 1 < length:
                    result = [l, r]
                    length = r - l + 1
                    
                window[s[l]] -= 1
                
                if s[l] in counts_t and window[s[l]] < counts_t[s[l]]:
                    have -= 1
                    
                l += 1
                
        l, r = result
        return s[l:r+1]
        
                    
                    
                
            
        
        