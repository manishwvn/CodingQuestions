class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        c1, c2 = collections.Counter(s), collections.Counter(t)
        return c1 == c2
        