class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        
        dp = {}
        result = 1
        words.sort(key = len)
        
        for word in words:
            dp[word] = 1
            
            for i in range(len(word)):
                prev = word[:i] + word[i+1:]
                if prev in dp:
                    dp[word] = max(dp[word], dp[prev] + 1)
                    result = max(result, dp[word])
                    
        return result
                    
        