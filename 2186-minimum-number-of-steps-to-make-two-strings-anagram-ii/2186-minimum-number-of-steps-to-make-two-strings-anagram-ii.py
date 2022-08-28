class Solution:
    def minSteps(self, s: str, t: str) -> int:
        c1, c2 = Counter(s), Counter(t)
        
        if len(s) == len(t) and c1 == c2:
            return 0
        
        for char in t:
            if char in c1:
                c1[char] -= 1
                if c1[char] == 0:
                    c1.pop(char)
                    
                c2[char] -= 1
                if c2[char] == 0:
                    c2.pop(char)
                
        return sum(list(c1.values())) + sum(list(c2.values()))
                
        