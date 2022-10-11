class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        
        n = len(arr)
        dp = [0] * n
        dp[0] = arr[0]
        
        for i in range(1, len(arr)):
            maxm = arr[i]
            for j in range(1, k+1):
                if i - j + 1 >= 0:
                    maxm = max(maxm, arr[i - j + 1])
                    if i - j >= 0:
                        curr = j * maxm + dp[i - j]
                        
                    else:
                        curr = j * maxm
                        
                    dp[i] = max(dp[i], curr)
                
        return dp[-1]
        
        