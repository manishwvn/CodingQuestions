class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        m, n = len(text1), len(text2)
        memo = [[0 for _ in range(n+1)] for _ in range(m+1)]
        
        def helper(text1, text2, m, n):
            
            if m == 0 or n == 0:
                return 0
            
            if memo[m][n] != 0:
                return memo[m][n]
            
            if text1[m - 1] == text2[n - 1]:
                memo[m][n] = 1 + helper(text1, text2, m - 1, n - 1)
                
            else:
                memo[m][n] = max(helper(text1, text2, m, n - 1), helper(text1, text2, m - 1, n))
            
            return memo[m][n]
        
        return helper(text1, text2, m, n)
        