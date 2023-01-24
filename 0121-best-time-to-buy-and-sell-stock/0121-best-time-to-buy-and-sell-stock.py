class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        minm, profit = float('inf'), 0
        
        for price in prices:
            if price < minm:
                minm = price
                
            elif price - minm > profit:
                profit = price - minm
                
        return profit
        