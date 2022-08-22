class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return 0
        
        if len(nums) == 2:
            return 0 if nums[0] > nums[1] else 1
         
        l, r = 0, len(nums) - 1
        
        while l <= r:
            m = (l + r) // 2
            
            if (m == 0 or nums[m] > nums[m-1]) and (m == len(nums) - 1 or nums[m] > nums[m+1]):
                return m
            
            elif m >0 and nums[m] < nums[m-1]:
                r = m - 1
            
            else:
                l = m + 1
        
        
        