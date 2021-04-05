class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        hm = {}
        for i in range(len(nums)):
            hm[nums[i]] = True
            
        for i in range(len(nums)):
            if nums[i] - 1 in hm:
                hm[nums[i]] = False
                
        curr_len, max_len = 0, 0
                
        for i in range(len(nums)):
            if hm[nums[i]] == True:
                val = nums[i]
                curr_len = 1
                
                while(val + curr_len in hm):
                    curr_len += 1
                
                if curr_len > max_len:
                    max_len = curr_len
                    
        return max_len
                    
            
                
        
        