class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        n = len(matrix)
        
        def calc_count(matrix, mid, small, large):
            count = 0
            n = len(matrix)
            
            row, col = n - 1, 0
            
            while row >= 0 and col < n:
                if matrix[row][col] > mid:
                    
                    large = min(large, matrix[row][col])
                    row -= 1
                    
                else:
                    
                    small = max(small, matrix[row][col])
                    count += row + 1
                    col += 1
                    
            return count, small, large
        
        
        l, r = matrix[0][0], matrix[-1][-1]
        
        while l < r:
            mid = (l + r) // 2
            
            small, large = matrix[0][0], matrix[-1][-1]
            
            count, small, large = calc_count(matrix, mid, small, large)
            
            if count == k:
                return small
            
            if count < k:
                l = large
                
            else:
                r = small
                
        return l
                
        