class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        if len(s) == 0:
            return -1
        
        hm = {}
        for char in s:
            if char in hm:
                hm[char] += 1
            else:
                hm[char] = 1
                
        for i in hm:
            if hm[i] == 1:
                return s.index(i)
        return -1
        