class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        if target > nums[-1]:
            return len(nums)
        
        if target <= nums[0]:
            return 0
        
        start, end = 0, len(nums) - 1
        result = None
    
        while(start < end):
            
            mid = (start + end) // 2
            
            if target == nums[mid]:
                return mid
            
            elif target > nums[mid]:
                start = mid + 1
            
            else:
                end = mid - 1
            
                
        if nums[start] < target:
            return start + 1
        return start
                
        
            
        