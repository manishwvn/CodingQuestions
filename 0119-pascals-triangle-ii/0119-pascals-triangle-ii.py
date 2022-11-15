class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        result = []
        
        for i in range(rowIndex+1):
            temp = []
            
            for j in range(i+1):
                
                if j == 0 or j == i:
                    temp.append(1)
                    
                else:
                    value = result[i-1][j-1] + result[i-1][j]
                    temp.append(value)
                    
            result.append(temp)
            
        return result[rowIndex]
                    
            
        