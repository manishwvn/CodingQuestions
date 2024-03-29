class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        #1D DP space optimized
        if not coins or len(coins) == 0:
            return 0
    
        n, m = len(coins), amount

        dp = [0] * (m + 1)
        dp[0] = 1
        
        for i in range(1, n+1):
            for j in range(1, m+1):
                if j >= coins[i - 1]:
                    dp[j] = dp[j] + dp[j - coins[i - 1]]
                    
        return dp[-1]
            
        
        
                
        
        