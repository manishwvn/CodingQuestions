class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m, n = len(matrix), len(matrix[0])
        self.sum_matrix = [[0] * (n+1) for _ in range(m+1)]
        
        for i in range(m):
            prefix = 0
            for j in range(n):
                prefix += matrix[i][j]
                above = self.sum_matrix[i][j+1]
                self.sum_matrix[i+1][j+1] = prefix + above

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        
        row1 += 1
        row2 += 1
        col1 += 1
        col2 += 1
        
        br = self.sum_matrix[row2][col2]
        ab = self.sum_matrix[row1 - 1][col2]
        left = self.sum_matrix[row2][col1 - 1]
        topleft = self.sum_matrix[row1 - 1][col1 - 1]
        
        return br - ab - left + topleft
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)