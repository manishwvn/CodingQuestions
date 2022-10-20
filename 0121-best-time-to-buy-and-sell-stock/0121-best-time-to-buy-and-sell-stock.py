class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        if len(prices) == 1: return 0
        
        minm, profit = 2 ** 31 - 1, 0
        
        for price in prices:
            if price < minm:
                minm = price
            elif price - minm > profit:
                profit = price - minm
                
        return profit
            
        return profit
            
        