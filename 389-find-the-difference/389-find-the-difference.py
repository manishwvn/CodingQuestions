class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        
        if len(s) == 0:
            return t
        
        hm = collections.Counter(t)
        for char in s:
            if char in hm:
                hm[char] -= 1
                if hm[char] == 0:
                    del hm[char]
        
        result = list(hm.keys())
        return str(result[0])
            
            
        