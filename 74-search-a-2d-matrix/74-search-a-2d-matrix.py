class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        m = len(matrix)
        n = len(matrix[0])
        
        for i in range(0, m):
            low, high = 0, n - 1
            
            while low <= high:
                mid = (low + high) // 2
                
                if matrix[i][mid] == target:
                    return True
                elif target > matrix[i][mid]:
                    low = mid + 1
                else:
                    high = mid - 1
        
        return False
        