class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        m, n = len(s), len(p)
        
        s1, p1 = 0, 0
        
        star, temp = -1, -1
        
        while s1 < m:
            
            if p1 < n and (p[p1] == '?' or p[p1] == s[s1]):
                s1 += 1
                p1 += 1
                
            elif p1 < n and p[p1] == "*":
                star = p1
                temp = s1
                p1 += 1
                
            elif star == -1:
                return False
            
            else:
                p1 = star + 1
                s1 = temp + 1
                temp = s1
                
        for i in range(p1, n):
            if p[i] != '*':
                return False
            
        return True
        