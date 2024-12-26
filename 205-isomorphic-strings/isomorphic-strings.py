class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        hms, hmt = {}, {}

        for i in range(len(s)):
            char1, char2 = s[i], t[i]
            if (char1 in hms and hms[char1] != char2) or (char2 in hmt and hmt[char2] != char1):
                return False
            hms[char1] = char2
            hmt[char2] = char1
        return True 
        