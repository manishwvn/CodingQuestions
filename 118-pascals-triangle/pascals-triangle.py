class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        result = [[1]]  

        for i in range(1, numRows):
            temp = [1] * (i + 1)

            for j in range(1, i):
                temp[j] = result[i-1][j-1] + result[i-1][j]
            
            result.append(temp)

        return result