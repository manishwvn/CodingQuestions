from typing import List

class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        stone_sum = sum(stones)
        n = len(stones)
        target = stone_sum // 2

        # dp[i][j] = True if subset with sum j is achievable using stones up to index i
        dp = [[False] * (target + 1) for _ in range(n + 1)]
        
        # With 0 stones, subset sum 0 is always possible
        for i in range(n + 1):
            dp[i][0] = True

        for i in range(1, n + 1):
            stone = stones[i - 1]
            for j in range(target + 1):
                # If we don't take the current stone
                dp[i][j] = dp[i - 1][j]
                
                # If we take the current stone (and j >= stone)
                if j >= stone:
                    dp[i][j] = dp[i][j] or dp[i - 1][j - stone]

        # Find the closest subset sum to target
        for j in range(target, -1, -1):
            if dp[n][j]:
                return stone_sum - 2 * j