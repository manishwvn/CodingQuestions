class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        if len(nums) < 2:
            return 0
        
        start, end = 0, len(nums) - 1
        maxint = 2 ** 31
        while start <= end:
            mid = (start + end) // 2
            left = nums[mid - 1] if mid else -maxint
            right = nums[mid + 1] if mid < len(nums) - 1 else -maxint
            if nums[mid] > left and nums[mid] > right:
                return mid
            
            elif nums[mid] < right:
                start = mid + 1
                
            else:
                end = mid - 1
                
        
            
        