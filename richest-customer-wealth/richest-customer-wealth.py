class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        
        wealths = []
        
        for acc in accounts:
            total = 0
            total = sum(acc)
            wealths.append(total)
            
            
        return max(wealths)
        