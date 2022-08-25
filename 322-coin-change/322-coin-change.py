class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        if not coins or len(coins) == 0:
            return 0
        
        n,m = len(coins), amount
        dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
        
        for j in range(1, m+1):
            dp[0][j] = m+1
            
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if j < coins[i-1]:
                    dp[i][j] = dp[i-1][j]
                    
                else:
                    dp[i][j] = min(dp[i-1][j], 1 + dp[i][j - coins[i-1]])
        
        return -1 if dp[-1][-1] > amount else dp[-1][-1]
                    
            