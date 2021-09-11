class Solution:
    def numTrees(self, n: int) -> int:
        
        dp = [0] * (n+1)
        dp[0] = dp[1] = 1
        
        for i in range(2, len(dp)):
            l, r = 0, i - 1
            
            while(l <= i-1):
                dp[i] += dp[l] * dp[r]
                l += 1
                r -= 1
                
        return dp[n]
        