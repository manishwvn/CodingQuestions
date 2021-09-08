class Solution:
    def numSquares(self, n: int) -> int:
        
        dp = [0] * (n+1)
        dp[1] = 1
        
        for i in range(2, n+1):
            minm = float('inf')
            j = 1
            while(j*j <= i):
                rem = i - (j*j)
                if dp[rem] < minm:
                    minm = dp[rem]
                j += 1
                    
            dp[i] = minm + 1
            
        return dp[n]
        