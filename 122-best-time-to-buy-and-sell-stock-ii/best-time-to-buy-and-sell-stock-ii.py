class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        prev = float('inf')
        curr_profit, max_profit = 0, 0

        for curr in prices:
            if curr > prev:
                curr_profit = curr - prev
                max_profit += curr_profit
            prev = curr
        return max_profit
        