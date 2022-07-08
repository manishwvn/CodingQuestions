from collections import Counter as c
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = c(nums)
        
        for key, value in counts.items():
            if value > len(nums) // 2:
                return key
            
        return -1
        