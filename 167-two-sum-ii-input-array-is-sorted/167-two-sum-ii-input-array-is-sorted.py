class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        l, r = 0, len(nums) - 1
        
        while l < r:
            sum_ = nums[l] + nums[r]
            
            if sum_ == target:
                return [l+1, r+1]
                
            if sum_ < target:
                l += 1
                
            else:
                r -= 1
        
        