class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        #2D DP
        if not coins or len(coins) == 0:
            return 0
    
        n, m = len(coins), amount
        dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
    
        for i in range(n+1):
            dp[i][0] = 1

        for j in range(1, m+1):
            dp[0][j] = 0
    
        for i in range(1, n+1):
            for j in range(1, m+1):

                if j < coins[i-1]:
                    dp[i][j] = dp[i-1][j]

                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j - coins[i - 1]]

        return dp[-1][-1]
                    
        
                
        
        