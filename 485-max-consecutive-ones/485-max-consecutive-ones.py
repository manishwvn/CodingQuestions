class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return 0 if not nums[0] else 1
        
        best_max = 0
        curr_max = 0
        for i in nums:
            if i == 1:
                curr_max += 1
                
            else:
                curr_max = 0
            
            best_max = max(best_max, curr_max)
            
        return best_max
        