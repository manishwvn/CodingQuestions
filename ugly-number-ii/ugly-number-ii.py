class Solution:
    def nthUglyNumber(self, n: int) -> int:
        
        if n == 1:
            return 1
        
        dp = [0] * (n+1)
        
        dp[1] = 1
        
        p2, p3, p5 = 1, 1, 1
        
        for i in range(2, n+1):
            f1 = 2 * dp[p2]
            f2 = 3 * dp[p3]
            f3 = 5 * dp[p5]
            
            dp[i] = min(f1, min(f2, f3))
            
            if dp[i] == f1:
                p2 += 1
                
            if dp[i] == f2:
                p3 += 1
                
            if dp[i] == f3:
                p5 += 1
                
        return dp[n]
        
        
        