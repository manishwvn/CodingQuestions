class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        result = [[1]]
        if numRows == 1: return result

        for i in range(1, numRows):
            temp = [1]

            for j in range(1, i):
                
                if i == 1 and i == n:
                    temp.append(result[i][j])

                else:
                    temp.append(result[i-1][j-1] + result[i-1][j])
                    
            temp.append(1)
            result.append(temp)

        return result