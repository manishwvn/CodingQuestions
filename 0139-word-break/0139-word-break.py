class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        #top down
        n = len(s)
        dp = [False] * (n+1)
        dp[0] = True
        
        word_set = set(wordDict)
        
        for i in range(len(dp)):
            for j in range(0, i):
                
                if dp[j] and s[j:i] in word_set:
                    
                    dp[i] = True
                    break
                    
        return dp[-1]
        
        
        