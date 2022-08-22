class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        l, r = 0, len(nums) - 1
        while l <= r:
            #already sorted
            if nums[l] <= nums[r]:
                return nums[l]
            
            m = (l+r) // 2
            
            if (m == 0 or nums[m] <= nums[m-1]) and (m == len(nums) -1 or nums[m] <= nums[m+1]):
                return nums[m]
            
            elif nums[m] >= nums[l]:
                l = m + 1
                
            else:
                r = m - 1
                
        return -1
            
                
        