class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        if not nums or len(nums) == 0: return 0            
        
        if len(nums) == 1: return 1
        
        result = [nums[0]]
        
        for i in range(1, len(nums)):
            if nums[i] > result[-1]:
                result.append(nums[i])
                
            else:
                j = 0
                while nums[i] > result[j]:
                    j += 1
                    
                result[j] = nums[i]
        
        print(result)
        return len(result)