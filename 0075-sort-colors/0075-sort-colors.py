class Solution:
    def sortColors(self, nums: List[int]) -> None:
        
        l, p, r = 0, 0, len(nums) - 1
        
        while p <= r:
            
            if nums[p] == 0:
                nums[l], nums[p] = nums[p], nums[l]
                l += 1
                p += 1
                
                
            elif nums[p] == 2:
                nums[p], nums[r] = nums[r], nums[p]
                r -= 1
                
            else:
                p += 1
                
                
                
            