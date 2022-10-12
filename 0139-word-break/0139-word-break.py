class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        #top down
        n = len(s)
        dp = [False] * (n+1)
        dp[n] = True
        
        for i in range(n-1, -1, -1):
            for word in wordDict:
                m = len(word)
                if i + m <= n and s[i:i+m] == word:
                    dp[i] = dp[i + m]
                    
                if dp[i]:
                    break
                    
        return dp[0]
        
        
        