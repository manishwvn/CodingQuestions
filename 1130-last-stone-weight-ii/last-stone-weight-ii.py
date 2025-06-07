from typing import List

class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        stone_sum = sum(stones)
        target = stone_sum // 2  # We aim to get as close to this as possible

        dp = [False] * (target + 1)
        dp[0] = True  # Zero sum is always possible (by taking no stones)

        for stone in stones:
            for j in range(target, stone - 1, -1):  # iterate backward
                if dp[j - stone]:
                    dp[j] = True

        # Find the largest j such that dp[j] is True
        for j in range(target, -1, -1):
            if dp[j]:
                # The two subsets are j and stone_sum - j
                return stone_sum - 2 * j