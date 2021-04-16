class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        
        result = []
        
        for i in range(0, len(nums)):
            for j in range(0, len(nums)):
                
                if nums[i] == nums[j] and i < j:
                    result.append((i,j))
                    
                    
        return len(result)
        