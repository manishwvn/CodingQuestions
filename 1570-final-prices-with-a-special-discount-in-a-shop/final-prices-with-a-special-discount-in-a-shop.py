class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        
        res = prices.copy()
        stack = []
        for i in range(len(prices)):

            while stack and prices[i] <= prices[stack[-1]]:
                j = stack.pop()
                res[j] = prices[j] - prices[i]
            stack.append(i)
        
        return res