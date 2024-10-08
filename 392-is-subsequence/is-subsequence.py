class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        if len(s) > len(t): return False
        m, n, i, j = len(s), len(t), 0, 0

        while i < m and j < n:
            if s[i] == t[j]:
                i += 1
            j += 1
        
        return i == m
        