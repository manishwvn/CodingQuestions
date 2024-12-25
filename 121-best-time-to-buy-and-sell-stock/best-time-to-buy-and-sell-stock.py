class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        prev, curr_profit, max_profit = prices[0], 0, 0

        for curr in prices:
            if curr < prev:
                prev = curr
            else:
                curr_profit = curr - prev
                max_profit = max(curr_profit, max_profit)
        
        return max_profit
        