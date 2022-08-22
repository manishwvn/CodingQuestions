class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        m, n = len(matrix), len(matrix[0])
        r, c = m - 1, 0
        
        while r >= 0 and c < n:
            if matrix[r][c] == target:
                return True
            
            if matrix[r][c] > target:
                r -= 1
                
            if matrix[r][c] < target:
                c += 1
                
        return False
                
        