class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        dp = [[False for _ in range(len(p) + 1)] for _ in range(len(s) + 1)]
        dp[0][0] = True
        
        
        for j in range(1, len(dp[0])):
            if p[j-1] == "*":
                dp[0][j] = dp[0][j-2]
                
        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                
                #normal char
                if p[j-1] != "*":
                    if p[j-1] == s[i-1] or p[j-1] == '.':
                        dp[i][j] = dp[i-1][j-1]
                        
                else:
                    #if *
                    #zero case
                    dp[i][j] = dp[i][j-2]
                    
                    #one case
                    if p[j-2] == s[i-1] or p[j-2] == ".":
                        dp[i][j] = dp[i][j] or dp[i-1][j]
                        
        return dp[-1][-1]
                    
        
        
        