class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        hm1, hm2 = {}, {}
        for i in range(len(s)):
            c1, c2 = s[i], t[i]
            if (c1 in hm1 and hm1[c1] != c2) or (c2 in hm2 and hm2[c2] != c1):
                return False
            hm1[c1] = c2
            hm2[c2] = c1

        return True
            

        