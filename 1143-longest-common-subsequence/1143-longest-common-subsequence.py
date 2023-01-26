class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        if not text1 or not text2: return 0
        
        if len(text1) < len(text2):
            text1, text2 = text2, text1
        
        
        m, n = len(text1), len(text2)
        
#         dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
        
        
#         for i in range(1,n+1):
#             for j in range(1,m+1):
                
#                 if text1[j-1] == text2[i-1]:
#                     dp[i][j] = 1 + dp[i-1][j-1]
                    
#                 else:
#                     dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                    
#         return dp[-1][-1]


        dp = [0] *(m+1)
    
    
        for i in range(1, n+1):
            prev = dp[0]
            for j in range(1, m+1):
                temp = dp[j]
                if text1[j-1] == text2[i - 1]:
                    dp[j] = prev + 1
                    
                else:
                    dp[j] = max(dp[j-1], dp[j])
                    
                prev = temp
                
        return dp[-1]
            