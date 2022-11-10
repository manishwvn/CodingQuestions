class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        word_set = set(wordDict)
        
        dp = [[]] * (len(s) + 1)
        dp[0] = [""]
        
        for end in range(1, len(s) + 1):
            sub = []
            
            for start in range(0, end):
                word = s[start:end]
                
                if word in word_set:
                    for prefix in dp[start]:
                        sub.append((prefix + " " + word).strip())
                        
            dp[end] = sub
            
        return dp[len(s)]

        
        