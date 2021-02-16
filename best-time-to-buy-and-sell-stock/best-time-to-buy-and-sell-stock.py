class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        
        max_profit, min_price = 0, prices[0]
        
        for i in range(0, len(prices)):
            min_price = min(min_price, prices[i])
            max_profit = max(prices[i] - min_price, max_profit)
            
        return max_profit
        
        