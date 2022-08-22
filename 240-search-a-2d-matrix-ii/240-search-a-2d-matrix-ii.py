class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        def bs(nums, target):
            l, r = 0, len(nums) - 1
            
            while l <= r:
                m = (l + r) // 2
                if nums[m] == target:
                    return True
                elif target > nums[m]:
                    l = m + 1
                    
                else:
                    r = m - 1
                    
            return False
        
        for i in range(len(matrix)):
            
            is_val = bs(matrix[i], target)
            if is_val:
                return True
            else:
                continue
            return False
            
            
                
                
                
        