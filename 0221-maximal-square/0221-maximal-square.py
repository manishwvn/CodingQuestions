class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        
        m= len(matrix)
        n = len(matrix[0]) if m > 0 else 0
        dp = [0 for _ in range(n+1)]
        print(dp)
        res = 0
        prev = 0
        temp = dp[1]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if matrix[i-1][j-1] == '1':
                    temp = dp[j]
                    dp[j] = min(dp[j-1], prev, dp[j]) + 1
                    res = max(res, dp[j])
                    
                else:
                    dp[j] = 0
                    
                prev = temp
                
        return res * res
                
                
        