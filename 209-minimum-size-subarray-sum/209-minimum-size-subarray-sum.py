class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        l, sum_ = 0, 0 
        res = float("inf")
        
        for r in range(len(nums)):
            sum_ += nums[r]
            
            while sum_ >= target:
                res = min(r - l + 1, res)
                sum_ -= nums[l]
                l += 1
            
        return 0 if res == float("inf") else res
        
                
            
        