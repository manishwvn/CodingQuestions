class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        if len(nums) == 1: return 0
        
        l, r = 0, len(nums) - 1
        
        while l <= r:
            
            mid = (l + r) // 2
            
            if (mid == 0 or nums[mid] > nums[mid-1]) and (mid == len(nums) - 1 or nums[mid] > nums[mid+1]):
                return mid
            
            elif mid > 0 and nums[mid] < nums[mid-1]:
                r = mid - 1
                
            else:
                l = mid + 1
                
        
        