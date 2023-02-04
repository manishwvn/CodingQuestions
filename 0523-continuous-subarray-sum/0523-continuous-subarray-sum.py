class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
    
        hm = {0: -1}
        prefix_sum = 0
        
        for i, num in enumerate(nums):
            
            prefix_sum = (prefix_sum + num) % k
            
            if prefix_sum not in hm:
                hm[prefix_sum] = i
            else:
                if i - hm[prefix_sum] >= 2:
                    return True
        
        return False
            
        
        