class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if not nums or len(nums) == 0: return 0
        
        if len(nums) == 1: return 1
        
        res = 0
        set_ = set(nums)
        
        for num in nums:
            if num - 1 not in set_:
                curr, curr_length = num, 1
                
                while curr + 1 in set_:
                    curr += 1
                    curr_length += 1
                    
                res = max(curr_length, res)
                
        return res
        
        
        