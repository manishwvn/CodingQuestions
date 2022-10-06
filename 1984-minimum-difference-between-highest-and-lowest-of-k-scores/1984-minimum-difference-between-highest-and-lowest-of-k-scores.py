class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        
        nums.sort()
        l = 0
        curr, minm = 0, nums[-1] - nums[0] 
        for r in range(l+k - 1, len(nums)):
            curr = nums[r] - nums[l]
            minm = min(curr, minm)
            l += 1
            
        return minm
        
        