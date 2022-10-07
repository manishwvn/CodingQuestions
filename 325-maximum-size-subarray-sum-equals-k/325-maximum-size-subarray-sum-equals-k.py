class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        
        prefix = 0
        hm = {}
        result = 0
        
        for i, num in enumerate(nums):
            prefix += num
            
            if prefix == k:
                result = i + 1
                
            if prefix - k in hm:
                result = max(result, i - hm[prefix - k])
                
            if prefix not in hm:
                hm[prefix] = i
          
        return result
            
            
        
        