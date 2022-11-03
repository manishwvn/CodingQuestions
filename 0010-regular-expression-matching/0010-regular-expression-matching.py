class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n = len(p)
        dp = [False] * (n + 1)
        prev = True
        
		# pretreat dp for p like "a*b*ccc*", dp[2] and dp[4] ought to be true.
        for j in range(2, n + 1, 2):
            if p[j - 1] != '*':
                break
            dp[j] = True
        
        for i in range(len(s)):
            for j in range(1, n + 1):
                
                temp = dp[j]  # to store dp[i-1][j-1] (in the original big dp matrix)
                
                if p[j - 1] == '*':
                    dp[j] = dp[j - 2] or dp[j - 1] or (
                        dp[j] and (s[i] == p[j - 2] or p[j - 2] == '.'))
                else:
                    dp[j] = prev and (p[j - 1] == '.' or s[i] == p[j - 1])
                    
                prev = temp
            
            prev = False  # dp[i][0] should be false (in the original big dp matrix)
        
        return dp[n]