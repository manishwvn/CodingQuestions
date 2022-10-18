from math import factorial as f
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        n = numRows
        result = []
        
        for i in range(n):
            temp = []
            for j in range(i+1):
                val = int(f(i)  / (f(i - j) * f(j)))
                temp.append(val)
                
            result.append(temp)
            
        return result
        
        