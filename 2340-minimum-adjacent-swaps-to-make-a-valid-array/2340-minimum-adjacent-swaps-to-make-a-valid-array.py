class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:
        
        minm, maxm = float('inf'), float('-inf')
        
        for i in range(len(nums)):
            
            if nums[i] >= maxm:
                maxm = nums[i]
                maxIdx = i
                
            if nums[i] < minm:
                minm = nums[i]
                minIdx = i
        
        if minIdx > maxIdx:
            minIdx -= 1
            
        return (len(nums) - 1 - maxIdx) + (minIdx)