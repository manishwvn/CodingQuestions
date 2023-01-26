class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if not nums or len(nums) == 1:
            return 0 if not nums else 1
        
        set_ = set(nums)
        
        result = 0
        
        for i in range(len(nums)):
            
            forw, back = 0, 0
            
            num = nums[i]
            while num + 1 in set_:
                forw += 1
                set_.remove(num+1)
                num += 1
                            
            num = nums[i]
            
            while num -1 in set_:
                back += 1
                set_.remove(num-1)
                num -= 1
                            
            result = max(back+forw+1, result)
        
        return result
        
        