class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        m, n = len(matrix), len(matrix[0])
        
        if target < matrix[0][0] or target > matrix[-1][-1]: return False
        
        
        l, r = 0, m - 1
        
        while l <= r:
            
            mid = (l + r) // 2
            
            if matrix[mid][0] == target:
                return True
            
            if mid == r:
                l2 = mid
                break
            
            elif matrix[mid][0] < target and matrix[mid+1][0] > target:
                l2 = mid
                break
                
            elif matrix[mid][0] < target:
                l = mid + 1
                
            else:
                r = mid - 1
                
        r2 = n - 1
        r = l2
        l2 = 0
        while l2 <= r2:
            
            mid = (l2 + r2) // 2
            # print(matrix[r][mid])
            
            if matrix[r][mid] == target:
                return True
            
            elif matrix[r][mid] < target:
                l2 = mid + 1
                
            else:
                r2 = mid - 1
                
        return False