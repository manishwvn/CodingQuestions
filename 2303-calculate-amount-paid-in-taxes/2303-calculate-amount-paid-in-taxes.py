class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        
        brackets = [[0, 0]] + brackets 

        total = 0
        for i in range(1, len(brackets)):
            
            diff = min(income, brackets[i][0] - brackets[i - 1][0])
            total += diff * (brackets[i][1] / 100)
            income = max(income - diff, 0)
            
        return total