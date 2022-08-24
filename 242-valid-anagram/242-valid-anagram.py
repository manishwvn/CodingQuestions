class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        c1= collections.Counter(s)
        
        for char in t:
            if char in c1:
                c1[char] -= 1
                if not c1[char]:
                    del c1[char]
        
        return len(c1) == 0
        