class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        
        dp = [[0 for i in range(K+1)] for j in range(N+1)] 
        
        for i in range(1, N+1):
            for j in range(1, K+1):
                dp[i][j] = 1 + dp[i-1][j] + dp[i-1][j-1]
                if dp[i][j] >= N:
                    return i
                
            
                    
                
        