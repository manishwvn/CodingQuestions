class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        buyIdx, sellIdx = 0, 0
        profit = 0

        for i in range(1, len(prices)):
            if prices[i] >= prices[i - 1]:
                sellIdx += 1

            else:
                profit += prices[sellIdx] - prices[buyIdx]
                buyIdx, sellIdx = i, i

        profit += prices[sellIdx] - prices[buyIdx]

        return profit
        