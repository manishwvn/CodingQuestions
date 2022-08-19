class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        start, end = -1, -1
        
        for i, val in enumerate(nums):
            if val == target:
                start = i
                break
                
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == target:
                end = i
                break
                
        return [start, end]
            
            
        